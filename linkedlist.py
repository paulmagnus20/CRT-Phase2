class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None 
      
obj1 = Node(10)
obj2 = Node(20)
obj3 = Node(30)
obj4 = Node(40)
obj5 = Node(50) 

obj1.next = obj2 
obj2.next = obj3
obj3.next = obj4 
obj4.next = obj5 

currentNode = obj1 
while currentNode != None:
    print(currentNode.data, end = " --> ")
    currentNode = currentNode.next