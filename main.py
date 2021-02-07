import math

class SearchingAlgo:
    def __init__(self, _list):
        self._list = _list
    
    def jump_search(self, num):
        n = len(self._list)
        m = int(math.sqrt(n))

        itr = m
        while self._list[itr] < num:
            itr+=m
        else:
            start_linear = itr-m
            for i in range(start_linear, n):
                if self._list[i] == num:
                    print('{} founded at index {}'.format(self._list[i], i))


if __name__ == '__main__':
    salgo = SearchingAlgo([0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610])
    
    salgo.jump_search(21)
