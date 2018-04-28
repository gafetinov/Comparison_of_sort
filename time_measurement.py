import array_generation
import sorting
import time

random_array = array_generation.Generator(100).random_array()
start_time = time.time()
sorting.merge_sort(random_array)
stop_time = time.time()
print("merge_sort: {}".format(stop_time-start_time))
start_time = time.time()
sorting.heap_sort(random_array)
stop_time = time.time()
print("heap_sort: {}".format(stop_time-start_time))
start_time = time.time()
sorting.quick_sort(random_array)
stop_time = time.time()
print("quick_sort: {}".format(stop_time-start_time))
start_time = time.time()
sorting.shell_sort(random_array)
stop_time = time.time()
print("shell_sort: {}".format(stop_time-start_time))
start_time = time.time()
sorting.selection_sort(random_array)
stop_time = time.time()
print("selection sort: {}".format(stop_time-start_time))
