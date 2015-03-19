class Link:
    """A linked list.

    >>> s = Link(3, Link(4, Link(5)))
    >>> len(s)
    3
    >>> s[2]
    5
    >>> s
    Link(3, Link(4, Link(5)))
    """
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __getitem__(self, i):
        if i == 0:
            return self.first
        else:
            return self.rest[i-1]

    def __len__(self):
        return 1 + len(self.rest)

    def __repr__(self):
        if self.rest:
            rest_str = ', ' + repr(self.rest)
        else:
            rest_str = ''
        return 'Link({0}{1})'.format(self.first, rest_str)

def deep_map(f, s):
    """Return a Link with the same structure as s but with fn mapped over
    its elements and any elements of linked lists contained anywhere within it.

    >>> s = Link(1, Link(Link(2, Link(3)), Link(4)))
    >>> deep_map(lambda x: x * x, s)
    Link(1, Link(Link(4, Link(9)), Link(16)))
    >>> s # unchanged
    Link(1, Link(Link(2, Link(3)), Link(4)))
    >>> deep_map(lambda x: 2 * x, Link(s, Link(Link(Link(5)))))
    Link(Link(2, Link(Link(4, Link(6)), Link(8))), Link(Link(Link(10))))
    """
    if s is Link.empty:
        return s
    elif isinstance(s.first, Link):
        return Link(deep_map(f, s.first), deep_map(f, s.rest))
    else:
        return Link(f(s.first), deep_map(f, s.rest))

def reverse(s):
    """Return a linked list with the elements of s in reverse order.

    >>> s = Link(3, Link(5, Link(4, Link(6))))
    >>> reverse(s)
    Link(6, Link(4, Link(5, Link(3))))
    >>> s
    Link(3, Link(5, Link(4, Link(6))))
    """
    new = Link(s.first, s.rest)
    reverse = Link.empty
    while new is not Link.empty:
        reverse = Link(new.first, reverse)
        new = new.rest
    return reverse

def has_cycle(s):
    """Return whether Link s contains a cycle.

    >>> s = Link(1, Link(2, Link(3)))
    >>> s.rest.rest.rest = s
    >>> has_cycle(s)
    True
    >>> t = Link(1, Link(2, Link(3)))
    >>> has_cycle(t)
    False
    """
    copy = Link(s.first, s.rest)
    newlinks = [s]
    while copy is not Link.empty:
        copy = copy.rest
        if copy in newlinks:
            return True
        newlinks.append(copy)
    return False

def has_cycle_constant(s):
    """Return whether Link s contains a cycle.

    >>> s = Link(1, Link(2, Link(3)))
    >>> s.rest.rest.rest = s
    >>> has_cycle_constant(s)
    True
    >>> t = Link(1, Link(2, Link(3)))
    >>> has_cycle_constant(t)
    False
    """
    # Challenge: replace this line with your implementation
    if s == Link.empty:
        return False
    else:        
        while s.rest != Link.empty:
            if s.rest.rest == Link.empty:
                return False
            elif s.rest == s or s.rest.rest == s:
                return True
            else:
                s, s.rest = s, s.rest.rest.rest
        return False

class Mobile:
    """A binary mobile has branches; each branch has a weight or a mobile.

    >>> m = Mobile(Branch(1, Weight(2)), Branch(2, Weight(1)))
    >>> m.weight
    3
    >>> m.is_balanced()
    True
    >>> m.left.contents = Mobile(Branch(1, Weight(1)), Branch(2, Weight(1)))
    >>> m.weight
    3
    >>> m.left.contents.is_balanced()
    False
    >>> m.is_balanced() # All submobiles must be balanced for m to be balanced
    False
    >>> m.left.contents.right.contents.weight = 0.5
    >>> m.left.contents.is_balanced()
    True
    >>> m.is_balanced()
    False
    >>> m.right.length = 1.5
    >>> m.is_balanced()
    True
    """
    def __init__(self, left, right):
        for v in (left, right):
            if type(v) != Branch:
                raise TypeError(str(v) + ' is not a Branch')
        self.left = left
        self.right = right

    @property
    def weight(self):
        """The total weight of the mobile."""
        return self.left.contents.weight + self.right.contents.weight

    def is_balanced(self):
        """True if and only if the mobile is balanced."""
        if self.left.torque == self.right.torque:
            if isinstance(self.left.contents, Weight) and isinstance(self.right.contents, Weight):
                return True
            elif isinstance(self.left.contents, Mobile) and isinstance(self.right.contents, Mobile):
                return self.left.contents.is_balanced() and self.right.contents.is_balanced()
            elif isinstance(self.left.contents, Mobile):
                return  self.left.contents.is_balanced()
            else:
                return self.right.contents.is_balanced()
        return False

class Branch:
    """A branch of a binary mobile."""
    def __init__(self, length, contents):
        if type(contents) not in (Weight, Mobile):
            raise TypeError(str(contents) + ' is not a Weight or Mobile')
        self.length = length
        self.contents = contents

    @property
    def torque(self):
        """The torque on the branch"""
        return self.length * self.contents.weight

class Weight:
    """A weight at the end of a branch."""
    def __init__(self, weight):
        self.weight = weight

    def is_balanced(self):
        return True



