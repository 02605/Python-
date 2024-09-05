class Array(object):

    def __init__(self, size=20, init=None):
        self._size = size
        self._items = [init] * size

    def __getitem__(self, index):
        return self._items[index]

    def __setitem__(self, index, value):
        self._items[index] = value

    def __len__(self):
        return self._size

    def clear(self, value=None):
        for i in range(len(self._items)):
            self._items[i] = value

    def __iter__(self):
        for item in self._items:
            yield item


class Solt(object):
    def __init__(self, key, value):
        self.key, self.value = key, value


class HashTable(object):

    UNUSED = None
    EMPTY = Solt(None, None)

    def __init__(self):
        self._table = Array(size=8, init=HashTable.UNUSED)
        self.length = 0

    @property
    def _load_factory(self):
        return self.length / float(len(self._table))

    def __len__(self):
        return self.length

    def _hash(self, key):
        return abs(hash(key)) % len(self._table)

    def _find_key(self, key):
        index = self._hash(key)
        _len = len(self._table)

        while self._table[index] is not HashTable.UNUSED:
            if self._table[index] is HashTable.EMPTY:
                index = (index * 5 + 1) % _len
                continue
            elif self._table[index].key == key:
                return index
            else:
                index = (index * 5 + 1) % _len
        return None

    def _slot_can_insert(self, index):
        return self._table[index] in (HashTable.EMPTY, HashTable.UNUSED)

    def _find_slot_for_insert(self, key):
        index = self._hash(key)
        _len = len(self._table)
        while not self._slot_can_insert(index):
            index = (index*5 + 1) % _len
        return index

    def __contains__(self, key):
        index = self._find_key(key)
        return index is not None

    def __iter__(self):
        for slot in self._table:
            if slot not in (HashTable.EMPTY, HashTable.UNUSED):
                yield slot.key

    def _rehash(self):
        old_table = self._table
        new_size = len(self._table) * 2
        self._table = Array(new_size, HashTable.UNUSED)

        self.length = 0

        for slot in old_table:
            if slot not in (HashTable.EMPTY, HashTable.UNUSED):
                index = self._find_slot_for_insert(slot.key)
                self._table[index] = slot
                self.length += 1

    def add(self, key, value):
        if key in self:
            index = self._find_key(key)
            self._table[index] = Solt(key, value)
            return False
        else:
            index = self._find_slot_for_insert(key)
            self._table[index] = Solt(key, value)
            self.length += 1
            if self._load_factory >= 0.8:
                self._rehash()
            return True

    def get(self, key, default=None):
        index = self._find_key(key)
        if index is None:
            return default
        else:
            return self._table[index].value

    def remove(self, key):
        index = self._find_key(key)
        if index is None:
            raise KeyError()
        value = self._table[index].value
        self._table[index] = HashTable.EMPTY
        self.length -= 1
        return value


class SetADT(HashTable):

    def add(self, key):
        return super(SetADT, self).add(key, True)

    def __and__(self, other_set):
        # 交集
        new_set = SetADT()
        for element in self:
            if element in other_set:
                new_set.add(element)
        return new_set

    def __sub__(self, other_set):
        # 差集
        new_set = SetADT()
        for element in self:
            if element not in other_set:
                new_set.add(element)
        return new_set

    def __or__(self, other_set):
        # 并集
        new_set = SetADT()
        for element_a in self:
            new_set.add(element_a)
        for element_b in other_set:
            new_set.add(element_b)
        return new_set


def test_set_adt():
    sa = SetADT()
    sa.add(1)
    sa.add(2)
    sa.add(3)
    assert 1 in sa    # 测试  __contains__ 方法，实现了 add 和 __contains__，集合最基本的功能就实现啦

    sb = SetADT()
    sb.add(3)
    sb.add(4)
    sb.add(5)
    assert sorted(list(sa & sb)) == [3]
    assert sorted(list(sa - sb)) == [1, 2]
    assert sorted(list(sa | sb)) == [1, 2, 3, 4, 5]


if __name__ == '__main__':
    test_set_adt()















