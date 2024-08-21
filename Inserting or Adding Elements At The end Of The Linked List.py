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
    def add_begin(self,data):
        new_node=Node(data)
        new_node.ref=self.head
        self.head=new_node
        
    def add_end(self,data):
        new_node=Node (data)
        if self.head is None:
            self.head=new_node
        else:
            n=self.head
            while n.ref is not None:
                n=n.ref
            n.ref=new_node

    def add_after(self,data,x):
        n=self.head
        while n is not None:
            if x==n.data:
                break
            n=n.ref
        if n is None:
            print ("node is not present in linkkedlist")
        else:
            new_node = Node(data)
            new_node.ref=n.ref
            n.ref=new_node
        def add_before (self,data,x):
            if self.head is None:
                print("LINKEDLIST is empty")
                return
            if self.head.data==x:
                new_node = Node (data)
                new_node.ref = self.head
                self,head = new_node
                return
            n= self.head
            while n.ref is not None:
                if n.ref.data==x:
                 break
                n=n.ref
            if n.ref is None:
                print(" node is not found")
            else:
                new_node=Node(data)
                new_node.ref = n.ref
                n.ref=new_node
                

LL1 = LinkedList()  
#LL1.add_begin(20)
#LL1.add_begin(780)
LL1.add_end(234)
LL1.add_begin(450)
LL1.add_before(45,234)
#LL1.add_begin(23)
LL1.print_LL()  
