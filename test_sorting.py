import sorting
import random
SORTINGS = (sorting.selection_sort, sorting.quick_sort, sorting.shell_sort,
            sorting.heap_sort, sorting.merge_sort, sorting.insertion_sort)


class TestSelectionSort:
    def test_quick(self):
        array = [3, 324, 2, 1, 4, 0, -34]
        sorted_array = list(array)
        sorted_array.sort(key=lambda x: abs(x))
        lst = list(array)
        sorting.heap_sort(lst, 0, len(lst)-1, key=lambda x: abs(x))
        assert lst == sorted_array

    def test_bin(self):
        array = [3, 1, 4, 0, 28]
        sorted_array = list(array)
        sorted_array.sort()
        lst = list(array)
        sorting.bin_insert_sort(lst, 0, len(lst)-1)
        assert lst == sorted_array

    def test_simple(self):
        array = [3, 324, 2, 1, 4, 0]
        sorted_array = list(array)
        sorted_array.sort()
        for sorting in SORTINGS:
            lst = list(array)
            sorting(lst, 0, len(lst)-1)
            assert lst == sorted_array

    def test_random_array(self):
        array = []
        for i in range(100):
            array.append(random.random())
        sorted_array = list(array)
        sorted_array.sort()
        for sorting in SORTINGS:
            lst = list(array)
            sorting(lst, 0, len(lst)-1)
            assert lst == sorted_array
