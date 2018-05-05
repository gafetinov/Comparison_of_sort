import sorting
import time
import random


def main():
    functions = (sorting.merge_sort, sorting.selection_sort,
                 sorting.shell_sort, sorting.quick_sort,
                 sorting.heap_sort)
    count = 100
    file = open('result.txt', 'w')
    while count < 200:
        random_array = get_random_array(count)
        for function in functions:
            times = []
            standard_deviation = 1
            average_time = 1
            while(standard_deviation/average_time > 0.05):
                time_work = notify_time(function, random_array)
                times.append(time_work)
                if len(times) > 1:
                    standard_deviation = 0
                    average_time = sum(times)/len(times)
                    for element in times:
                        standard_deviation += (element-average_time)**2
                    standard_deviation = (standard_deviation/(len(times) - 1))**0.5
            delta =
            file.write('{} {} {}\n'.format(function.__name__,
                                           count,
                                           average_time))
        count *= 5
    file.close()


def get_random_array(count):
    array = []
    for i in range(count):
        array.append(random.random())
    return array


def notify_time(func, array):
    start_time = time.time()
    func(array)
    return time.time() - start_time


if __name__ == '__main__':
    main()