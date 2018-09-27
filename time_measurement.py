import sorting
import time
import random
import copy
from data import Data


class Researh:
    def __init__(self,
                 function_names=("selection", "shell", "shell_hib",
                                 "shell_sedgewick", "shell_pratt", "quick",
                                 "heap", "insertion", "merge", "bin_insert",
                                 "sorted"),
                 arrays_lengths=(2000, 3000, 4000, 5000),
                 data_types=("random",)):
        self.functions_data = {}
        self.function_names = function_names
        self.array_lens = arrays_lengths
        self.data_types = data_types
        self.functions = self.get_functions(function_names)

    def get_functions(self, names):
        all_functions = {"selection": sorting.selection_sort,
                         "shell": sorting.shell_sort,
                         "shell_hib": sorting.shell_sort_hib,
                         "shell_sedgewick": sorting.shell_sort_sedgewick,
                         "shell_pratt": sorting.shell_sort_pratt,
                         "quick": sorting.quick_sort,
                         "heap": sorting.heap_sort,
                         "insertion": sorting.insertion_sort,
                         "merge": sorting.merge_sort,
                         "bin_insert": sorting.bin_insert_sort,
                         "sorted": sorted}
        result = []
        for name in names:
            result.append(all_functions[name])
        return tuple(result)

    def get_array(self, type, length):
        if type == "random":
            return self.get_random_array(length)
        elif type == "best":
            return self.get_best_array(length)
        elif type == "worst":
            return self.get_worst_array(length)

    def check(self):
        for function in self.functions:
            dict_by_type = {}
            for data_type in self.data_types:
                dict_by_length = {}
                for length in self.array_lens:
                    array = self.get_array(data_type, length)
                    times = []
                    standard_deviation = 1
                    average_time = 1
                    while(standard_deviation/average_time >= 0.05):
                        array = copy.deepcopy(array)
                        time_work = self.notify_time(function, array)
                        if time_work == 0:
                            continue
                        times.append(time_work)
                        if len(times) > 1:
                            standard_deviation = 0
                            average_time = sum(times)/len(times)
                            for element in times:
                                standard_deviation += \
                                    (element-average_time)**2
                            standard_deviation = \
                                (standard_deviation/(len(times)-1))**0.5
                    dict_by_length[length] = Data(average_time,
                                                  sorting.PERMISSION_COUNT,
                                                  sorting.C0MPARISON_COUNT)
                dict_by_type[data_type] = dict_by_length
            self.functions_data[function.__name__] = dict_by_type

    def get_random_array(self, count):
        array = []
        for i in range(count):
            array.append(random.random())
        return array

    def get_best_array(self, count):
        return [x for x in range(count)]

    def get_worst_array(self, count):
        return [x for x in range(count, -1, -1)]

    def notify_time(self, func, array):
        start_time = time.time()
        func(array)
        return time.time() - start_time
