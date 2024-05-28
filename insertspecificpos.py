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
    temp.next = head 
    return temp

def insertAtSpecificPosition(head, position, ele):
    if position == 0:
        return insertAtHead(head, ele)
 
    temp = Node(ele)
    index = 0 
    currentNode = head 
    while index != position - 1:
        currentNode = currentNode.next 
        index += 1 
 
    nextNode = currentNode.next 
    temp.next = nextNode 
    currentNode.next = temp 
    return head
 
nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
head = None  
for ele in nums:
    head = insertAtHead(head, ele)
head =insertAtSpecificPosition(head, 3, 101)
printLinkedList(head)