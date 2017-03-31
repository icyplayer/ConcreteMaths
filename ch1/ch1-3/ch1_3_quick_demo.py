from lists.node import Node
from lists.deque import NodeDeque


def josephus(n):
    # 1. init
    crowdDeq = NodeDeque()
    # number the crowd, 1~n
    for i in range(1, n + 1):
        crowdDeq.append(Node(i))
    # 2. looping untill the crowd has 1 person left
    startIdx = 0  # start from crowdDeq[0], if is -1, means last killing loop, n is odd
    while len(crowdDeq) > 1:   
        # Method 1(goal: reduce codes quntity)   
        if startIdx + n % 2 == 0:  # (startIdx == -1 and n%2 == 1) or (startIdx == 0 and n%2 == 0)
            upperBound = n - 1
        else:
            upperBound = n - 2
        # update startIdx, startIdx must be updated before n changed  
        if n % 2 == 1 and startIdx == 0:
            startIdx = -1
        elif n % 2 == 1 and startIdx == -1:  
            startIdx = 0
 
        for i in range(upperBound, -1, -2):
            crowdDeq.remove(i)  # must be removed in reverse order
            n -= 1

    #===========================================================================
    #   # Method 2(goal: easier to understand)
    #   if startIdx == 0:
    #       if n%2 == 0:
    #           for i in range(n-1, -1, -2):
    #               crowdDeq.remove(i)  # must be removed in reverse order
    #               n -= 1
    #       else:  # n%2 == 1
    #           for i in range(n-2, -1, -2):
    #               crowdDeq.remove(i)
    #               n -= 1
    #           startIdx = -1
    #   else:  # startIdx = -1
    #       if n%2 == 0:
    #           for i in range(n-2, -1, -2):
    #               crowdDeq.remove(i)
    #               n -= 1
    #       else:
    #           for i in range(n-1, -1, -2):
    #               crowdDeq.remove(i)
    #               n -= 1
    #           startIdx = 0
    #===========================================================================
    
    # print("Debug: n=%d, left=%r" % (n, crowdDeq))  # debug message

    return crowdDeq.peek().value()


# simple test
n = 10
print("Josephus(%d) = %r" % (n, josephus(n)))            
print()


upperBound = 50
print("Josephus:")
j = []
for i in range(1, upperBound):
    j.append(josephus(i))


print(j)

