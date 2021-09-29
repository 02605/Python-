# 线性结构: 内存连续、下标访问

class Array(object):

    def __init__(self, size = 23):

        self._size = size
        self._items = [None] * size

    def __getitem__(self, item):
        return self._items[item]

    def __setitem__(self, key, value):
        self._items[key] = value

    def clear(self, value = None):

        for i in range(len(self._items)):
            self._items[i] = value

    def __iter__(self):

        for item in self._items:
            yield item

    def __len__(self):

        return len(self._items)

def test_array_adt():

    size = 10
    a = Array(size)
    a[0] = 1
    assert a[0] == 1

    a.clear()
    assert a[0] is None

    for i in a:

        print(i)

if __name__ == '__main__':
    test_array_adt()
