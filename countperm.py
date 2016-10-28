import operator
from collections import Counter
from math import factorial
def npermutations(l):
    num = factorial(len(l))
    mults = Counter(l).values()
    den = reduce(operator.mul, (factorial(v) for v in mults), 1)
    return num / den


npermutations(['j', 'a', 'y', 'j', 'a', 'n'])
