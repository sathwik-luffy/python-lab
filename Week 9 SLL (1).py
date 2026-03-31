class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
    def add_begin(self,data):
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
    def add_end(self,data):
        if self.head is None:
            self.head = new_node
        else:
            
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
    def add_specific(self,data,pos):
        if self.head is None:
            self.head = new_node
        
        else:
            current=self.head
            for i in range(1,pos):
                p=current
                current=current.next
            p.next=new_node
            new_node.next=current   
    def display(self):
        current = self.head
        while current:
            print(current.data, end = ' ')
            current = current.next
    def delete_beg(self):
        current=self.head
        self.head=current.next
        del(current)
    def delete_end(self):
        current=self.head
        while current.next is not None:
            p=current
            current=current.next
        p.next=None
        del(current)
    def del_specific(self,pos):
        current=self.head
        for i in range(1,pos):
            p=current
            current=current.next
        
        p.next=current.next
        del(current)
LL1=LinkedList()
print("1.INSERT AT BEGINING")
print("2.INSERT AT ENDING")
print("3.INSERT AT SPECIFIC POSITION")
print("4.DISPLAY")
print("5.DELETE FROM BEGINING")
print("6.DELETE FROM ENDING")
print("7.DELETE FROM SPECIFIC POSITION")
print("8.EXIT")

while True:
    op=int(input("enter your choice"))
    match(op):
        case 1:
            data = int(input('Enter the  element:'))
            new_node = Node(data)
            LL1.add_begin(new_node)
        case 2:
            data = int(input('Enter the element:'))
            new_node = Node(data)
            LL1.add_end(new_node)
        case 3:
            pos=int(input('Enter pos:'))
            data = int(input('Enter the element:'))
            new_node = Node(data)
            LL1.add_specific(new_node,pos)
            
        case 4:
            print('The list: ', end = '')
            LL1.display()
            print()
        case 5:
            LL1.delete_beg()
        case 6:
            LL1.delete_end()
    
        case 7:
            pos=int(input("enter pos"))
            LL1.del_specific(pos)
        case 8:
            exit()