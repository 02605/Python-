class Node(object):
    def __init__(self, value=None, prev=None, next=None):
        self.value, self.prev, self.next = value, prev, next


class CircleDoubleLinkedList(object):
    def __init__(self, max_size=None):
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


class Deque(CircleDoubleLinkedList):

    def pop(self):
        if len(self) == 0:
            raise Exception("Empty")

        tail_node = self.get_tail()
        tail_value = tail_node.value

        self.remove(tail_node)
        return tail_value

    def pop_left(self):
        if len(self) == 0:
            raise Exception("Empty")

        head_node = self.get_head()
        head_value = head_node.value

        self.remove(head_node)
        return head_value


class Stack(object):
    def __init__(self):
        self.deque = Deque()

    def pop(self):
        return self.deque.pop()

    def push(self, value):
        self.deque.append_right(value)

    def __len__(self):
        return len(self.deque)


def test_stack():
    my_stack = Stack()
    assert len(my_stack) == 0

    my_stack.push(0)
    my_stack.push(1)
    my_stack.push(2)
    assert len(my_stack) == 3

    assert my_stack.pop() == 2
    assert my_stack.pop() == 1
    assert my_stack.pop() == 0

    assert len(my_stack) == 0

    import pytest
    with pytest.raises(Exception) as exec_info:
        my_stack.pop()
    assert "Empty" in str(exec_info)