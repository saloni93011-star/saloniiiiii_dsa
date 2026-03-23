# Stack create karna using list
stack = []

# Push operation (add element)
stack.append("Saloni")
stack.append("Rahul")
stack.append("Amit")

print("Stack after push:", stack)

# Pop operation (last element remove hota hai)
removed = stack.pop()
print("Removed element:", removed)

# Top element (peek)
print("Top element:", stack[-1])

# Check if stack is empty
if len(stack) == 0:
    print("Stack is empty")
else:
    print("Stack is not empty")

print("Final stack:", stack)