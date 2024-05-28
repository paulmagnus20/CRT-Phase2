class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None 
 
def printLinkedList(head):
    currentNode = head 
    while currentNode != None:
        print(currentNode.data, end = " --> ")
        currentNode = currentNode.next
    print()
    
def insertAtHead(head, ele):
    temp = Node(ele)
    temp.next=head
    return temp


def deleteTailNode(head):
    if head == None or head.next == None:
        return None
    
    previous = None
    currentNode = head
    
    while currentNode.next != None:
        previous=currentNode
        currentNode=currentNode.next
        
    previous.next = None
    return head

nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
head = None  
for ele in nums:
    head = insertAtHead(head, ele)
deleteTailNode(head)
printLinkedList(head)
