class Node:

    def __init__(self, data):
        self.next = None
        self.prev = None
        self.data = data

    def __str__(self):
        return str(self.data)


class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def prepend(self, data):
        """Insert new node before the head of the list """
        new_node = Node(data)
        new_node.next = self.head
        new_node.prev = None

        if self.head is not None:
            self.head.prev = new_node

        self.head = new_node
        # self.tail = new_node

        if not self.head.next:
            self.tail = self.head

    def append(self, data):
        """Insert new node after the tail of the list """
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            self.tail = new_node

        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def find(self, data):
        """Return a node with the given data,
        or None if it isn't found """
        node = self.head
        while node:
            if node.data == data:
                return node
            node = node.next
        return None

    def remove(self, data):
        """Remove the first node with the given data.
        Raise exception if data is not found """
        if not self.head:
            raise Exception('List is empty')

        if not self.find(data):
            raise Exception(f'Node with data {data} not found')

        # else:
        #     curr_node = data.next
        #     curr_node.prev = data.prev
        #     node = data.next
        #     curr_node.next = node.next

        node = self.find(data)

        if node.next is None:
            prev_node = node.prev
            prev_node.next = None
            self.tail = prev_node
            return

        if node.prev is None:
            next_node = node.next
            next_node.prev = None
            self.head = next_node
            return

        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node

    def __str__(self):
        values = []
        node = self.head
        while node:
            values.append(str(node.data))
            node = node.next
        values.append('None')
        return ' <--> '.join(values)





