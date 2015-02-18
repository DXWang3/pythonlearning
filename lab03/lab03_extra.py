# Q9

def compose(f, g):

    def h(x): 
         return f(g(x))
    return h


def cycle(f1, f2, f3):
    """ Returns a function that is itself a higher order function
    >>> def add1(x):
    ...     return x + 1
    >>> def times2(x):
    ...     return x * 2
    >>> def add3(x):
    ...     return x + 3
    >>> my_cycle = cycle(add1, times2, add3)
    >>> identity = my_cycle(0)
    >>> identity(5)
    5
    >>> add_one_then_double = my_cycle(2)
    >>> add_one_then_double(1)
    4
    >>> do_all_functions = my_cycle(3)
    >>> do_all_functions(2)
    9
    >>> do_more_than_a_cycle = my_cycle(4)
    >>> do_more_than_a_cycle(2)
    10
    >>> do_two_cycles = my_cycle(6)
    >>> do_two_cycles(1)
    19
    """
    
    def result(n):
        if n % 3 == 0:
           a = f3
        
        if n % 3 == 1:
           a = f1

        if n % 3 == 2:
           a = f2
        
        if n == 0:
           return lambda x:x
         
        elif n == 1:
           return f1
        
        elif n == 2:
           return compose(f2, f1)
        
        elif n == 3:
           return compose(f3, compose(f2, f1))

        else: 
           return compose(a, result(n-1))


    return result
          
    
    

# Q10
def lambda_curry2(func):
    """
    Returns a Curried version of a two argument function func.
    >>> from operator import add
    >>> x = lambda_curry2(add)
    >>> y = x(3)
    >>> y(5)
    8
    """

    return lambda x: lambda y: func(x, y)

# Q12
def paths(m, n):
    """Return the number of paths from one corner of an
    M by N grid to the opposite corner.

    >>> paths(2, 2)
    2
    >>> paths(5, 7)
    210
    >>> paths(117, 1)
    1
    >>> paths(1, 157)
    1
    """
    if m == 1: 
       return 1
    if n == 1: 
       return 1
    
    return paths(m, n-1) + paths(m-1, n)

# Q13
def gcd(a, b):
    """Returns the greatest common divisor of a and b.
    Should be implemented using recursion.

    >>> gcd(34, 19)
    1
    >>> gcd(39, 91)
    13
    >>> gcd(20, 30)
    10
    >>> gcd(40, 40)
    40
    """
    
    if a == 0: 
       return b
    elif b == 0: 
       return a

    return gcd(b, (a % b))
