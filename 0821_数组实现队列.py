
class Array(object):
    def __init__(self, size=32):
        self._size = self
        self._items = [None] * size

    def __getitem__(self, index):
        return self._items[index]

    def __setitem__(self, index, value):
        self._items[index] = value

    def __len__(self):
        return self._size

    def clear(self):
        for i in range(len(self._items)):
            self._items[i] = None

    def __iter__(self):
        for item in self._items:
            yield item


class ArrayQueue(object):
    """
    head表示头指针
    tail表示尾指针
    头尾指针不停的+1，通过对队列最大长度取模计算真实的头尾指针下标
    """
    def __init__(self, max_size):
        self.max_size = max_size
        self.array = Array(max_size)
        self.head = 0
        self.tail = 0

    def __len__(self):
        return self.head - self.tail

    def push(self, value):
        if len(self) == self.max_size:
            raise Exception("Full")
        self.array[self.head % self.max_size] = value
        self.head += 1

    def pop(self):
        if len(self) == 0:
            raise Exception("Empty")
        # 通过取模计算出下标
        value = self.array[self.tail % self.max_size]
        self.tail += 1
        return value


def test_array_queue():
    my_queue = ArrayQueue(6)
    assert len(my_queue) == 0

    for i in range(6):
        my_queue.push(i)
    assert len(my_queue) == 6

    import pytest

    with pytest.raises(Exception) as exec_info:
        my_queue.push(6)
    assert "Full" in str(exec_info)

    assert my_queue.pop() == 0
    assert len(my_queue) == 5
    assert my_queue.pop() == 1
    assert my_queue.pop() == 2
    assert my_queue.pop() == 3
    assert my_queue.pop() == 4
    assert my_queue.pop() == 5
    assert len(my_queue) == 0

    with pytest.raises(Exception) as exec_info:
        my_queue.pop()
    assert "Empty" in str(exec_info)

