import logging
import os

import requests


class APIController(object):
    def __init__(self):
        self._api_key = os.getenv('AI_DEVS_API_KEY')
        self._api_path = os.getenv('AI_DEVS_URL')

    def url(self, path):
        return f'{self._api_path}/{path}'

    def post_answer(self, exercise, answer):
        response = requests.post(
            self.url('verify'),
            json={
                'task': exercise.TASK_NAME,
                'apikey': self._api_key,
                'answer': answer,
            },
        )
        logging.info(response.json())


def check_task(exercise):
    answer = exercise.resolve()
    logging.info(answer)

def run_task(exercise):
    controller = APIController()
    answer = exercise.resolve()
    logging.info(answer)
    controller.post_answer(exercise, answer)
