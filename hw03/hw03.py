from math import log

def g(n):
    """Return the value of G(n), computed recursively.

    >>> g(1)
    1
    >>> g(2)
    2
    >>> g(3)
    3
    >>> g(4)
    10
    >>> g(5)
    22
    """
    if n == 1: 
       return 1

    if n == 2: 
       return 2

    if n == 3: 
       return 3

    return g(n-1) + 2 * g(n-2) + 3 * g(n-3)

def g_iter(n):
    """Return the value of G(n), computed iteratively.

    >>> g_iter(1)
    1
    >>> g_iter(2)
    2
    >>> g_iter(3)
    3
    >>> g_iter(4)
    10
    >>> g_iter(5)
    22
    """

   

   
    if n <= 3:

        return n
 
 
    a = 1
    b = 2
    c = 3

    for i in range(0, n-3):
       a, b, c = b, c ,c + 2 * b + 3 * a
                
    return c



def has_seven(k):
    """Returns True if at least one of the digits of k is a 7, False otherwise.

    >>> has_seven(3)
    False
    >>> has_seven(7)
    True
    >>> has_seven(2734)
    True
    >>> has_seven(2634)
    False
    >>> has_seven(734)
    True
    >>> has_seven(7777)
    True
    """
    if k % 10 == 7:

       return True

    elif k < 10 and k % 10 != 7:

       return False

    return has_seven(k // 10)


def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(7)
    7
    >>> pingpong(8)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    0
    >>> pingpong(30)
    6
    >>> pingpong(68)
    2
    >>> pingpong(69)
    1
    >>> pingpong(70)
    0
    >>> pingpong(71)
    1
    >>> pingpong(72)
    0
    >>> pingpong(100)
    2
    """
  
    def check_switch(i):
       
        if i < 7:
            return 1
       
        if i%7 == 0 or has_seven(i):
       
            return check_switch(i-1) + 1
       
        return check_switch(i-1)

    if n <= 7:
       
         return n

    if check_switch(n-1)%2 == 0:
        
         return pingpong(n-1) - 1

    return pingpong(n-1) + 1

def count_change(amount):
    """Return the number of ways to make change for amount.

    >>> count_change(7)
    6
    >>> count_change(10)
    14
    >>> count_change(20)
    60
    >>> count_change(100)
    9828
    """

    def partition(n, k):
       
        if n == 0:
            return 1
       
        if n < 0 or k == 0: 
            return 0
       
        return partition(n-k, k) + partition(n, k//2)
   
    return partition(amount, 2 ** (int(log(amount, 2))))

def towers_of_hanoi(n, start, end):
    """Print the moves required to solve the towers of hanoi game, starting
    with n disks on the start pole and finishing on the end pole.

    The game is to assumed to have 3 poles.

    >>> towers_of_hanoi(1, 1, 3)
    Move the top disk from rod 1 to rod 3
    >>> towers_of_hanoi(2, 1, 3)
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 3
    >>> towers_of_hanoi(3, 1, 3)
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 3 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 1
    Move the top disk from rod 2 to rod 3
    Move the top disk from rod 1 to rod 3
    """
    assert 0 < start <= 3 and 0 < end <= 3 and start != end, "Bad start/end"

    def move(start, end):
        print("Move the top disk from rod" ,start, "to rod", end)

    if n > 0:
        available = 6 - (start + end)
        towers_of_hanoi(n-1, start, available)
        move(start, end)
        towers_of_hanoi(n-1, available, end)


from operator import sub, mul

def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    """
    
    U = lambda f: lambda g: f(g)
    return U(lambda f: lambda n: 1 if n == 1 else mul(n, U(f)(f)(sub(n , 1))))(lambda f: lambda n: 1 if n == 1 else mul(n, U(f)(f)(sub(n , 1))))
