#Them phan tu vao dau danh sach

class Node:
    def __init__(self, data):
        self.data = data
        self.next = next

class CricularLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if not self.head:
            new_node.next = new_node
            self.head = new_node
            return
        last_node = self.head
        while last_node.next != self.head:
            last_node = last_node.next
            return
        last_node = self.head
        while last_node.next != self.head:
            last_node = last_node.next
        new_node.next= self.head
        self.head = new_node
        last_node.next = new_node

# Them phan tu voa vi tri cuoi cung cua danh dach

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            new_node.next = new_node
            self.head= new_node
            return
        last_node = self.head
        while last_node.next != self.head:
            last_node = last_node.next
        last_node.next = new_node
        new_node.next = self.head

# Xoa phan tu ow dau danh sach

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def delete_at_beginning(self):
        if not self.head:
            return
        if self.head.next == self.head:
            self.head = None
            return
        last_node = self.head
        while last_node.next != self.head:
            last_node = last_node.next
        last_node.next = self.head.next 
        self.head = self.head.next


#  Xoa phan tu o cuoi danh sach
class CircularLinkedList:
    def __init__(self):
        self.head = None

    def delete_at_end(self):
        if not self.head:
            return
        if self.head.next == self.head:
            self.head = None
            return
        second_last = self.head
        while second_last.next.next != self.head:
            second_last== second_last.next
        second_last.next = self.head

# Xoa phan tu o vi tri bat ky 
class CircularLinkedList:
    def __init__(self):
        self.head = None

    def delete_ar_position(self, position):
        if not  self.head:
            return
        if position == 0:
            last_node = self.head
            while last_node.next != self.head:
                last_node = last_node.next
            self.head= self.head.next
            last_node.next = self.head
            return
        current_node = self.head
        for i in range(position-1):
            if current_node.next == self.head:
                return
            current_node = current_node.next
        if current_node.next == self.head:
            return
        current_node.next = current_node.next.next

# Chèn phanà tử vào
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CricularLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head= new_node
            new_node.next=self.head
        else:
            current_node = self.head
            while current_node.next != self.head:
                current_node= current_node.next
            
        current_node.next=new_node
        new_node.next=self.head