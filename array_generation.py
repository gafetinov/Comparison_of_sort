import random


class Generator:
    def __init__(self, size):
        self.size = size

    def random_array(self):
        random_array = []
        for i in range(self.size):
            random_array.append(random.random())
        return random_array

    def best_selection_and_sorting_array(self):
        array = self.random_array()
        array.sort()
        return array

    def worse_selection_and_sorting_array(self):
        return self.best_selection_and_sorting_array().reverse()