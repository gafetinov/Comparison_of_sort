import math

C0MPARISON_COUNT = 0
PERMISSION_COUNT = 0


def selection_sort(array, key=lambda x: x):
    global C0MPARISON_COUNT
    global PERMISSION_COUNT
    C0MPARISON_COUNT = 0
    PERMISSION_COUNT = 0
    start = 0
    end = len(array)-1
    for i in range(start, end+1):
        index = i
        min = array[i]
        for j in range(i, end+1):
            if key(array[j]) < key(min):
                min = array[j]
                index = j
            C0MPARISON_COUNT += 1
        array[i], array[index] = array[index], array[i]
        PERMISSION_COUNT += 1


def shell_sort(array, key=lambda x: x):
    global C0MPARISON_COUNT
    global PERMISSION_COUNT
    C0MPARISON_COUNT = 0
    PERMISSION_COUNT = 0
    start = 0
    end = len(array)-1
    step = (end-start+1)//2
    while step >= 1:
        for i in range(start, end-step+1):
            j = i
            while j >= start and key(array[j]) > key(array[j+step]):
                array[j], array[j+step] = array[j+step], array[j]
                C0MPARISON_COUNT += 1
                PERMISSION_COUNT += 1
                j -= 1
            C0MPARISON_COUNT += 1
        step //= 2


def shell_sort_hib(array, key=lambda x: x):
    global C0MPARISON_COUNT
    global PERMISSION_COUNT
    C0MPARISON_COUNT = 0
    PERMISSION_COUNT = 0
    start = 0
    end = len(array)
    if end == 0:
        return
    step = 2**math.floor(math.log2(end-start))-1
    while step >= 1:
        for i in range(start, end-step):
            j = i
            while j >= start and key(array[j]) > key(array[j + step]):
                array[j], array[j + step] = array[j + step], array[j]
                C0MPARISON_COUNT += 1
                PERMISSION_COUNT += 1
                j -= 1
            C0MPARISON_COUNT += 1
        step = (step+1)//2-1


def shell_sort_sedgewick(array, key=lambda x: x):
    global C0MPARISON_COUNT
    global PERMISSION_COUNT
    C0MPARISON_COUNT = 0
    PERMISSION_COUNT = 0
    start = 0
    end = len(array)
    if end < 2:
        return
    steps = []
    k = 1
    current_step = 1
    while 3*current_step <= end:
        steps.append(current_step)
        if k % 2 == 1:
            current_step = 8*2**k - 6*2**((k+1)//2) + 1
        elif k % 2 == 0:
            current_step = 9*2**k - 9*2**(k//2) + 1
        k += 1
    for index in range(len(steps)-1, -1, -1):
        for i in range(start, end-steps[index]):
            j = i
            while j >= start and key(array[j]) > key(array[j + steps[index]]):
                array[j], array[j + steps[index]] = \
                    array[j + steps[index]], array[j]
                PERMISSION_COUNT += 1
                C0MPARISON_COUNT += 1
                j -= 1
            C0MPARISON_COUNT += 1


def shell_sort_pratt(array, key=lambda x: x):
    def get_pratt_seq(max):
        i = 0
        seq = []
        while 3**i <= max:
            current_el = 3**i
            while current_el <= max:
                seq.append(current_el)
                current_el *= 2
            i += 1
        return sorted(seq)

    global C0MPARISON_COUNT
    global PERMISSION_COUNT
    C0MPARISON_COUNT = 0
    PERMISSION_COUNT = 0
    start = 0
    end = len(array)
    steps = get_pratt_seq(end / 2)
    for index in range(len(steps)-1, -1, -1):
        for i in range(start, end-steps[index]):
            j = i
            while j >= start and key(array[j]) > key(array[j + steps[index]]):
                array[j], array[j + steps[index]] = \
                    array[j + steps[index]], array[j]
                PERMISSION_COUNT += 1
                C0MPARISON_COUNT += 1
                j -= 1
            C0MPARISON_COUNT += 1


def quick_sort(array, key=lambda x: x):
    def quick(start, end):
        global C0MPARISON_COUNT
        global PERMISSION_COUNT
        if end - start < 1:
            return
        left = start
        right = end
        pivot = array[(left + right) // 2]
        while left <= right:
            while key(array[left]) < key(pivot):
                left += 1
                C0MPARISON_COUNT += 1
            while key(array[right]) > key(pivot):
                right -= 1
                C0MPARISON_COUNT += 1
            if left <= right:
                array[left], array[right] = array[right], array[left]
                C0MPARISON_COUNT += 2
                PERMISSION_COUNT += 1
                left += 1
                right -= 1
        if right > start:
            quick(start, right)
        if end > left:
            quick(left, end)

    global C0MPARISON_COUNT
    global PERMISSION_COUNT
    C0MPARISON_COUNT = 0
    PERMISSION_COUNT = 0
    quick(0, len(array)-1)


def heap_sort(array, key=lambda x: x):
    def get_larger(a, b):
        if key(array[a] > key(array[b])):
            return a
        else:
            return b

    def heapify(index, unsorted):
        global C0MPARISON_COUNT
        global PERMISSION_COUNT
        while index * 2 + 2 < unsorted:
            largest = get_larger(index * 2 + 1, index * 2 + 2)
            C0MPARISON_COUNT += 1
            if key(array[index]) < key(array[largest]):
                array[index], array[largest] = array[largest], array[index]
                PERMISSION_COUNT += 1
            index = largest
            C0MPARISON_COUNT += 1

    global C0MPARISON_COUNT
    global PERMISSION_COUNT
    C0MPARISON_COUNT = 0
    PERMISSION_COUNT = 0
    n = len(array)
    # heapify
    for i in range((n//2)-1, -1, -1):
        heapify(i, n)
    # sort
    for i in range(n - 1, 0, -1):
        if key(array[i]) < key(array[0]):
            array[i], array[0] = array[0], array[i]
            PERMISSION_COUNT += 1
        C0MPARISON_COUNT += 1
        heapify(0, i)


def merge_sort(array, key=lambda x: x):
    def merge(array, start, mid, end):
        global PERMISSION_COUNT
        global C0MPARISON_COUNT
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
            C0MPARISON_COUNT += 1
            PERMISSION_COUNT += 1

    def do_sorting(start, end):
        end += 1
        if end - start > 1:
            mid = (start + end) // 2
            do_sorting(start, mid-1)
            do_sorting(mid, end-1)
            merge(array, start, mid, end)

    global C0MPARISON_COUNT
    global PERMISSION_COUNT
    C0MPARISON_COUNT = 0
    PERMISSION_COUNT = 0
    do_sorting(0, len(array)-1)


def insertion_sort(array, key=lambda x: x):
    global C0MPARISON_COUNT
    global PERMISSION_COUNT
    C0MPARISON_COUNT = 0
    PERMISSION_COUNT = 0
    for i in range(1, len(array)):
        elem = array[i]
        j = i - 1
        while (j > -1) and key(elem) < key(array[j]):
            array[j + 1] = array[j]
            C0MPARISON_COUNT += 1
            PERMISSION_COUNT += 1
            j = j - 1
        C0MPARISON_COUNT += 1
        array[j + 1] = elem
        PERMISSION_COUNT += 1


def bin_insert_sort(array, key=lambda x: x):
    global C0MPARISON_COUNT
    global PERMISSION_COUNT
    C0MPARISON_COUNT = 0
    PERMISSION_COUNT = 0
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
                C0MPARISON_COUNT += 1
            for j in range(i-1, left-1, -1):
                array[j+1] = array[j]
                PERMISSION_COUNT += 1
            array[left] = elem
            PERMISSION_COUNT += 1
        C0MPARISON_COUNT += 1
# All sorting is inplace
