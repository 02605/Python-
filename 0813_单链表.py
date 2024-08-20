import ctypes

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

    def reverse(self):
        curr_node = self.root.next
        self.tail_node = curr_node
        prev_node = None

        while curr_node:
            next_node = curr_node.next
            curr_node.next = prev_node

            if next_node is None:
                self.root.next = curr_node
                # print(id(curr_node))

            prev_node = curr_node
            curr_node = next_node
            # print(f"next_node:{id(next_node)}")
            # print(f"curr_node:{id(curr_node)}")

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


if __name__ == '__main__':
    my_list = LinkedList()
    my_list.append(1)
    my_list.append(2)
    my_list.append(3)
    my_list.append(4)
    print(list(my_list))
    print([id(each_node) for each_node in my_list])

    my_list.reverse()
    print(list(my_list))
    print([id(each_node) for each_node in my_list])

    my_list.reverse_2()
    print(list(my_list))
    print([id(each_node) for each_node in my_list])

    my_list.reverse_3()
    print(list(my_list))
    print([id(each_node) for each_node in my_list])






