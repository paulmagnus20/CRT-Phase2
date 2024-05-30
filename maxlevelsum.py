class Tree():
    def __init__(self,data):
        
        self.data=data
        self.right=None
        self.left=None
        
def maxLevelSum(root):
    if root == None:
        return 0
    Q = [root]
    resultLevel = 0 
    resultSum = -100000000
    currLevel = 1
    while len(Q) > 0:
        n = len(Q)
        currSum = 0
        for i in range(n):
            # step-1 (Deleting)
            currNode = Q.pop(0)

            # step-2 (Appending to subResult)
            currSum += currNode.data

            # step-3 (Enquing the left child)
            if currNode.left != None:
                Q.append(currNode.left)

            # step-4 (Enquing the right child)
            if currNode.right != None:
                Q.append(currNode.right)

        if currSum > resultSum:
            resultSum = currSum 
            resultLevel = currLevel 
        currLevel += 1
    print(resultLevel)


    
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
maxLevelSum(obj1)