class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next=self.head
        self.head= new_node

# Them phan tu vao cuoi danh sach
class LinedList:
    def __init__(self):
        self.head = None
    
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head= new_node
            return
        last_node = self.head
        while last_node.next:
            last_node= last_node.next
        last_node.next= new_node

# Xoa phan tu dau danh sach
class LinkedList:
    def __init__(self): 
        self.head = None

    def delete_at_beginning(self):
        if not self.head:
            return
        self.head= self.head.next

# Xoa phan tu o cuoi danh sanh
class LinkedLisit:
    def __init__(self):
        self.head = None

    def delete_at_end(self):
        if not self.head:
            return
        if not self.head.next:
            self.head = None
            return
        second_last = self.head
        while second_last.next.next:
            second_last = second_last.next
        second_last.next = None

# Xoa phan tu o vi tri bất kỳ 
class LikedList:
    def __init__(self):
        self.head = None

    def delete_at_position(self, position):
        if not self.head:
            return
        if position == 0:
            self.head = self.head.next
            return
        current_node = self.head
        for i in range(position-1):
            if not current_node.next:
                return
            current_node = current_node.next
        if not current_node.next:
            return
        current_node.next = current_node.next.next 