"""Required questions for lab 2"""

## Boolean Operators ##

# Q6
def both_positive(x, y):
    """
    Returns True if both x and y are positive.
    >>> both_positive(-1, 1)
    False
    >>> both_positive(1, 1)
    True
    """
    if x > 1 and y > 0:
       return x > 0  and y > 0

## while Loops ##

# Q9
def factors(n):
    """Prints out all of the numbers that divide `n` evenly.

    >>> factors(20)
    20
    10
    5
    4
    2
    1
    """
    i = n
    while i > 0:
       if n % i == 0:
           print(i)
       i = i - 1
    return None  

# Q10
def fib(n):
    """Returns the nth Fibonacci number.

    >>> fib(0)
    0
    >>> fib(1)
    1
    >>> fib(2)
    1
    >>> fib(3)
    2
    >>> fib(4)
    3
    >>> fib(5)
    5
    >>> fib(6)
    8
    """
    
    if n == 0:
       return 0
    if n == 1: 
       return 1

    return fib(n-1) + fib(n-2)

