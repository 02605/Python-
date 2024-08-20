class Node(object):
    def __init__(self, value=None, prev=None, next=None):
        self.value, self.prev, self.next = value, prev, next


class CircularDoubleLinkedList(object):
    def __init__(self, max_size=None):
        self.max_size = max_size
        node = Node()
        node.prev = node
        node.next = node
        self.root = node
        self.length = 0

    def __len__(self):
        return self.length

    def iter_node(self):
        if self.root.next is self.root:
            return
        node = self.root.next
        while node is not self.root.prev:
            yield node
            node = node.next
        yield node

    def __iter__(self):
        for node in self.iter_node():
            yield node.value

    def get_head_node(self):
        return self.root.next

    def get_tail_node(self):
        return self.root.prev

    def append(self, value):
        if self.max_size is not None and len(self) == self.max_size:
            raise Exception("full")
        node = Node(value)
        tail_node = self.get_tail_node()

        tail_node.next = node
        node.prev = tail_node

        node.next = self.root
        self.root.prev = node

        self.length += 1

    def append_left(self, value):
        if self.max_size is not None and len(self) == self.max_size:
            raise Exception("full")

        node = Node(value)

        # 只有根节点
        if self.root.next is self.root:
            node.next = self.root
            self.root.prev = node
        else:
            head_node = self.get_head_node()

            node.next = head_node
            head_node.prev = node

        self.root.next = node
        node.prev = self.root

        self.length += 1

    def remove(self, node):
        if node is self.root:
            return
        node.prev.next = node.next
        node.next.prev = node.prev

        self.length -= 1
        return node

    def iter_reverse(self):
        if self.root.next is self.root:
            return
        tail_node = self.root.prev
        while tail_node.prev is not self.root:
            yield tail_node
            tail_node = tail_node.prev
        yield tail_node

    def insert(self, value, new_value):
        if self.max_size is not None and self.max_size == len(self):
            raise Exception("full")
        current_node = self.root.next
        node = Node(new_value)

        while current_node is not self.root:
            if current_node.value == value:
                current_node.prev.next = node
                node.prev = current_node.prev
                node.next = current_node
                current_node.prev = node
                self.length += 1
                return
            else:
                current_node = current_node.next

        if current_node is self.root:
            raise Exception(f"not find {value}")


def test_double_linked_list():
    double_linked_list = CircularDoubleLinkedList()
    assert len(double_linked_list) == 0

    double_linked_list.append(1)
    double_linked_list.append(2)
    double_linked_list.append(3)
    double_linked_list.append(4)
    assert [each_one.value for each_one in double_linked_list.iter_node()] == [1, 2, 3, 4]

    head_node = double_linked_list.get_head_node()
    double_linked_list.remove(head_node)
    assert [each_one.value for each_one in double_linked_list.iter_node()] == [2, 3, 4]

    double_linked_list.append(5)
    assert list(double_linked_list) == [2, 3, 4, 5]

    double_linked_list.append_left(1)
    assert list(double_linked_list) == [1, 2, 3, 4, 5]

    assert [each_one.value for each_one in double_linked_list.iter_reverse()] == [5, 4, 3, 2, 1]

    double_linked_list.insert(1, 0)
    assert list(double_linked_list) == [0, 1, 2, 3, 4, 5]

    double_linked_list.insert(5, 4)
    assert list(double_linked_list) == [0, 1, 2, 3, 4, 4, 5]
    print(list(double_linked_list))

    double_linked_list.insert(6, 5)


if __name__ == '__main__':
    test_double_linked_list()