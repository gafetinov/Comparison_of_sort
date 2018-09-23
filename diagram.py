import matplotlib.pyplot as plt
import numpy
import math


class Diagram:
    def __init__(self, data):
        self.data = data

    def draw(self):
        if len(self.data) == 1:
            pass
        elif len(self.data) > 1:
            for function in self.data:
                for data_type in self.data[function]:
                    plt.plot(sorted(self.get_times(list(self.data[function][data_type].values()))),
                             sorted(list(self.data[function][data_type].keys())),
                             label=function)
        plt.xlabel('Time')
        plt.ylabel('Count')
        plt.legend()
        plt.show()

    def get_times(self, data_by_count):
        res = []
        for e in data_by_count:
            res.append(e.time)
        return res