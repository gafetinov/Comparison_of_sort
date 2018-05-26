import math


def selection_sort(array, start, end):
    for i in range(len(array)):
        index = i
        min = array[i]
        for j in range(i, len(array)):
            if array[j] < min:
                min = array[j]
                index = j
        array[i], array[index] = array[index], array[i]


def shell_sort(array, start, end):
    step = len(array) // 2
    while step > 1:
        i = 0
        while i + step < len(array) - 1:
            if array[i] > array[i+step]:
                array[i], array[i+step] = array[i+step], array[i]
            i += 1
        step //= 2


def quick_sort(array, start, end):
    left = start
    right = end
    pivot = array[(left+right)//2]
    while left <= right:
        while array[left] < pivot:
            left += 1
        while array[right] > pivot:
            right -= 1
        if left <= right:
            array[left], array[right] = array[right], array[left]
            left += 1
            right -= 1
    if right > start:
        quick_sort(array, start, right)
    if end > left:
        quick_sort(array, left, end)


def heap_sort(array, start, end):
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


def merge_sort(array, start, end):
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


def insertion_sort(array, start, end):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while (j > -1) and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = key


def bin_insert_sort(array, start, end):
    for i in range(len(array)):
        if array[i-1] > array[i]:
            x = array[i]
            left = 0
            right = i-1
            while left <= right:
                mid = (left+right)/2
                if array[mid] < x:
                    left = mid+1
                else:
                    right = mid-1
            for j in range(i-1, left-1, -1):
                array[j+1] = array[j]
                array[left] = x
# some sorting is inplace
