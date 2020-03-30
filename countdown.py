import sys
import math
import operator
from itertools import permutations, combinations_with_replacement, product

def apply_op(operation,a,b):
    if operation == "+":
        return a+b
    elif operation == "-":
        return a-b
    elif operation == "*":
        return a*b
    elif operation == "/" :
        return a/b
    else:
        sys.exit("Invalid Operation Passed to apply_op")

def is_int(number):
    try:
        return float(number) == number
    except ValueError:
        return False


ops = {'+':operator.add,
       '-':operator.sub,
       '*':operator.mul,
       '/':operator.div}

def rpn(expression):
    stack = []
    for term in expression:
        if is_int(term):
            stack.insert(0,term)
        else:
            if len(stack) < 2:
                return None
            n1 = stack.pop(1)
            n2 = stack.pop(0)
            try:
                result = ops[term](n1,n2)
            except ZeroDivisionError:
                return None
#Only integer intermediate solutions are allowed
            if int(result) != result:
                return None
            stack.insert(0,result)
    return result

numbers = (5.,6.,8.,10.,25.,100.)
N = len(numbers)
operations = ["+","-","*","/"]

FOUND = False
TARGET = 354.

#for num_combo, op_combo in product(permutations(numbers),combinations_with_replacement(operations,N-1)):
f = open('solutions','w')
#first two terms in rpn stack must be numbers
for n1_n2 in permutations(numbers,2):
    for op_combo in combinations_with_replacement(operations,N-1):
        reduced_numbers = tuple(x for x in numbers if x not in n1_n2)
        for expression in permutations(reduced_numbers + op_combo):
            possible_solution = rpn(n1_n2 + expression)
            if possible_solution == TARGET:
                print >> f, n1_n2 + expression, possible_solution
                f.flush()
f.close()
