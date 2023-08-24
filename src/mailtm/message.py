import json
import time
import traceback
from threading import Thread

import requests.exceptions


class Listen:
    listen = False
    message_ids = []

    def message_list(self):
        try:
            url = "https://api.mail.tm/messages"
            headers = {'Authorization': 'Bearer ' + self.token}
            response = self.session.get(url, headers=headers)

            if response.status_code in [429]:
                print("Getting message lists returned 429.")
                return []
            else:
                response.raise_for_status()

            data = response.json()
            return [
                msg for i, msg in enumerate(data['hydra:member'])
                if data['hydra:member'][i]['id'] not in self.message_ids
            ]
        except requests.exceptions.HTTPError as e:
            traceback.print_exception(e)
            time.sleep(15)
            return self.message_list(self)


    def message(self, idx):
        try:
            url = "https://api.mail.tm/messages/" + idx
            headers = { 'Authorization': 'Bearer ' + self.token }
            response = self.session.get(url, headers=headers)
            response.raise_for_status()
            return response.json()

        except requests.exceptions.HTTPError as e:
            traceback.print_exception(e)
            time.sleep(15)
            return self.message(self, idx)


    def run(self):
        while self.listen:
            for message in self.message_list():
                self.message_ids.append(message['id'])
                message = self.message(message['id'])
                self.listener(message)

            time.sleep(self.interval)

    def start(self, listener, interval=3):
        if self.listen:
            self.stop()

        self.listener = listener
        self.interval = interval
        self.listen = True

        # Start listening thread
        self.thread = Thread(target=self.run)
        self.thread.start()
    
    def stop(self):
        self.listen = False
        self.thread.join()