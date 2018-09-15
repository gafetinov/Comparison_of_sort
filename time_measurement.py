import sorting
import time
import random
import copy
import data


class Researh:
    def __init__(self,
                 function_names=("selection", "shell", "shell_hib",
                                 "shell_sedgewick", "shell_pratt", "quick",
                                 "heap", "insertion", "merge", "bin_insert",
                                 "sorted"),
                 arrays_lengths=(1000,),
                 data_types=("random",)):
        self.data = []
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

    def check(self):
        for length in self.array_lens:
            for data_type in self.data_types:
                random_array = self.get_array(data_type, length)
                for function in self.functions:
                    times = []
                    standard_deviation = 1
                    average_time = 1
                    while(standard_deviation/average_time >= 0.05):
                        array = copy.deepcopy(random_array)
                        time_work = self.notify_time(function, array)
                        if time_work == 0:
                            continue
                        times.append(time_work)
                        if len(times) > 1:
                            standard_deviation = 0
                            average_time = sum(times)/len(times)
                            for element in times:
                                standard_deviation += (element-average_time)**2
                            standard_deviation = (standard_deviation/(len(times)-1))**0.5
                    self.data.append(data.Data(function=function.__name__,
                                               count=length,
                                               time=average_time,
                                               comparisons_count=sorting.
                                               C0MPARISON_COUNT,
                                               permissions_count=sorting.
                                               PERMISSION_COUNT,
                                               type=data_type))

    def get_random_array(self, count):
        array = []
        for i in range(count):
            array.append(random.random())
        return array

    def notify_time(self, func, array):
        start_time = time.time()
        func(array)
        return time.time() - start_time

    def get_dates(self):
        return self.data
