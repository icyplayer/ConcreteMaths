from lists.node import Node
from lists.deque import NodeDeque


from random import randrange

d = NodeDeque() # init  
# append
d.append(Node(1)) 
d.append(Node(2))
d.append(Node(3))
# validate
print(d.head)
print(d.tail)

for i in range(10):
    d.append(Node(randrange(1, 255)))
# __repr__
print(d)

# remove
d.remove(0)
d.remove(-1)
d.remove(1)
print(d)
       
# pop
print(d.pop())
print(d)