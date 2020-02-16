import json
import time

import requests
from queue import Queue
from threading import Thread

# Defaults
REQUEST_TIMEOUT = 10.0
REQUEST_DELAY = 2.0
REQUEST_QUEUE_MAX_SIZE = 100
PROBLEMS_URL = 'https://dmoj.ca/api/problem/list'


def get_json(url):
    return json.loads(requests.get(url))


def request_submissions(user):
    return get_json(f'https://dmoj.ca/api/user/submissions/{user}')


def request_problems():
    return get_json(PROBLEMS_URL)


class RequestManager:
    def __init__(self, answer_request_function, delay=REQUEST_DELAY, max_size=REQUEST_QUEUE_MAX_SIZE):
        self.request_queue = Queue(maxsize=max_size)
        self.answer_queue = Queue()
        self.delay = delay
        self.answer_request_function = answer_request_function

        self.request_thread = Thread(target=self.request_loop)

    def ask(self, args, timeout=REQUEST_TIMEOUT):
        self.request_queue.put(args)
        return self.answer_queue.get(timeout=timeout)

    def request_loop(self):
        while True:
            args = self.request_queue.get()
            self.answer_queue.put(self.answer_request_function(args))
            time.sleep(self.delay)
