import requests
from queue import Queue
from threading import Thread


REQUEST_DELAY = 10.0


class RequestManager:
    def __init__(self):
        self.sub_request_manager = Queue()
        self.sub_request_thread = Thread(target=self.sub_request_loop)

    def sub_request_loop(self):
