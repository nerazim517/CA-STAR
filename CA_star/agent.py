import queue
from random import randint


class Agent:
    def __init__(self):
        self.id = randint(5, 255)
        self.start = int()
        self.destination = int()
        # self.current_location = None
        self.planned_path = []

    def set_task(self, start, destination):
        self.start = start
        self.destination = destination

    def get_planned_path(self):
        return self.planned_path
