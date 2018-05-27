import math


def standard_key(x):
    return x


def selection_sort(array, start, end, key=standard_key):
    for i in range(start, end+1):
        index = i
        min = array[i]
        for j in range(i, end+1):
            if key(array[j]) < key(min):
                min = array[j]
                index = j
        array[i], array[index] = array[index], array[i]


def shell_sort(array, start, end, key=standard_key, offsets=None):
    step = (end-start+1)//2
    while step >= 1:
        for i in range(start, end-step+1):
            j = i
            while j >= start and key(array[j]) > key(array[j+step]):
                array[j], array[j+step] = array[j+step], array[j]
                j -= 1
        step //= 2


def hibbard_seq(n):
    current_step = 1
    steps = [current_step]
    i = 2
    while current_step <= n:
        current_step = 2**i - 1
        steps.append(current_step)
        i += 1
    return steps


def quick_sort(array, start, end, key=standard_key):
    if end-start < 1:
        return
    left = start
    right = end
    pivot = array[(left+right)//2]
    while left <= right:
        while key(array[left]) < key(pivot):
            left += 1
        while key(array[right]) > key(pivot):
            right -= 1
        if left <= right:
            array[left], array[right] = array[right], array[left]
            left += 1
            right -= 1
    if right > start:
        quick_sort(array, start, right, key)
    if end > left:
        quick_sort(array, left, end, key)


def heap_sort(array, start, end, key=standard_key):
    sl = len(array)

    def swap(pi, ci):
        if key(array[pi]) < key(array[ci]):
            array[pi], array[ci] = array[ci], array[pi]

    def sift(pi, unsorted):
        i_gt = lambda a, b: a if key(array[a]) > key(array[b]) else b
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


def merge_sort(array, start, end, key=standard_key):
    def merge(array, start, mid, end):
        left = array[start:mid]
        right = array[mid:end]
        i = 0
        j = 0
        k = start
        for l in range(k, end):
            if j >= len(right) or (i < len(left) and key(left[i]) < key(right[j])):
                array[l] = left[i]
                i = i + 1
            else:
                array[l] = right[j]
                j = j + 1

    end += 1
    if end - start > 1:
        mid = (start + end) // 2
        merge_sort(array, start, mid-1, key)
        merge_sort(array, mid, end-1, key)
        merge(array, start, mid, end)


def insertion_sort(array, start, end, key=standard_key):
    for i in range(1, len(array)):
        elem = array[i]
        j = i - 1
        while (j > -1) and key(elem) < key(array[j]):
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = elem


def bin_insert_sort(array, start, end, key=standard_key):
    for i in range(1, end+1):
        if array[i-1] > array[i]:
            x = array[i]
            left = 0
            right = i-1
            while left <= right:
                mid = (left+right)//2
                if array[mid] < x:
                    left = mid+1
                else:
                    right = mid-1
            for j in range(i-1, left-1, -1):
                array[j+1] = array[j]
            array[left] = x
# All sorting is inplace
