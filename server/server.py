from prometheus_client import Summary, Counter, Histogram, generate_latest
from http.server import BaseHTTPRequestHandler, HTTPServer

# Create a metric to track time spent and requests made.
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')
REQUEST_COUNT = Counter('request_count', 'Total count of requests')


class HelloHandler(BaseHTTPRequestHandler):
    # Decorate function with time metric to track how long it takes to process requests.
    @REQUEST_TIME.time()
    def do_GET(self):
        # Increment counter for each request made.
        REQUEST_COUNT.inc()

        # if url is '/metrics':
        if self.path == '/metrics':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain; version=0.0.4; charset=utf-8')
            self.end_headers()

            # Generate prometheus metrics.
            self.wfile.write(generate_latest())

        else:
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'Hello, World!')

# Create a web server and define the handler
httpd = HTTPServer(('', 8000), HelloHandler)
print('Server running on port 8000...')

# Wait forever for incoming http requests
httpd.serve_forever()
