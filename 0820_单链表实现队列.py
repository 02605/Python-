class Node(object):

    def __init__(self, value=None, next=None):
        self.value, self.next = value, next


class LinkedList(object):

    def __init__(self, max_size=None):
        self.max_size = max_size
        self.root = Node()
        self.length = 0
        self.tail_node = None

    def __len__(self):
        return self.length

    # 尾插
    def append(self, value):
        if self.max_size is not None and len(self) > self.max_size:
            raise Exception("Full")
        node = Node(value)
        tail_node = self.tail_node
        if tail_node is None:
            self.root.next = node
        else:
            tail_node.next = node
        self.tail_node = node
        self.length += 1

    # 头插
    def append_left(self, value):
        head_node = self.root.next
        node = Node(value)
        self.root.next = node
        node.next = head_node
        self.length += 1

    def iter_node(self):
        current_node = self.root.next
        while current_node is not self.tail_node:
            yield current_node
            current_node = current_node.next
        yield current_node

    def __iter__(self):
        for node in self.iter_node():
            yield node.value

    # 根据值删除节点
    def remove(self, value):
        """根据值删除链表中的某一元素，删除成功返回1，失败返回-1

        :param value:
        :return:
        """
        prev_node = self.root
        for curr_node in self.iter_node():
            if curr_node.value == value:
                if curr_node is self.tail_node:
                    self.tail_node = prev_node
                del curr_node
                self.length -= 1
                return 1
            else:
                prev_node = curr_node
        return -1

    def find(self, value):
        index = 0
        for curr_node in self.iter_node():
            if curr_node.value == value:
                return index
            index += 1
        return -1

    # 弹出最左边的元素
    def pop_left(self):
        head_node = self.root.next
        if head_node is None:
            raise Exception("empty list.")
        if head_node is self.tail_node:
            self.tail_node = None
        self.root.next = head_node.next
        value = head_node.value
        self.length -= 1
        del head_node
        return value

    def clear(self):
        for curr_node in self.iter_node():
            del curr_node
        self.tail_node = None
        self.root.next = None
        self.length = 0

    # 逆置
    def reverse(self):
        curr_node = self.root.next
        self.tail_node = curr_node
        prev_node = None

        while curr_node:
            next_node = curr_node.next
            curr_node.next = prev_node

            if next_node is None:
                self.root.next = curr_node

            prev_node = curr_node
            curr_node = next_node

    def reverse_2(self):
        head_node = self.root.next
        prev_node = head_node
        curr_node = head_node.next
        self.root.next = self.tail_node
        self.tail_node = head_node
        while curr_node is not None:
            prev_node.next = curr_node.next
            curr_node.next = head_node
            head_node = curr_node
            curr_node = prev_node.next

    def reverse_3(self):
        root_node = self.root
        head_node = root_node.next
        root_node.next = None
        self.tail_node = head_node
        while head_node is not None:
            next_node = head_node.next
            head_node.next = root_node.next
            root_node.next = head_node
            head_node = next_node


class Queue(object):
    def __init__(self, max_size=None):
        self.max_size = max_size
        self._iter_linked_list = LinkedList()

    def __len__(self):
        return len(self._iter_linked_list)

    def push(self, value):
        if self.max_size is not None and self.max_size == len(self):
            raise Exception("Full")
        self._iter_linked_list.append(value)

    def pop(self):
        if len(self) == 0:
            raise Exception("Empty")
        return self._iter_linked_list.pop_left()


def test_queue():

    my_queue = Queue()
    my_queue.push(0)
    my_queue.push(1)
    my_queue.push(2)
    my_queue.push(3)
    assert len(my_queue) == 4

    assert 0 == my_queue.pop()

    assert len(my_queue) == 3

    assert 1 == my_queue.pop()
    assert 2 == my_queue.pop()
    assert 3 == my_queue.pop()

    import pytest
    with pytest.raises(Exception) as exc_info:
        my_queue.pop()
    assert "Empty" in str(exc_info.value)