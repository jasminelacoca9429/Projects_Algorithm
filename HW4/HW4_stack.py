from HW4.HW4_linked_list import DoublyLinkedList


class Stack:

    def __init__(self):
        self.items = DoublyLinkedList()
        self.minimum = None

    def push(self, item):
        if self.minimum is None:
            self.minimum = item
        elif self.minimum > item:
            self.items.append(self.minimum)
            self.minimum = item
        self.items.append(item)

    def pop(self):
        print('debug')
        result_node = self.items.tail
        prev_node = self.items.tail.prev
        prev_node.next = None
        self.items.tail = prev_node
        if result_node.data == self.minimum:
            self.minimum = prev_node.data
            prev_node = self.items.tail.prev
            prev_node.next = None
            self.items.tail = prev_node
        return f'The removed element is {result_node.data}'

    def min(self):
        return f'The minimum element of this stack is {self.minimum}'

    def __str__(self):
        return str(self.items)
