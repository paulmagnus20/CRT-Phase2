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

def insertAtTail(head, ele):
    temp = Node(ele)
    if head == None:
        return temp
 
    tail = head 
    while tail.next != None:
        tail = tail.next 
    tail.next = temp 
    return head

def deletenotatSpecificPosition(head,position):
    index=0
    currentNode = head
    while index != position - 1:
        index += 1
        currentNode = currentNode.next
        
    nodetobeDeleted = currentNode.next
    nextNode = nodetobeDeleted.next
    
    nodetobeDeleted.next= None
    currentNode.next= None 
    currentNode.next= nextNode

nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
head = None  
for ele in nums:
    head = insertAtTail(head, ele)
deletenotatSpecificPosition(head, 3)
printLinkedList(head)
