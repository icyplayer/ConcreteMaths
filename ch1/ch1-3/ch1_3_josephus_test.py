import timeit
from forms.forms import Form
from josephus import *


#===============================================================================
# tests
#===============================================================================


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

# test1()


def test2():
    """ bitwise test """
    print("bitwise test")
    try:
        # nLst = [1,2,5,9,10] # simple nLst
        nLst = [i for i in range(16)]  # full range nLst
        result1, result2 = [], []
        result3, result31 = [], []
        for n in nLst:
            result1.append(josephus_bitwiseVer1(n))
            result2.append(josephus_bitwiseVer2(n))
            result3.append(josephus_bitwiseVer3(n))
            result31.append(josephus_bitwiseVer3_1(n))
        # init form generator
        form = Form([nLst, result1, result2, result3, result31], dim=5,
                    needTranspose=False)
        print("Josephus bitwise-v1: J(2^m+l) = 2*l+1 = (bn-1 ... b1 b0 1 )2")
        print("Josephus bitwise-v2: J(2^m+l) = 2*l+1 = (bn-1 ... b1 b0 bm)2")
        print("Josephus bitwise-v3/v3.1: J((bm bm-1 ... b2 b1 b0)2) = (α βbm-1 ... βb2 βb1 βb0)2")
        print(form.genFromWithHeader(["n",
                                      "Jv1(n)",
                                      "Jv2(n)",
                                      "Jv3(n)", "Jv3.1(n)"]))
    except Exception as e:
        print(str(e))

# test2()


def test3():
    print("test3: time cost comparism of Ver3.0 and Ver3.1")
    n = 1023
    jv3_test = "josephus_bitwiseVer3(%d)" % n
    jv31_test = "josephus_bitwiseVer3_1(%d)" % n
    repeat, number = 5, 10000
    print(timeit.repeat(jv3_test, "from __main__ import josephus_bitwiseVer3",
                        repeat=repeat,  number=number))
    print(timeit.repeat(jv31_test, "from __main__ import josephus_bitwiseVer3_1",
                        repeat=repeat, number=number))


# test3()

def printSeparatorBar(msg):
    print("==================================================================")
    print(msg)
    print("------------------------------------------------------------------")


def testCvtBase():
    printSeparatorBar("x is int")
    print(cvtBase(128, oldBase=10, newBase=16))
    print(cvtBase(9, 10, 3))
    print(cvtBase(1024, 10, 2))
    printSeparatorBar("x is str, separator==None")
    print(cvtBase("10000", 2, 16))
    print(cvtBase("111", 2, 3))
    printSeparatorBar("x is str, separator==None")
    print(cvtBase("1 0 0 0 0", 2, 16, separator=" "))
    printSeparatorBar("x is list-of-str, separator==None")
    print(cvtBase(["1", "0", "0", "0", "0"], 2, 16, separator=" "))
    printSeparatorBar("x is list-of-int, separator==None")
    print(cvtBase([1, 0, 0, 0, 0], 2, 16, separator=" "))


# testCvtBase()

print(josephus_general(x=19,
                       alphaLst=[34, 5], betaLst=[76, -2, 8],
                       recurrenceLst=["10f(n)+76", "10f(n)-2", "10f(n)+8"],
                       c=10, d=3))
