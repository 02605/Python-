
class Array(object):
    def __init__(self, max_size, init=None):
        self._size = max_size
        self._items = [init] * max_size

    def __getitem__(self, index):
        return self._items[index]

    def __setitem__(self, index, value):
        self._items[index] = value

    def __len__(self):
        return self._size

    def __iter__(self):
        for each_one in self._items:
            yield each_one

    def clear(self, value=None):
        self._items = [value] * self._size


class Slot(object):
    """
    hash表的槽，用于存放key，value
    """
    def __init__(self, key, value):
        self.key, self.value = key, value


class HashTable(object):

    # 从没有被使用过
    UNUSED = None
    # 被使用过，但是已经被删除了
    EMPTY = Slot(None, None)

    def __init__(self):
        self._table = Array(8, HashTable.UNUSED)
        self.length = 0

    def __len__(self):
        return self.length

    # 自定义hash函数
    def _hash(self, key):
        return abs(hash(key)) % len(self._table)

    @property
    def _load_factory(self):
        # 返回装载因子的值
        return self.length / float(len(self._table))

    def _find_key(self, key):
        """
        解释一个 slot 为 UNUSED 和 EMPTY 的区别
        因为使用的是二次探查的方式，假如有两个元素 A，B 冲突了，首先A hash 得到是 slot 下标5，A 放到了第5个槽，之后插入 B 因为冲突了，所以继续根据二次探查方式放到了 slot8。
        然后删除 A，槽 5 被置为 EMPTY。然后我去查找 B，第一次 hash 得到的是 槽5，但是这个时候我还是需要第二次计算 hash 才能找到 B。
        但是如果槽是 UNUSED 我就不用继续找了，我认为 B 就是不存在的元素。这个就是 UNUSED 和 EMPTY 的区别。
        """
        ori_index = index = self._hash(key)
        _len = len(self._table)
        # 循环条件，槽不是空槽
        while self._table[index] is not HashTable.UNUSED:
            # 如果被占用过，继续hash下一个index
            if self._table[index] is HashTable.EMPTY:
                index = (index * 5 + 1) % _len
                if index == ori_index:
                    break
                continue
            # 找到key
            if self._table[index].key == key:
                return index
            else:
                index = (index * 5 + 1) % _len
                if index == ori_index:
                    break

        return None

    def _slot_can_insert(self, index):
        return self._table[index] in (HashTable.UNUSED, HashTable.EMPTY)

    def _find_slot_for_insert(self, key):
        index = self._hash(key)
        _len = len(self._table)

        while not self._slot_can_insert(index):
            index = (index * 5 + 1) % _len
        return index

    def __contains__(self, key):
        index = self._find_key(key)
        return index is not None

    def __iter__(self):
        for each_slot in self._table:
            if each_slot not in (HashTable.UNUSED, HashTable.EMPTY):
                yield each_slot.key

    def add(self, key, value):
        if key in self:
            index = self._find_key(key)
            self._table[index].value = value
            return False
        else:
            index = self._find_slot_for_insert(key)
            self._table[index] = Slot(key, value)
            self.length += 1
            if self._load_factory >= 0.8:
                self._rehash()
            return True

    # rehashing扩容
    def _rehash(self):
        old_table = self._table
        new_size = len(self._table) * 2
        self._table = Array(new_size, HashTable.UNUSED)
        self.length = 0

        for slot in old_table:
            if slot not in (HashTable.UNUSED, HashTable.EMPTY):
                index = self._find_slot_for_insert(slot.key)
                self._table[index] = slot
                self.length += 1

    def get(self, key, default=None):
        index = self._find_key(key)
        if index is not None:
            return self._table[index].value

        return default

    def remove(self, key):
        index = self._find_key(key)
        if index is not None:
            value = self._table[index].value
            self._table[index] = HashTable.EMPTY
            self.length -= 1
            return value
        else:
            raise KeyError()


def test_my_hash_table():
    my_hash_table = HashTable()
    assert len(my_hash_table) == 0

    my_hash_table.add("a", 0)
    my_hash_table.add("b", 1)
    my_hash_table.add("c", 2)
    assert len(my_hash_table) == 3

    assert my_hash_table.get("a") == 0
    assert my_hash_table.get("c") == 2
    assert my_hash_table.get("csss") is None

    assert my_hash_table.remove("a") == 0
    assert "c" in my_hash_table

    assert sorted(list(my_hash_table)) == ["b", "c"]

    # 测试rehashing
    for i in range(20):
        my_hash_table.add(i, i)

    for i in range(20):
        assert my_hash_table.get(i) == i


















