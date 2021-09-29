
class Node(object):

    def __init__(self, value=None, next=None):
        self.value, self.next = value, next

class LinkedList(object):

    def __init__(self, maxsize=None):

        self.maxsize = maxsize
        self.root = Node()
        self.length = 0
        self.tail_node = None

    def __len__(self):
        return self.length

    # 尾插
    def append(self, value):

        if self.maxsize is not None and len(self) == self.maxsize:
            raise Exception("FULL From LinkedList")
        # 目标节点
        node = Node(value)
        # 尾节点
        tail_node = self.tail_node
        if tail_node is None:
            self.root.next = node
        else:
            tail_node.next = node
        self.tail_node = node
        self.length += 1

    # 头插
    def append_left(self, vale):

        if self.maxsize is not None and len(self) == self.maxsize:
            raise Exception("FULL From LinkedList")
        current_node = Node(vale)
        head_node = self.root.next
        current_node.next = head_node
        self.root.next = current_node
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

    def remove(self, value):

        pre_node = self.root
        for curr_node in self.iter_node():
            if curr_node.value == value:
                pre_node.next = curr_node.next
                if curr_node is self.tail_node:
                    self.tail_node = pre_node
                del curr_node
                self.length -= 1
                return 1
            else:
                pre_node = curr_node
        return -1

    def find(self, value):

        index = 0
        for node in self.iter_node():
            if node.value == value:
                return index
            index += 1
        return -1

    def pop_left(self):

        if self.root.next is None:
            raise Exception("Empty LinkedList")

        curr_node = self.root.next
        self.root.next = curr_node.next
        self.length -= 1
        # 这步可以不用，Python的销毁资源是None
        # if curr_node is self.tail_node:
        #     self.tail_node = None
        value = curr_node.value
        del curr_node
        return value

    def clear(self):

        for node in self.iter_node():
            del node
        self.root.next = None
        self.length = 0

def test_LinkedList():

    my_list = LinkedList(10)
    my_list.append(1)
    my_list.append(2)
    my_list.append(3)
    my_list.append(4)
    my_list.append(5)

    my_list.append_left(0)
    my_list.remove(5)
    print(my_list.find(4))
    print(my_list.pop_left())
    my_list.clear()
    assert my_list.length == 0
    # print(list(my_list))

if __name__ == '__main__':
    test_LinkedList()











