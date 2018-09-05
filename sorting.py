import math


def selection_sort(array, key=lambda x: x):
    start = 0
    end = len(array)-1
    for i in range(start, end+1):
        index = i
        min = array[i]
        for j in range(i, end+1):
            if key(array[j]) < key(min):
                min = array[j]
                index = j
        array[i], array[index] = array[index], array[i]


def shell_sort(array, key=lambda x: x):
    start = 0
    end = len(array)-1
    step = (end-start+1)//2
    while step >= 1:
        for i in range(start, end-step+1):
            j = i
            while j >= start and key(array[j]) > key(array[j+step]):
                array[j], array[j+step] = array[j+step], array[j]
                j -= 1
        step //= 2


def shell_sort_hib(array, key=lambda x: x):
    pass


def shell_sort_sedgwick(array, key=lambda x: x):
    pass


def shell_sort_pratt(array, key=lambda x: x):
    pass


def quick_sort(array, key=lambda x: x):
    def quick(start, end):
        if end - start < 1:
            return
        left = start
        right = end
        pivot = array[(left + right) // 2]
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
            quick(start, right)
        if end > left:
            quick(left, end)

    quick(0, len(array)-1)


def heap_sort(array, key=lambda x: x):
    def get_larger(a, b):
        if key(array[a] > key(array[b])):
            return a
        else:
            return b

    def heapify(index, unsorted):
        while index * 2 + 2 < unsorted:
            largest = get_larger(index * 2 + 1, index * 2 + 2)
            if key(array[index]) < key(array[largest]):
                array[index], array[largest] = array[largest], array[index]
            index = largest

    n = len(array)
    # heapify
    for i in range((n//2)-1, -1, -1):
        heapify(i, n)
    # sort
    for i in range(n - 1, 0, -1):
        if key(array[i]) < key(array[0]):
            array[i], array[0] = array[0], array[i]
        heapify(0, i)


def merge_sort(array, key=lambda x: x):
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

    def do_sorting(start, end):
        end += 1
        if end - start > 1:
            mid = (start + end) // 2
            do_sorting(start, mid-1)
            do_sorting(mid, end-1)
            merge(array, start, mid, end)

    do_sorting(0, len(array)-1)


def insertion_sort(array, key=lambda x: x):
    for i in range(1, len(array)):
        elem = array[i]
        j = i - 1
        while (j > -1) and key(elem) < key(array[j]):
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = elem


def bin_insert_sort(array, key=lambda x: x):
    end = len(array)
    for i in range(1, end):
        if key(array[i-1]) > key(array[i]):
            elem = array[i]
            left = 0
            right = i-1
            while left <= right:
                mid = (left+right)//2
                if key(array[mid]) < key(elem):
                    left = mid+1
                else:
                    right = mid-1
            for j in range(i-1, left-1, -1):
                array[j+1] = array[j]
            array[left] = elem
# All sorting is inplace
