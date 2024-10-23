import requests

from lessons.exercise_interface import ExerciseInterface

class Exercise(ExerciseInterface):
    TASK_NAME: str = 'POLIGON'
    TASK_URL: str = 'https://poligon.aidevs.pl/dane.txt'

    def resolve(self, **kwargs):
        response = requests.get(self.TASK_URL)
        return response.text.strip().split('\n')
