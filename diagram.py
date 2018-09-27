import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import spline


class Diagram:
    def __init__(self, data):
        self.data = data

    def draw(self):
        if len(self.data) >= 1:
            for function in self.data:
                for data_type in self.data[function]:
                    x = np.array(
                        sorted(
                            self.get_times(
                                list(
                                    self.data[function]
                                    [data_type].values()))))
                    y = np.array(
                        sorted(list(self.data[function][data_type].keys())))
                    xnew = np.linspace(x.min(), x.max(), 300)
                    ynew = spline(x, y, xnew)
                    plt.plot(xnew, ynew, label=function)
        plt.xlabel('Time')
        plt.ylabel('Count')
        plt.legend()
        plt.show()

    def get_times(self, data_by_count):
        res = []
        for e in data_by_count:
            res.append(e.time)
        return res