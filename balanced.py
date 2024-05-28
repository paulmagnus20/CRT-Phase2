def isBalanced(word):
    stack=[]
    for ele in word:
        if ele=="(":
            stack.append('(')
        else:
            if len(stack)==0:
                return False
            else:
                stack.pop()
    if len(stack)==0:
        return False
    return True
word='())())('
result=isBalanced(word)
print(result)