#  Them phan tu vao dau danh sach

class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None
        self.prev = None

class DoublyLinkedlist:
    def __init__(self, data):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        self.head= new_node

#  Them phan tu vao cuoi danh sach
class DoubyLinkedlist:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node= last_node.next
        last_node.next = new_node
        new_node.prev = last_node


#  Xoa phan tu dau tien cua danh sach

class doublyLinkedList:
    def __init__(self):
        self.head = None

    def delete_at_beginning(self):
        if not self.head:
            return
        self.head = self.head.next
        if self.head:
            self.head.prev = None

    
#  Xoa phan tu cuoi danh sach
 
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def delete_at_end(self):
        if not self.head:
            return
        if not self.head.next:
            self.head =None
            return
        last_node = self.head
        while last_node.next:
            last_node= last_node.next
        last_node.prev.next = None
        last_node.prev = None


# Xoa pohan tu opw vi tri bat ky

class DoublyLInkedList:
    def __init__(self):
        self.head= None

    def delete_at_position(self, position):
        if not self.head:
            return
        if position==0:
            self.head= self.head.next
            if self.head:
                self.head.prev = None
            return
        current_node = self.head
        for i in range(position-1):
            if not current_node.next:
                return
            current_node= current_node.next
        if not current_node.next:
            return
        current_node.next= current_node.next.next
        if current_node.next:
            current_node.next.prev = current_node

#  Chen phan tu vao 

class Node:
    def __init__(self, data):
        self.data= data
        self.next = None
        self.prev = None

class DoublyLinkelist:
    def __init__(self):
        self.head = None

    def insert(self, data, position):
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            if self.head:
                self.head.prev=new_node
            self.head=new_node
            return
        current_node = self.head
        for i in range(position-1):
            if not current_node:
                return
            current_node= current_node.next
        if not current_node:
            return
        new_node.next= current_node.next
        new_node.prev - current_node
        if current_node.next:
            current_node.next.prev = new_node
        current_node.next=new_node