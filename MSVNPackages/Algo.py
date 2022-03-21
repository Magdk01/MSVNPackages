"""Queue and Stack data structure built with linked lists  """
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

'''' LnkedList class represents the linked list '''

class LinkedList_Queue():
    def __init__(self):
        self.head = None
        self.tail = None

    ''' Check if the list (queue) is empty so returns True (self.head is None) 
    or not so returns False (self.head is not None) '''

    def is_empty(self):
        return not self.head

    '''Add a new node to the end of the linked list (queue)'''

    def enqueue(self, key):
        new_node = Node(key)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    ''' Remove the first node of the linked list (queue).
    If the linked list (queue) is empty returns a warning message '''

    def dequeue(self):
        if self.is_empty():
            return "Warning: The queue is empty"
        deleted_element = self.head.value
        self.head = self.head.next
        return deleted_element

    ''' Return the first node of the linked list. 
    If the linked list (queue) is empty returns a warning message'''

    def peek(self):
        if self.is_empty():
            return "Warning: The queue is empty"
        return self.head.value

class LinkedList_Stack():
    def __init__(self):
        self.head = None
        self.tail = None

    ''' Check if the list (queue) is empty so returns True (self.head is None) 
    or not so returns False (self.head is not None) '''

    def is_empty(self):
        return not self.head

    '''Add a new node to the end of the linked list (queue)'''

    def push(self, key):
        new_node = Node(key)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    ''' Remove the first node of the linked list (queue).
    If the linked list (queue) is empty returns a warning message '''

    def pop(self):
        if self.is_empty():
            return "Warning: The stack is empty"
        deleted_element = self.head.value
        self.head = self.head.next
        return deleted_element

    ''' Return the first node of the linked list. 
    If the linked list (queue) is empty returns a warning message'''

    def peek(self):
        if self.is_empty():
            return "Warning: The stack is empty"
        return self.head.value
myque = LinkedList_Queue()
mystack = LinkedList_Stack()
