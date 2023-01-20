import requests
import random
import time

url = "http://server:8000"


# Send requests to the server in a loop with a random interval between 1ms and 500ms
while True:
    time.sleep(random.uniform(0.001, 0.1)) # sleep for a random interval between 1ms and 500ms
    response = requests.get(url)
    print(response.text)
