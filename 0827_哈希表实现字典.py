class Array(object):
    def __init__(self, max_size, init=None):
        self.size = max_size
        self._items = [init] * max_size

    def __getitem__(self, index):
        return self._items[index]

    def __setitem__(self, index, value):
        self._items[index] = value

    def __len__(self):
        return self.size

    def clear(self, default=None):
        for i in range(len(self)):
            self._items[i] = default

    def __iter__(self):
        for item in self._items:
            yield item


class Slot(object):
    def __init__(self, key, value):
        self.key, self.value = key, value


class HashTable(object):
    UNUSED = None
    EMPTY = Slot(None, None)

    def __init__(self):
        self._table = Array(8, HashTable.UNUSED)
        self.length = 0

    def __len__(self):
        return self.length

    def _hash(self, key):
        return abs(hash(key)) % len(self._table)

    @property
    def _slot_factory(self):
        return self.length / float(len(self._table))

    def _find_key(self, key):
        index = self._hash(key)
        _len = len(self._table)

        while self._table[index] is not HashTable.UNUSED:
            if self._table[index] is HashTable.EMPTY:
                index = (index*5 + 1) % _len
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

    def __iter__(self):
        for slot in self._table:
            if slot not in (HashTable.EMPTY, HashTable.UNUSED):
                yield slot.key

    def __contains__(self, key):
        index = self._find_key(key)
        return index is not None

    def _rehash(self):
        old_table = self._table
        self.length = 0
        new_size = len(self._table) * 2
        self._table = Array(new_size, HashTable.UNUSED)

        for slot in old_table:
            if slot not in (HashTable.EMPTY, HashTable.UNUSED):
                index = self._find_slot_for_insert(slot.key)
                self._table[index] = slot
                self.length += 1

    def add(self, key, value):
        if key in self:
            index = self._find_key(key)
            self._table[index] = value
            return False
        else:
            index = self._find_slot_for_insert(key)
            self._table[index] = Slot(key, value)
            self.length += 1
            if self._slot_factory >= 0.8:
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


class DictADT(HashTable):

    def __getitem__(self, key):
        if key not in self:
            raise KeyError()
        return self.get(key)

    def __setitem__(self, key, value):
        self.add(key, value)

    def _iter_slot(self):
        for slot in self._table:
            if slot not in (HashTable.EMPTY, HashTable.UNUSED):
                yield slot

    def items(self):
        for item in self._iter_slot():
            yield item.key, item.value

    def keys(self):
        for item in self._iter_slot():
            yield item.key

    def values(self):
        for item in self._iter_slot():
            yield item.value


def test_dict_adt():
    import random
    d = DictADT()

    d['a'] = 1
    assert d['a'] == 1
    d.remove('a')

    l = list(range(30))
    random.shuffle(l)
    for i in l:
        d.add(i, i)

    for i in range(30):
        assert d.get(i) == i

    assert sorted(list(d.keys())) == sorted(l)


test_dict_adt()





















