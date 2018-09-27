import sorting
import random
SORTINGS = (sorting.selection_sort, sorting.shell_sort,
            sorting.shell_sort_hib, sorting.shell_sort_sedgewick,
            sorting.shell_sort_pratt, sorting.quick_sort, sorting.heap_sort,
            sorting.insertion_sort, sorting.merge_sort,
            sorting.bin_insert_sort)


class TestSortings:
    def check_sortings(self, array):
        sorted_array = list(array)
        sorted_array.sort()
        for sorting in SORTINGS:
            arr = list(array)
            sorting(arr)
            assert arr == sorted_array

    def get_random_array(self):
        array = []
        for i in range(100):
            array.append(random.random())
        return array

    def test_bin(self):
        array = [12, 214, 32, 4, 223, 2, 3, 2, 3, 23, 3, 364, 34]
        sorted_array = list(array)
        sorted_array.sort()
        lst = list(array)
        sorting.shell_sort(lst)
        assert lst == sorted_array

    def test_empty(self):
        array = []
        self.check_sortings(array)

    def test_singleton(self):
        array = [1]
        self.check_sortings(array)

    def test_simple(self):
        array = [3, 324, 2, 1, 4, 0, -43]
        self.check_sortings(array)

    def test_random_array(self):
        array = self.get_random_array()
        self.check_sortings(array)

    def test_sorted(self):
        array = self.get_random_array()
        array.sort()
        self.check_sortings(array)

    def test_reversed(self):
        array = self.get_random_array()
        array.sort(reverse=True)
        self.check_sortings(array)

    def test_same(self):
        array = [1]*100
        self.check_sortings(array)

    def test_strings(self):
        array = []
        for i in range(100):
            string = ''
            for j in range(random.randint(0, 10000)):
                string.join(chr(random.randint(33, 125)))
            array.append(string)
        self.check_sortings(array)

    def test_worst_way(self):
        self.check_sortings([x for x in range(100, -1, -1)])

    def test_best_way(self):
        self.check_sortings([x for x in range(100)])
