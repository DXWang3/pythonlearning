from operator import add, sub

def a_plus_abs_b(a, b):
    """Return a+abs(b), but without calling abs.

    >>> a_plus_abs_b(2, 3)
    5
    >>> a_plus_abs_b(2, -3)
    5
    """
    if b < 0:
        f = a - b
    else:
        f = a + b

    return f

def two_of_three(a, b, c):
    """Return x*x + y*y, where x and y are the two largest members of the
    positive numbers a, b, and c.

    >>> two_of_three(1, 2, 3)
    13
    >>> two_of_three(5, 3, 1)
    34
    >>> two_of_three(10, 2, 8)
    164
    >>> two_of_three(5, 5, 5)
    50
    """
    max = None
    max2 = None
    if (a >= b and a >= c) and (b >= c):
       max = a
       max2 = b
    elif (a >= b and a >= c) and (c >= b):
       max = a
       max2 = c
    elif (b >= c and b >= a) and (c >= a):
       max = b
       max2 = c
    elif (b >= c and b >= a) and (a >= c):
       max = b
       max2 = a
    elif (c >= b and c >= a) and (b >= a):
       max = c
       max2 = b
    else: 
       max = c
       max2 = a

    f=max*max + max2*max2 

    return f


def if_function(condition, true_result, false_result):
    """Return true_result if condition is a true value, and
    false_result otherwise.

    >>> if_function(True, 2, 3)
    2
    >>> if_function(False, 2, 3)
    3
    >>> if_function(3==2, 3+2, 3-2)
    1
    >>> if_function(3>2, 3+2, 3-2)
    5
    """
 

    if condition:
        return true_result
    else:
        return false_result

    

def with_if_statement():
    """
    >>> with_if_statement()
    1
    """
    if c():
        return t()
    else:
        return f()

def with_if_function():
    return if_function(c(), t(), f())

def c():
    return True

def t():
    return 1

def f():
    return 3/0

def hailstone(n):
    """Print the hailstone sequence starting at n and return its
    length.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    length = 1
    
    while (n != 1):
        print(n)
        if n % 2 == 0:
             n = n // 2
        else:
             n = 3 * n + 1
        length += 1
    print(n)
    return length


challenge_question_program = """
"*** YOUR CODE HERE ***"
"""


