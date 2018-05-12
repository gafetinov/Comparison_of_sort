import sorting
import random


class TestSelectionSort:
    def test_simple(self):
        array = [3, 324, 2, 1, 4, 0]
        sorted_array = array
        sorted_array.sort()
        assert sorting.quadratic_sort(array) == sorted_array
        assert sorting.shell_sort(array) == sorted_array
        assert sorting.quick_sort(array) == sorted_array
        # assert sorting.heap_sort(array) == sorted_array
        assert sorting.merge_sort(array) == sorted_array

    def test_random_array(self):
        array = []
        for i in range(100):
            array.append(random.randint(-10000, 10000))
        sorted_array = array
        sorted_array.sort()
        assert sorting.quadratic_sort(array) == sorted_array
        assert sorting.shell_sort(array) == sorted_array
        assert sorting.quick_sort(array) == sorted_array
        # assert sorting.heap_sort(array) == sorted_array
        assert sorting.merge_sort(array) == sorted_array
