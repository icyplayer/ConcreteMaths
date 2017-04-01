from lists.node import Node
from lists.deque import NodeDeque

from forms.forms import Form
import numpy as np

def josephus_iterVer(n):
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


def josephus_bitwiseVer1(n):
    """ J(2^m+l) = 2*l + 1 """
    m = len(str(bin(n))) - 2  # 0bxxxx, m = 4
    return (((n ^ (1 << (m-1))) << 1) + 1)  # J(n) = 2*l+1 = (bn-1 bn-2 ... b1 b0 1)2

def josephus_bitwiseVer2(n):
    """ J(2^m+l) = 2*l + 1 """
    bNStr = str(bin(n))
#     print(bNStr)
#     print("0b" + bNStr[3:] + bNStr[2])
    return int(bNStr[3:]+bNStr[2], 2)  # J(n) = 2*l+1 = (bn-1 bn-2 ... b1 b0 bm)2


def test1():
    """ simple test of BF method"""
    n = 10
    print("Josephus(%d) = %r" % (n, josephus_iterVer(n)))            
    print()
    
    upperBound = 50
    print("Josephus:")
    j = []
    for i in range(1, upperBound):
        j.append(josephus_iterVer(i))
    
    print(j)
    
    
def test2():
    """ bitwise test """
    print("bitwise test")
    # init form generator

    
    try:
        nLst = [0, 1, 2, 9, 10]
        result1, result2 = [], []
        for n in nLst:
            result1.append(josephus_bitwiseVer1(n))
            result2.append(josephus_bitwiseVer2(n))
        dim = 3
        form = Form([nLst, result1, result2], dim, False)
        print("Josephus bitwise-v1: J(2^m+l) = 2*l+1 = (bn-1 bn-2 ... b1 b0 1 )2")
        print("Josephus bitwise-v2: J(2^m+l) = 2*l+1 = (bn-1 bn-2 ... b1 b0 bm)2")
        print(form.genFromWithHeader(["n", "Jv1(n)", "Jv2(n)",]))

    except Exception as e:
        print(str(e))

        
test2()

