from lists.node import Node
from lists.deque import NodeDeque



def josephus_iterVer(n):
    # 1. init
    crowdDeq = NodeDeque()
    # number the crowd, 1~n
    for i in range(1, n + 1):
        crowdDeq.append(Node(i))
    # 2. looping untill the crowd has 1 person left
    # start from crowdDeq[0], if is -1, means last killing loop, n is odd
    startIdx = 0
    while len(crowdDeq) > 1:
        # Method 1(goal: reduce codes quntity)
        if startIdx + n % 2 == 0:
            # (startIdx == -1 and n%2 == 1) or (startIdx == 0 and n%2 == 0)
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
    return crowdDeq.peek().value()


def josephus_bitwiseVer1(n):
    """ J(2^m+l) = 2*l + 1 """
    if n == 0:
        return 0
    m = len(str(bin(n))) - 2  # 0bxxxx, m = 4
    return (((n ^ (1 << (m-1))) << 1) + 1)  # J(n)=2*l+1=(bn-1 ... b1 b0 1)2


def josephus_bitwiseVer2(n):
    """ J(2^m+l) = 2*l + 1 """
    bNStr = str(bin(n))
    return int(bNStr[3:]+bNStr[2], 2)  # J(n)=2*l+1= (bn-1 bn-2 ... b1 b0 bm)2


def josephus_bitwiseVer3(n):
    """
    n = 2^m + l
    f(1) = α
    f((bm bm-1 bm-2 ... b2 b1 b0)2) = (α βbm-1 βbm-2 ... βb1 βb0)2
    α=1, β=-1, γ=1
    note: josephus_bitwiseVer3 runs faster then josephus_bitwiseVer3_1 with
    Python3.6 interpreter with Mac OS X 10.12.3
    """
    nBinStr = str(bin(n))[2:]  # [βbm/α, βbm-1, βbm-2, ... , βb1, βb0]
    result = 0
    if n == 0:
        return result
    shift = (n).bit_length() - 1  # start from m
    for b in nBinStr:
        if b == "1":
            result += 1 << shift
        else:  # b == 0 && shift >= 1
            result += -1 << shift
        shift -= 1
    return result


def josephus_bitwiseVer3_1(n):
    """
    n = 2^m + l
    f(1) = α
    f((bm bm-1 bm-2 ... b2 b1 b0)2) = (α βbm-1 βbm-2 ... βb1 βb0)2
    α=1, β=-1, γ=1
    verified based on Ver3 using shift operation to get βbi, i=0,1,2,...,m
    aming at more general expression and readable
    """
    result = 0
    if n != 0:
        for i in range((n).bit_length()):
            result += ((((n >> i) & 0x1) << 1) - 1) << i
    return result


def cvtBitLstToInt(bLst, base=10):
    """
    bLst: int-list or str-list: [bm, bm-1, ..., b0] representing number
        (bm bm-1 ... b0)base
    NOTE: May use np.array to handle int/str differences
    See:
    https://docs.scipy.org/doc/numpy/reference/generated/numpy.fromstring.html
    """
    result = 0
    for bi in bLst[:]:
        result = result*base + int(bi)
    return result


def cvtBase(x, oldBase=10, newBase=10, separator=None, readable=True):
    """
    convert (x)oldBase to (result)newBase
    x: int/ int-separator-like str/ list of bm, bm-1, ..., b0
    separator:
        1) x is int, separator == None
        2) x is str,
            if oldBase <= 10,
            x is str and x=="bmbm-1 ... b0", separator==""
            x is str and x=="bm bm-1 ... b0", separator==" ", etc
            if oldBase > 10,
            x is str and x=="bm bm-1 ... b0", separator==" ", etc
        3) x is list of int/int-like-str, separator==None
    """
    result = 0
    # Verify bases
    if newBase <= 1 or oldBase <= 1:
        raise ValueError("Invalid base: (%d, %d)" % (oldBase, newBase))

    # 1. Verify and convert (x)oldBase => int-type (x')10
    if isinstance(x, int):
        if oldBase != 10:
            raise ValueError("Invalid base: base(int x) should be 10")
    elif isinstance(x, str):
        if oldBase <= 10:
            if isinstance(separator, str) and separator != "":
                # separator == None/"" should be ignored
                x = "".join(x.split(separator))
            x = int(x, oldBase)  # convert to base 10 format as middle result
        else:  # oldBase > 10
            if isinstance(separator, str) and len(separator) > 0:
                # must have a separator other than ""/None
                x = cvtBitLstToInt(x.split(separator), base=oldBase)
            else:
                raise ValueError("Invalid separator: %r" % separator)
    elif isinstance(x, list):
        # ignore the separator
        try:
            x = cvtBitLstToInt(x, oldBase)
        except Exception as e:
            print(str(e))
            raise RuntimeError("x conversion failed.")
    else:
        raise TypeError("Invalid x")
    # 2. Convert (x)10 to (result)newBase
    if newBase == 10:
        result = x
    else:
        expr = ""
        xArray = []
        while x >= newBase:
            xArray.append(str(x % newBase))
            x //= newBase
        xArray.append(str(x))

        if newBase <= 10:
            separator1 = ""
        else:
            separator1 = " "
        expr = separator1.join(xArray[::-1])
        if readable:
            result = "(%s)%d" % (expr, newBase)
        else:
            result = expr
    return result


def josephus_general(x, alphaLst, betaLst, recurrenceLst, c, d):
    """
    x == (x)10
    params:
        alphaLst: list of int. alphaLst = [α1, α2, α3, ... , αd-1]
        betaLst: list of int, betaLst = [β0, β1, β2, ..., βd-1]
        recurrenceLst: for further re calculation,
        so that alphaLst and betaLst will not be neccessary
    mapping:
        if bi == 0, then βbi => β0
    procedure:
        convert (x)10 to (x')d
        shift and calculate (y)c
        get result = (y')10
    """
    # Varify type
    if not isinstance(x, int):
        raise TypeError("x should be an int")
    elif not isinstance(alphaLst, list) or \
         not isinstance(betaLst, list) or \
         not isinstance(recurrenceLst, list):
        raise TypeError("alphaLst, betaLst, recurrenceLst should be list type")
    # Varify elements count in 3 lists
    if len(alphaLst) != d-1 or len(betaLst) != d or len(recurrenceLst) != d:
        raise Exception("Error: count of elements in alphaLst, betaLst, recurrenceLst is invalid")
    # Convert x into (x')c
    xd = cvtBase(x, oldBase=10, newBase=d, readable=False)
    alpha_bm = alphaLst[int(xd[0])-1]
    ycBitLst = [alpha_bm]
    for bi in xd[1:]:
        beta_bi = betaLst[int(bi)]
        ycBitLst.append(beta_bi)
    result = cvtBase(ycBitLst, oldBase=c, newBase=10, readable=False)
    return result
