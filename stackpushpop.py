def push(stack,ele):
    stack.append(ele)
    print(ele,"inserted successfully")

def pop(stack):
    if len(stack)== 0:
        print("Stack is empty")
        return
    print(stack[-1],"deleted successfully")
    stack.pop()
    
stack=[]
push(stack,10)
push(stack,20)
push(stack,30)
push(stack,40)
print("The stack is", stack)

pop(stack)
pop(stack)
pop(stack)
pop(stack)
pop(stack)
print("The Stack is", stack)
