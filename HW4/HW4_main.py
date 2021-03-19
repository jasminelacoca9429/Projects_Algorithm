from HW4.HW4_stack import Stack
from HW4.HW4_linked_list import DoublyLinkedList
from HW4.HW4_BST import BST

# Q1
print('---------------------------Q1----------------------------')
it = Stack()
for i in range(8):
    it.push(i)
print('The instantiated stack:', it)
print(it.pop())
print(it.min())

# Q2
print('---------------------------Q2----------------------------')
# initialize doubly linked list
d_list = DoublyLinkedList()
print('The initiated linked list:', d_list.head)
# Prepend 5, 9, 11 to the list
d_list.prepend(5)
d_list.prepend(9)
d_list.prepend(11)
print(f'With prepended elements,\n'
      f'this doubly linked list looks like \n'
      f'{d_list},\n'
      f'head: {d_list.head}; tail: {d_list.tail}')

d_list.append(1)
d_list.append(3)
print(f'With appended elements,\n'
      f'this doubly linked list now looks like \n'
      f'{d_list},\n'
      f'head: {d_list.head}; tail: {d_list.tail}')

print(d_list.find(9))

d_list.remove(11)
print(f'After removing element 11,\n'
      f'this doubly linked list now looks like \n'
      f'{d_list},\n'
      f'head: {d_list.head}; tail: {d_list.tail}')

# Q3
print('---------------------------Q3----------------------------')
bst = BST()
# Respectively insert 5, 2, 0, 77, 8, 4, 7 into the tree
for x in [5, 2, 0, 77, 8, 4, 7]:
    bst.insert(x)

print('Reference of the min element:', bst.tree_minimum())
print('Reference of the max element:', bst.tree_maximum())
print('The successor of node x:', bst.successor(5).value)
