def interval(a, b):
    """Construct an interval from a to b."""

   
    return [a, b]

def lower_bound(x):
    """Return the lower bound of interval x."""

    return x[0]

def upper_bound(x):
    """Return the upper bound of interval x."""
   
    return x[1]

def str_interval(x):
    """Return a string representation of interval x.
    >>> str_interval(interval(-1, 2))
    '-1 to 2'
    """
    return '{0} to {1}'.format(lower_bound(x), upper_bound(x))

def add_interval(x, y):
    """Return an interval that contains the sum of any value in interval x and
    any value in interval y.
    >>> str_interval(add_interval(interval(-1, 2), interval(4, 8)))
    '3 to 10'
    """
    lower = lower_bound(x) + lower_bound(y)
    upper = upper_bound(x) + upper_bound(y)
    return interval(lower, upper)

def mul_interval(x, y):
    """Return the interval that contains the product of any value in x and any
    value in y.
    >>> str_interval(mul_interval(interval(-1, 2), interval(4, 8)))
    '-8 to 16'
    """
    p1 = lower_bound(x) * lower_bound(y)
    p2 = lower_bound(x) * upper_bound(y)
    p3 = upper_bound(x) * lower_bound(y)
    p4 = upper_bound(x) * upper_bound(y)
    return interval(min(p1, p2, p3, p4), max(p1, p2, p3, p4))

def div_interval(x, y):
    """Return the interval that contains the quotient of any value in x divided
    by any value in y.
    Division is implemented as the multiplication of x by the reciprocal of y.
    >>> str_interval(div_interval(interval(-1, 2), interval(4, 8)))
    '-0.25 to 0.5'
    """
    assert (y != 0), "Y cannot be 0!"

    reciprocal_y = interval(1/upper_bound(y), 1/lower_bound(y))
    return mul_interval(x, reciprocal_y)

def sub_interval(x, y):
    """Return the interval that contains the difference between any value in x
    and any value in y.
    >>> str_interval(sub_interval(interval(-1, 2), interval(4, 8)))
    '-9 to -2'
    """

    opposite_y = interval(-upper_bound(y), -lower_bound(y))
    return add_interval(x, opposite_y)

def par1(r1, r2):
    return div_interval(mul_interval(r1, r2), add_interval(r1, r2))

def par2(r1, r2):
    one = interval(1, 1)
    rep_r1 = div_interval(one, r1)
    rep_r2 = div_interval(one, r2)
    return div_interval(one, add_interval(rep_r1, rep_r2))

# These two intervals give different results for parallel resistors:
"*** YOUR CODE HERE ***"

def test():

    print(par1(interval(6,8), interval(7,9)) == par2(interval(6,8), interval(7,9)))
  
def multiple_references_explanation():
    return """The mulitple reference problem..."""





def quadratic(x, a, b, c):
    """Return the interval that is the range of the quadratic defined by
    coefficients a, b, and c, for domain interval x.
    >>> str_interval(quadratic(interval(0, 2), -2, 3, -1))
    '-3 to 0.125'
    >>> str_interval(quadratic(interval(1, 3), 2, -3, 1))
    '0 to 10'
    """
   
    t = lower_bound(x)
    r = upper_bound(x)
    q = -b/(2*a)

    if q <= r and q >= t:

         m = min((a *(t ** 2) + b * t + c), (a * (q ** 2) + b * q + c), (a * (r ** 2) + b * r + c))
         n = max((a *(t ** 2) + b * t + c), (a * (q ** 2) + b * q + c), (a * (r ** 2) + b * r + c))

    else: 

         m = min((a *(t ** 2) + b * t + c), (a * (r ** 2) + b * r + c))
         n = max((a *(t ** 2) + b * t + c), (a * (r ** 2) + b * r + c))
   
    return interval(m, n)

def polynomial(x, c):
    """Return the interval that is the range of the polynomial defined by
    coefficients c, for domain interval x.
    >>> str_interval(polynomial(interval(0, 2), [-1, 3, -2]))
    '-3 to 0.125'
    >>> str_interval(polynomial(interval(1, 3), [1, -3, 2]))
    '0 to 10'
    >>> str_interval(polynomial(interval(0.5, 2.25), [10, 24, -6, -8, 3]))
    '18.0 to 23.0'
    """
 
    """ Define f, df, dff """
    
 

    def add_fns(f_and_df, g_and_dg):

        return lambda x, derive: f_and_df(x, derive) + g_and_dg(x, derive)


    def f(m):
        f = lambda m: 0

        for k, i in enumerate(c):
            f = add_fns(f , (lambda m: (i * (m ** k)))) 
        return f

    def df(m):
        df = lambda m: 0
        for k, i in enumerate(c):
           if (k > 0):
              df = add_fns(df, (lambda m: (i * (k - 1) * (m ** (k - 1)))))
        return df
    
    def ddf(m):
        ddf = lambda m: 0
        for k, i in enumerate(c):
           if (k > 1):
              ddf = add_fns(ddf, (lambda m: (i * (k - 1) * (k - 2) * (m ** (k - 2)))))
        return ddf        

    """ Implement new x value via Newton method"""

    def newton(f, df):

        def iterate(m):
            return (m - f(m))/df(m)
        return iterate

    """ Define when is the approximation close enough to the zero. """

    def bound(x, y, bound = 1e-15):

        
        if x >= y:
           return x - y < bound
        else:
           return y - x < bound

    """ Returns whether the root is close enough in boolean. """ 

    def close(m):

        return bound(df(m), 0, 1e-15)

    
    
    """ Progressively implement newton method until value is close enough """

    def increment(iterate, close, guess=1, max_updates = 100):
         
        k = 0
        while not close(guess) and k < max_updates:
            guess = iterate(guess)
            k = k + 1
        return guess

    """ Find the location of the zero. """

    def find_zero(f, df, guess=1):

        def valid(m):
            return bound(f(m), 0)

        return increment(newton(f, df), valid, guess)

    a = lower_bound(x)
    b = upper_bound(x) 
    limit = [find_zero(df, ddf, a + ((b - a) * i / 100)) for i in range(0, 101)]
    list = [n for n in limit if n > a and n < b]
    valuelist = [f(d) for d in list]
    return interval(min(valuelist), max(valuelist))
