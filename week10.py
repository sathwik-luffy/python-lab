class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
class DoublyLinkedList:
    def __init__(self):
        self.head = None
    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is not None:
            self.head.prev = new_node
            new_node.next = self.head
        self.head = new_node
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp
    def insert_at_position(self, position, data):
        new_node = Node(data)
        if position == 0:
            self.insert_at_beginning(data)
            return
        temp = self.head
        for _ in range(position - 1):
            if temp is None:
                print("Position out of range")
                return
            temp = temp.next
        if temp is None:
            print("Position out of range")
            return
        new_node.next = temp.next
        new_node.prev = temp
        if temp.next:
            temp.next.prev = new_node
        temp.next = new_node
    def delete_from_beginning(self):
        if self.head is None:
            print("List is empty")
            return
        if self.head.next is None:
            self.head = None
            return
        self.head = self.head.next
        self.head.prev = None
    def delete_from_end(self):
        if self.head is None:
            print("List is empty")
            return
        if self.head.next is None:
            self.head = None
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.prev.next = None
    def delete_at_position(self, position):
        if self.head is None:
            print("List is empty")
            return
        temp = self.head
        if position == 0:
            self.delete_from_beginning()
            return
        for _ in range(position):
            if temp is None:
                print("Position out of range")
                return
            temp = temp.next
        if temp is None:
            print("Position out of range")
            return
        if temp.next:
            temp.next.prev = temp.prev
        if temp.prev:
            temp.prev.next = temp.next
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" <--> ")
            temp = temp.next
        print("None")
dll = DoublyLinkedList()
dll.insert_at_beginning(10)
print("After insertion at starting:")
dll.display()
dll.insert_at_end(30)
dll.insert_at_end(40)
print("After insertion at ending:")
dll.display()
dll.insert_at_position(2, 25)
print("After insertion at specific position:")
dll.display()
dll.delete_from_beginning()
print("After deleting from beginning:")
dll.display()
dll.delete_from_end()
print("After deleting from end:")
dll.display()
dll.delete_at_position(1)
print("After deleting from specific position:")
dll.display()        
