from lists.node import Node
from lists.deque import NodeDeque
from lists.deque import ListDeque


from random import randrange


def testNodeDeque():
    print("====test NodeDeque====")
    print("Init NodeDeque")
    try:
        d = NodeDeque()  # init
        print("\tNodeDeque initialized")
    except Exception:
        print("\tInit failed")
    # append
    print("append")
    d.append(Node(1))
    d.append(Node(2))
    d.append(Node(3))
    # validate
    print(d.head)
    print(d.tail)

    for i in range(10):
        d.append(Node(randrange(1, 255)))
    # __repr__
    print("__repr__:")
    print(d)

    # remove
    print("remove:")
    d.remove(0)
    d.remove(-1)
    d.remove(1)
    print(d)
    # pop
    print("pop:")
    print(d.pop())
    print(d)
    print("len:")
    print(len(d))  
    # peek 
    print("%s:" % d.peek.__name__)
    print(d.peek())  
    print("==========END==========\n\n")


def testListDeque():
    print("====test ListDeque====")
    print("Init ListDeque")
    try:
        d = ListDeque()  # init
        print("\tListDeque initialized")
    except Exception:
        print("\tInit failed")
    # append
    print("append")
    d.append(1)
    d.append(2)
    d.append(3)

    for i in range(10):
        d.append(randrange(1, 255))
    # __repr__
    print("__repr__:")
    print(d)

    # remove
    print("remove:")
    d.remove(0)
    d.remove(-1)
    d.remove(1)
    print(d)
    # pop
    print("pop:")
    print(d.pop())
    print(d)
    # len
    print("len:")
    print(len(d))
    # peek 
    print("%s:" % d.peek.__name__)
    print(d.peek())
    print("==========END==========\n\n")

testNodeDeque()
testListDeque()
