
class Bag(object):

    def __init__(self, maxsize = 10):

        self.maxsize = maxsize
        self._items = list()

    def add(self, item):

        if len(self) > self.maxsize:
            raise Exception("full")
        self._items.append(item)

    def remove(self, item):

        self._items.remove(item)

    def __len__(self):

        return len(self._items)

    def __iter__(self):

        for item in self._items:
            yield item

def test_adt():

    bag = Bag()
    bag.add(1)
    bag.add(2)
    bag.add(3)

    assert len(bag) == 3

    bag.remove(3)
    assert len(bag) == 2

    for each_one in bag:
        print(each_one)

if __name__ == '__main__':
    test_adt()
