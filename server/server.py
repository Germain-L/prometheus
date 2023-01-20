from prometheus_client import Summary, Counter, Histogram, generate_latest
from http.server import BaseHTTPRequestHandler, HTTPServer

REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')
REQUEST_COUNT = Counter('request_count', 'Total count of requests')

class HelloHandler(BaseHTTPRequestHandler):
    @REQUEST_TIME.time()
    def do_GET(self):
        REQUEST_COUNT.inc()
        if self.path == '/metrics':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain; version=0.0.4; charset=utf-8')
            self.end_headers()
            self.wfile.write(generate_latest())
        else:
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'Hello, World!')

httpd = HTTPServer(('', 8000), HelloHandler)
print('Server running on port 8000...')
httpd.serve_forever()
