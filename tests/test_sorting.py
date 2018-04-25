import sorting


class TestSelectionSort:
    def test_simple(self):
        array = [3, 324, 2, 1, 4, 0]
        sorted_array = array
        sorted_array.sort()
        assert sorting.selection_sort(array) == sorted_array
        assert sorting.shell_sort(array) == sorted_array
        assert sorting.quick_sort(array) == sorted_array
