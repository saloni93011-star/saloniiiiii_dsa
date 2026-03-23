# Queue create karna
queue = []

# Enqueue operation (add element at end)
queue.append("Saloni")
queue.append("Rahul")
queue.append("Amit")

print("Queue after enqueue:", queue)

# Dequeue operation (first element remove hota hai)
removed = queue.pop(0)
print("Removed element:", removed)

# Front element
print("Front element:", queue[0])

# Check if queue is empty
if len(queue) == 0:
    print("Queue is empty")
else:
    print("Queue is not empty")

print("Final queue:", queue)