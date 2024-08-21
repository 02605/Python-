class Node(object):
    def __init__(self, value=None, prev=None, next=None):
        self.value, self.prev, self.next = value, prev, next


class CircleDoubleLinkedList(object):
    def __init__(self, max_size):
        self.max_size = max_size
        self.length = 0
        node = Node()
        node.prev = node
        node.next = node
        self.root = node

    def __len__(self):
        return self.length

    def iter_node(self):
        if self.root.next is self.root:
            return
        curr = self.root.next
        # 当前节点的下一个节点是root节点时此节点是尾节点
        while curr.next is not self.root:
            yield curr
            curr = curr.next
        yield curr

    def __iter__(self):
        for node in self.iter_node():
            yield node.value

    def get_head(self):
        return self.root.next

    def get_tail(self):
        return self.root.prev

    def append_right(self, value):
        if self.max_size is not None and self.max_size == len(self):
            raise Exception("Full")
        node = Node(value)
        tail_node = self.get_tail()

        tail_node.next = node
        node.prev = tail_node

        self.root.prev = node
        node.next = self.root

        self.length += 1

    def append_left(self, value):
        if self.max_size is not None and self.max_size == len(self):
            raise Exception("Full")
        node = Node(value)
        head_node = self.get_head()

        self.root.next = node
        node.prev = self.root

        # 只有根节点
        if head_node is self.root:
            node.next = self.root
            self.root.prev = node
        else:
            node.next = head_node
            head_node.prev = node

        self.length += 1

    def remove(self, node):
        if node is self.root:
            return None
        node.prev.next = node.next
        node.next.prev = node.prev

        self.length -= 1

        return node


class DeQueue(object):
    def __init__(self, max_size):
        self.max_size = max_size
        self.queue = CircleDoubleLinkedList(max_size)

    def __len__(self):
        return len(self.queue)

    def push_right(self, value):
        self.queue.append_right(value)

    def push_left(self, value):
        self.queue.append_left(value)

    def pop_left(self):
        head_node = self.queue.get_head()
        pop_node = self.queue.remove(head_node)
        return pop_node if pop_node is None else pop_node.value

    def pop_right(self):
        tail_node = self.queue.get_tail()
        pop_node = self.queue.remove(tail_node)
        return pop_node if pop_node is None else pop_node.value

    def __iter__(self):
        for node in self.queue:
            yield node


def test_de_queue():
    my_deque = DeQueue(6)

    assert len(my_deque) == 0

    my_deque.push_right(0)
    my_deque.push_right(1)
    my_deque.push_right(2)
    assert len(my_deque) == 3
    assert list(my_deque) == [0, 1, 2]

    my_deque.push_left(-1)
    my_deque.push_left(-2)
    assert len(my_deque) == 5
    assert list(my_deque) == [-2, -1, 0, 1, 2]

    assert my_deque.pop_left() == -2
    assert my_deque.pop_right() == 2
    assert len(my_deque) == 3
    assert list(my_deque) == [-1, 0, 1]
