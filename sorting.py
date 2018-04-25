import math


def selection_sort(array):
    for i in range(len(array)):
        index = i
        min = array[i]
        for j in range(i, len(array)):
            if array[j] < min:
                min = array[j]
                index = j
        array[i], array[index] = array[index], array[i]
    return array


def shell_sort(array):
    step = len(array) // 2
    while step > 1:
        i = 0
        while i + step < len(array) - 1:
            if array[i] > array[i+step]:
                array[i], array[i+step] = array[i+step], array[i]
            i += 1
        step //= 2
    return array


def quick_sort(array):
    if len(array) <= 1:
        return array
    pivot = array[len(array)//2]
    l_arr = []
    r_arr = []
    medium_arr = []
    for elem in array:
        if elem < pivot:
            l_arr.append(elem)
        elif elem > pivot:
            r_arr.append(elem)
        else:
            medium_arr.append(elem)
    return quick_sort(l_arr) + medium_arr + quick_sort(r_arr)


def heap_sort(array):
    pass


def merge_sort(array):
    pass