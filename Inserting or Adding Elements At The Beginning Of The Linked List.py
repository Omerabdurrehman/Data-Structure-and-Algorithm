class Node: 
    def __init__(self, data):
        self.data = data
        self.ref = None  

class LinkedList:  
    def __init__(self):
        self.head = None
    
    def print_LL(self):  
        if self.head is None: 
            print("Linked list is empty")
        else:
            n = self.head
            while n is not None:  
                print(n.data)
                n = n.ref
    
    def add_begin(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node
    
    def sub_begin(self, data):
        if self.head is None:
            print("Linked list is empty")
            return
        
        if self.head.data == data:
            self.head = self.head.ref
            return
        
        n = self.head
        while n.ref is not None:
            if n.ref.data == data:
                n.ref = n.ref.ref
                return
            n = n.ref
        
        print(f"{data} not found in the list")

LL1 = LinkedList()  
LL1.add_begin(20)
LL1.add_begin(32)
LL1.add_begin(234)
LL1.sub_begin(32)
LL1.print_LL()
