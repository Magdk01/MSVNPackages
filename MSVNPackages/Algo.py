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


class max_Heap():

    def __init__(self):
        self.heap = [None]
        self.len = 0

    def is_empty(self):
        return self.len == 0

    def insert(self, key):
        self.len += 1
        self.heap.append(key)
        self.bubble_up(self.len)

    def swap(self,i,j):
        temp = self.heap[i]
        self.heap[i] = self.heap[j]
        self.heap[j] = temp

    def bubble_up(self,i):
        if i < 2:
            return
        parent = i // 2
        if self.heap[i] > self.heap[parent]:
            self.swap(i,parent)
            self.bubble_up(parent)

    def bubble_down(self,i):
        if i * 2 > self.len: return

        child = 2 * i + 1 if 2 * i + 1 <= self.len and self.heap[2 * i + 1] > self.heap[2 * i] else 2 * i
        if self.heap[child] > self.heap[i]:
            self.swap(child, i)
            self.bubble_down(child)

        # child_left = i * 2
        # child_right = i * 2 + 1
        # if self.heap[i] < self.heap[child_left]:
        #     self.swap(i,child_left)
        #     self.bubble_up(child_left)
        # elif self.heap[i] < self.heap[child_right]:
        #     self.swap(i, child_right)
        #     self.bubble_down(child_right)
    def extract_max(self):
        if self.is_empty(): return
        maxi = self.heap[1]
        self.heap[1] = self.heap[self.len]
        self.len -= 1
        self.bubble_down(1)
        del(self.heap[-1])
        return maxi

    def __str__(self):
        return ' '.join([str(elem) for elem in self.heap[1:self.len+1]])


class min_Heap():

    def __init__(self):
        self.heap = [None]
        self.len = 0

    def is_empty(self):
        return self.len == 0

    def insert(self, key):
        self.len += 1
        self.heap.append(key)
        self.bubble_up(self.len)

    def swap(self,i,j):
        temp = self.heap[i]
        self.heap[i] = self.heap[j]
        self.heap[j] = temp

    def bubble_up(self,i):
        if i < 2:
            return
        parent = i // 2
        if self.heap[i] < self.heap[parent]:
            self.swap(i,parent)
            self.bubble_up(parent)

    def bubble_down(self,i):
        if i * 2 > self.len: return

        child = 2 * i + 1 if 2 * i + 1 <= self.len and self.heap[2 * i + 1] < self.heap[2 * i] else 2 * i
        if self.heap[child] < self.heap[i]:
            self.swap(child, i)
            self.bubble_down(child)

        # child_left = i * 2
        # child_right = i * 2 + 1
        # if self.heap[i] < self.heap[child_left]:
        #     self.swap(i,child_left)
        #     self.bubble_up(child_left)
        # elif self.heap[i] < self.heap[child_right]:
        #     self.swap(i, child_right)
        #     self.bubble_down(child_right)
    def extract_min(self):
        if self.is_empty(): return
        mini= self.heap[1]
        self.heap[1] = self.heap[self.len]
        self.len -= 1
        self.bubble_down(1)
        del(self.heap[-1])
        return mini

    def __str__(self):
        return ' '.join([str(elem) for elem in self.heap[1:self.len+1]])


class Unionfind():

    def __init__(self, length):
        self.id_list = [x for x in range(length)]
        self.size = [1]*length

    def find(self, i):
        while i != self.id_list[i]:
            i = self.id_list[i]
        return i

    def union(self,c1,c2):
        r1 = self.find(c1)
        r2 = self.find(c2)

        if self.size[r1] < self.size[r2]:
            r1, r2 = r2, r1
        self.id_list[r2] = r1
        self.size[r1] += self.size[r2]