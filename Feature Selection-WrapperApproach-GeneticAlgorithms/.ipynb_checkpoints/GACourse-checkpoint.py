import random
import math
from deap.benchmarks import binary

###
### SUPPORT FUNCTIONS
###

def isBinary(x):
    for i in range(len(x)):
        if x[i]!=0 and x[i]!=1:
            return False
    return True

def isRealValued(x):
    for i in range(len(x)):
        if not float(x[i]):
            return False
    return True

def isConstrained(x, min_value=-1.0, max_value=1.0):
    for i in range(len(x)):
        if x[i]<min_value or x[i]>max_value:
            return False
    return True

# def GenerateRandom(n):
#     s = "("+str(int(random.random()*2))
#     for i in range(n):
#         s = s + "," + str(int(random.random()*2))
#     print s+")"

def RandomBinaryTuple(n):
    s = []
    for i in range(n):
        s.append(int(random.random()*2))
    return tuple(s)

###
### BINARY FUNCTIONS
###

def __CountOnes(x):
    if not isBinary(x):
        return -1
    return sum(x)/float(len(x))

def __NeedleInAHaystack(x):
    needle = (1,1,0,0,0,1,1,0,1,0,0,0,1,0,1,0,1,1,0,0,1,1,1,1,0,0,1,1,1,0,1,0,1,0,0,1,1,0,1,0,0,0,0,1,1,0,1,0,0,0,1,0,1,0,1,1,0,0,0,0,1,0,0,1,1,0,0,0,0,0,0,0,1,1,0,1,1,0,1,1,0,1,1,1,1,1,1,0,1,0,0,0,0,1,1,1,1,1,1,1,0)
    if (len(x)>len(needle)):
        return -1
    if isBinary(x) and x==needle[0:len(x)]:
        return len(x)
    else:
        return 0

def __Similarity(x):
    needle = (1,1,0,0,0,1,1,0,1,0,0,0,1,0,1,0,1,1,0,0,1,1,1,1,0,0,1,1,1,0,1,0,1,0,0,1,1,0,1,0,0,0,0,1,1,0,1,0,0,0,1,0,1,0,1,1,0,0,0,0,1,0,0,1,1,0,0,0,0,0,0,0,1,1,0,1,1,0,1,1,0,1,1,1,1,1,1,0,1,0,0,0,0,1,1,1,1,1,1,1,0)
    if (len(x)>len(needle) or not isBinary(x)):
        return -1
    else:
        sum = 0
        for i in range(len(x)):
            if x[i]==needle[i]:
                sum = sum + 1.0
        return sum/len(x)


def __Binary2Int(x):
    s = 0;
    for i in range(len(x)):
        s = s*2+x[i]
    return s

def __BinarySum(x, n=5):
    m = len(x)/int(n)
    s = 0
    for i in range(int(m)):
        b = x[i*n:i*n+n]
        #print str(b)+" ==> "+str(Binary2Int(b))
        s = s + __Binary2Int(b)
    return s

def __BinaryProduct(x, n=5):
    m = len(x)/int(n)
    s = 1
    for i in range(int(m)):
        b = x[i*n:i*n+n]
        #print str(b)+" ==> "+str(Binary2Int(b))
        s = s * __Binary2Int(b)
    return s

def __HierarchicalTrap(x, n=5):
    m = len(x)/int(n)
    s = 0
    for i in range(int(m)):
        s = s + binary.trap(x[i*n:i*n+n])
    return s

def __HierarchicalInvTrap(x, n=5):
    m = len(x)/int(n)
    s = 0
    for i in range(int(m)):
        s = s + binary.inv_trap(x[i*n:i*n+n])
    return s


def bf1(x):
    return __CountOnes(x),

def bf2(x):
    return __NeedleInAHaystack(x),

def bf3(x):
    return __Similarity(x),

def bf4(x):
    """number of variables must be multiple of 2"""
    return __BinarySum(x,2),

def bf5(x):
    """number of variables must be multiple of 4"""
    return __BinarySum(x,4),

def bf6(x):
    """number of variables must be multiple of 10"""
    return __BinarySum(x,10),

def bf7(x):
    return __BinarySum(x,len(x)),

def bf8(x):
    """number of variables must be multiple of 2"""
    return __BinaryProduct(x,2),

def bf9(x):
    """number of variables must be multiple of 4"""
    return __BinaryProduct(x,4),

def bf10(x):
    """number of variables must be multiple of 10"""
    return __BinaryProduct(x,10),

def bf11(x):
    return __BinaryProduct(x,len(x)),

def bf12(x):
    return binary.trap(x),

def bf13(x):
    return binary.inv_trap(x),

def bf14(x):
    """number of variables must be multiple of 3"""
    return __HierarchicalTrap(x,3),

def bf15(x):
    """number of variables must be multiple of 5"""
    return __HierarchicalTrap(x,5),

def bf16(x):
    """number of variables must be multiple of 3"""
    return __HierarchicalInvTrap(x,3),

def bf17(x):
    """number of variables must be multiple of 5"""
    return __HierarchicalInvTrap(x,5),

def bf18(x):
    """40 + 1 variables"""
    return binary.chuang_f1(x),

def bf19(x):
    """40 + 1 variables"""
    return binary.chuang_f2(x),

def bf20(x):
    """40 + 1 variables"""
    return binary.chuang_f3(x),

def bf20(x):
    """40 + 1 variables"""
    return binary.chuang_f3(x),

###
### REAL VALUED FUNCTIONS
###

def f1(x,y):
    """
    :param x: real value
    :param y: real value
    :return: function value :)
    """
    return abs(x*x-y),

def f2(x):
    """
    :param x: real value
    :return: function value :)
    """
    if (abs(x)>2 or not float(x)):
        print("ERROR")
        return 0
    return x*x*x - x*x,

def f3(x):
    return x*x*x - 6*x*x,

def f4(x):
    return float(x*x - 5.0*x +4.0)/float(x*x + 5.0*x +4.0)

def f5(x):
    if (x>2 or x<=0):
        print("ERROR")
        return 0
    return float(x)/math.log(x)
