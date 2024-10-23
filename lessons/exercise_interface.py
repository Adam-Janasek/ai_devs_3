from abc import ABC, abstractmethod


class MandatoryField(object):
    def __init__(self, name):
        self.name = name
        self.private_name = f'_{name}'

    def __get__(self, instance, owner):
        value = getattr(instance, self.private_name, None)
        if value is None:
            raise AttributeError(f'{self.name} must be defined in the subclass')
        return value

    def __set__(self, instance, value):
        setattr(instance, self.private_name, value)


class ExerciseInterface(ABC):
    TASK_NAME = MandatoryField('TASK_NAME')
    TASK_URL = MandatoryField('TASK_URL')

    @abstractmethod
    def resolve(self, payload, **kwargs):
        raise NotImplementedError
