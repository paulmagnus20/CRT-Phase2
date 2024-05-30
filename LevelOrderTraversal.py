class Tree:
    def __init__(self,data):
        
        self.data=data
        self.right=None
        self.left=None
        
def printLevelOrderTraversal(root):
    if root == None:
        return
    Q=[root]
    result=[]
    while len(Q)>0:
        n=len(Q)
        subResult=[]
        for i in range(n):
            #deleting
            currNode=Q.pop(0)
            #append
            subResult.append(currNode.data)
            #insert left child
            if currNode.left !=None:
                Q.append(currNode.left)
            #insert right child
            if currNode.right != None:
                Q.append(currNode.right)
        result.append(subResult)
    print(result)
        
obj1=Tree(-15)
obj2=Tree(10)
obj3=Tree(7)
obj4=Tree(115)
obj5=Tree(102)
obj6=Tree(15)
obj7=Tree(18)
obj8=Tree(3)
obj9=Tree(71)
obj10=Tree(80)

#obj1.data=obj1
obj1.left=obj2
obj1.right=obj3
obj2.left=obj4
obj2.right=obj5
obj3.left=obj6
obj3.right=obj7
obj5.left=obj8
obj7.left=obj9
obj7.right=obj10

printLevelOrderTraversal(obj1)
