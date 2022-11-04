stack = []
stack.append(1)
stack.append(2)
stack.append(3)

print(stack)

pop_elem = stack.pop()
print(stack, pop_elem)

queue = []
queue.append(13)
queue.append(1)
queue.append(3)
pop_elem = queue.pop(0) # removing the first element in the list

print(queue, pop_elem)