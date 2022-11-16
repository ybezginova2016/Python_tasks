# Linked List

# LinkedList используется если необходимо производить много операций
# вставки/удаления элементов в середине списка и мало операций
# доступа к элементу по индексу. Структура связного списка в
# таких операциях будет эффективнее массива, на котором основана
# реализация ArrayList, потому что при вставке элементов в середину
# ArrayList физически сдвигаются все последующие элементы.

# BENEFIT: easy to insert or remove

class Node:
    def __init__ (self, data=None, next_node=None):
        self.data = data
        self.next = next_node

    def __str__ (self):
        return str(self.data)

class LinkedList:
    def __init__ (self):
        self.length = 0
        self.head = None
    def print_list(self):
        node = self.head
        while node is not None:
            print(node, end=' ')
            node = node.next
        print('')
    def add_at_head(self, node):
        node.next = self.head
        self.head = node
        self.length += 1

my_list = LinkedList()
my_list.add_at_head(Node(3))
my_list.add_at_head(Node(9))
my_list.print_list()