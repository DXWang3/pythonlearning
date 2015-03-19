## Extra Recursive Objects ##

from lab07 import *

# Linked List Practice

def list_to_link(lst):
    """Takes a Python list and returns a Link with the same elements.

    >>> list_to_link([1, 2, 3])
    Link(1, Link(2, Link(3)))
    """
    if len(lst) == 0:
        return Link.empty
    return Link(lst[0], list_to_link(lst[1:]))

def link_to_list(link):
    """Takes a Link and returns a Python list with the same elements.

    >>> link = Link(1, Link(2, Link(3, Link(4))))
    >>> link_to_list(link)
    [1, 2, 3, 4]
    >>> link_to_list(Link.empty)
    []
    """
    if link is Link.empty:
        return list()
    return [link.first] + link_to_list(link.rest)

def reverse(link):
    """Returns a Link that is the reverse of the original.

    >>> reverse(Link(1))
    Link(1)
    >>> link = Link(1, Link(2, Link(3)))
    >>> reverse(link)
    Link(3, Link(2, Link(1)))
    >>> link
    Link(1, Link(2, Link(3)))
    """
    back = Link(link.first)
    while link.rest is not Link.empty:
         back = Link(link.rest.first, back)
         link = link.rest
    return back

def mutate_reverse(link):
    """Mutates the Link so that its elements are reversed.

    >>> link = Link(1)
    >>> mutate_reverse(link)
    >>> link
    Link(1)

    >>> link = Link(1, Link(2, Link(3)))
    >>> mutate_reverse(link)
    >>> link
    Link(3, Link(2, Link(1)))
    """
    if link is Link.empty:
        return
    elif link.rest is Link.empty:
        return
    else:
        mutate_reverse(link.rest)
    while link.rest is not Link.empty:
        tmp = link.first
        link.first = link.rest.first
        link.rest.first = tmp
        link = link.rest


# Tree Practice

def leaves(t):
    """Returns a list of all the entries of the leaf nodes of the Tree t.

    >>> leaves(Tree(1))
    [1]
    >>> leaves(Tree(1, [Tree(2, [Tree(3)]), Tree(4)]))
    [3, 4]
    """
    if t.is_leaf():
        return [t.entry]
    final = list()
    for x in t.branches:
        final = final + leaves(x)
    return final
           
 
def cumulative_sum(t):
    """Return a new Tree, where each entry is the sum of all entries in the
    corresponding subtree of t.

    >>> t = Tree(1, [Tree(3, [Tree(5)]), Tree(7)])
    >>> cumulative = cumulative_sum(t)
    >>> t
    Tree(1, [Tree(3, [Tree(5)]), Tree(7)])
    >>> cumulative
    Tree(16, [Tree(8, [Tree(5)]), Tree(7)])
    >>> cumulative_sum(Tree(1))
    Tree(1)
    """
    branches = [cumulative_sum(x) for x in t.branches]
    return Tree(sum(x.entry for x in branches) + t.entry, branches)   

def same_shape(t1, t2):
    """Returns whether two Trees t1, t2 have the same shape. Two trees have the
    same shape if they have the same number of branches and each of their
    children have the same shape.

    >>> t, s = Tree(1), Tree(3)
    >>> same_shape(t, t)
    True
    >>> same_shape(t, s)
    True
    >>> t = Tree(1, [Tree(2), Tree(3)])
    >>> same_shape(t, s)
    False
    >>> s = cumulative_sum(t)
    >>> same_shape(t, s)
    True
    """
    
    firstcondition = len(t1.branches) == len(t2.branches)
    secondcondition = all(same_shape(s1, s2) for s1, s2 in zip(t1.branches, t2.branches))
               
    return firstcondition and secondcondition


# Folding Linked Lists

from operator import add, sub, mul

def foldl(link, fn, z):
    """ Left fold
    >>> lst = Link(3, Link(2, Link(1)))
    >>> foldl(lst, sub, 0) # (((0 - 3) - 2) - 1)
    -6
    >>> foldl(lst, add, 0) # (((0 + 3) + 2) + 1)
    6
    >>> foldl(lst, mul, 1) # (((1 * 3) * 2) * 1)
    6
    """
    if link is Link.empty:
        return z
    
    return foldl(link.rest, fn, fn(z, link.first))

def foldr(link, fn, z):
    """ Right fold
    >>> lst = Link(3, Link(2, Link(1)))
    >>> foldr(lst, sub, 0) # (3 - (2 - (1 - 0)))
    2
    >>> foldr(lst, add, 0) # (3 + (2 + (1 + 0)))
    6
    >>> foldr(lst, mul, 1) # (3 * (2 * (1 * 1)))
    6
    """
    if link.rest is Link.empty:
        return fn(link.first, z)
    else:
        return fn(link.first, foldr(link.rest, fn, z))

identity = lambda x: x

def foldl2(link, fn, z):
    """ Write foldl using foldr
    >>> list = Link(3, Link(2, Link(1)))
    >>> foldl2(list, sub, 0) # (((0 - 3) - 2) - 1)
    -6
    >>> foldl2(list, add, 0) # (((0 + 3) + 2) + 1)
    6
    >>> foldl2(list, mul, 1) # (((1 * 3) * 2) * 1)
    6
    """
    def step(x, g):
        return lambda a: g(fn(a, x))
    return foldr(link, step, identity)(z)

