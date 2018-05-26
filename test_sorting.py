import sorting
import random
SORTINGS = (sorting.selection_sort, sorting.quick_sort,
            sorting.heap_sort, sorting.merge_sort, sorting.insertion_sort,
            sorting.bin_insert_sort)


class TestSelectionSort:
    def test_quick(self):
        array = [3, 324, 2, 1, 4, 0]
        sorted_array = list(array)
        sorted_array.sort()
        lst = list(array)
        sorting.quick_sort(lst, 0, len(lst)-1)
        assert lst == sorted_array

    def test_simple(self):
        array = [3, 324, 2, 1, 4, 0]
        sorted_array = list(array)
        sorted_array.sort()
        for sorting in SORTINGS:
            lst = list(array)
            sorting(lst)
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
