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
    sl = len(array)

    def swap(pi, ci):
        if array[pi] < array[ci]:
            array[pi], array[ci] = array[ci], array[pi]

    def sift(pi, unsorted):
        i_gt = lambda a, b: a if array[a] > array[b] else b
        while pi * 2 + 2 < unsorted:
            gtci = i_gt(pi * 2 + 1, pi * 2 + 2)
            swap(pi, gtci)
            pi = gtci

    # heapify
    for i in range((sl // 2) - 1, -1, -1):
        sift(i, sl)
    # sort
    for i in range(sl - 1, 0, -1):
        swap(i, 0)
        sift(0, i)
    return array


def merge_sort(array):
    def merge(left, right):
        lst = []
        while left and right:
            if left[0] < right[0]:
                lst.append(left.pop(0))
            else:
                lst.append(right.pop(0))
        if left:
            lst.extend(left)
        if right:
            lst.extend(right)
        return lst

    length = len(array)
    if length >= 2:
        mid = int(length / 2)
        array = merge(merge_sort(array[:mid]), merge_sort(array[mid:]))
    return array
