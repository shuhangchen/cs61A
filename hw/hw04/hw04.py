###########
# Objects #
###########

# Q1

class VendingMachine:
    """A vending machine that vends some product for some price.

    >>> v = VendingMachine('candy', 10)
    >>> v.vend()
    'Machine is out of stock.'
    >>> v.restock(2)
    'Current candy stock: 2'
    >>> v.vend()
    'You must deposit $10 more.'
    >>> v.deposit(7)
    'Current balance: $7'
    >>> v.vend()
    'You must deposit $3 more.'
    >>> v.deposit(5)
    'Current balance: $12'
    >>> v.vend()
    'Here is your candy and $2 change.'
    >>> v.deposit(10)
    'Current balance: $10'
    >>> v.vend()
    'Here is your candy.'
    >>> v.deposit(15)
    'Machine is out of stock. Here is your $15.'

    >>> w = VendingMachine('soda', 2)
    >>> w.restock(3)
    'Current soda stock: 3'
    >>> w.deposit(2)
    'Current balance: $2'
    >>> w.vend()
    'Here is your soda.'
    """
    "*** YOUR CODE HERE ***"
    def __init__(self, product, price):
        self.product = product
        self.price = price
        self.balance = 0
        self.stock = 0

    def restock(self, num):
        self.stock += num
        return 'Current {0} stock: {1}'.format(self.product, self.stock)

    def deposit(self, money):
        if self.stock == 0:
            return 'Machine is out of stock. Here is your ${0}.'.format(money)
        else:
            self.balance += money
            return 'Current balance: ${0}'.format(self.balance )
    
    def vend(self):
        if self.stock == 0:
            return 'Machine is out of stock.'
        elif self.balance < self.price:
            return 'You must deposit ${0} more.'.format(self.price - self.balance)
        elif self.balance == self.price:
            self.balance = 0
            self.stock -= 1
            return 'Here is your {0}.'.format(self.product)
        else:
            change = self.balance - self.price
            self.balance = 0
            self.stock -= 1
            return 'Here is your {0} and ${1} change.'.format(self.product, change)

# Q2

class interval:
    """A range of floating-point values.

    >>> a = interval(1, 4)
    >>> a
    interval(1, 4)
    >>> print(a)
    (1, 4)
    >>> a.low
    1
    >>> a.high
    4
    >>> a.low = 3    # .low and .high are read-only
    AttributeError
    >>> a.width
    3
    >>> a.width = 4
    AttributeError
    >>> b = interval(2, -2)  # Order doesn't matter
    >>> print(b, b.low, b.high)
    (-2, 2) -2 2
    >>> a + b
    interval(-1, 6)
    >>> a - b
    interval(-1, 6)
    >>> a * b
    interval(-8, 8)
    >>> b / a
    interval(-2.0, 2.0)
    >>> a / b
    ValueError
    >>> -a
    interval(-4, -1)
    """
    "*** YOUR CODE HERE ***"
    def __init__(self, start, end):
        self._low = min(start, end)
        self._high = max(start, end)
        self._width = self._high - self._low

    def __repr__(self):
        return 'interval({0}, {1})'.format(self._low, self._high)

    def __str__(self):
        return '({0}, {1})'.format(self._low, self._high)
    @property
    def low(self):
        return self._low

    @property
    def high(self):
        return self._high
    @property
    def width(self):
        return self._width
        
    def __add__(self, other):
        return interval(self._low + other._low, self._high + other._high)

    def __sub__(self, other):
        return interval(self._low - other._high, self._high - other._low)

    def __mul__(self, other):
        return interval(min(self._low * other._low, self._high * other._high,self._low * other._high,self._high * other._low), max(self._low * other._low, self._high * other._high,self._low * other._high,self._high * other._low))

    def __neg__(self):
        return interval(-self._low, -self._high)

    def __truediv__(self, other):
        if (other._low < 0 and other._high > 0) or other._low == 0 or other._high== 0 :
            raise ValueError('division by interval containing 0')
        else:
            return interval(min(self._low / other._high, self._high / other._low, self._low / other._low, self._high / other._high), max(self._low / other._high, self._high / other._low, self._low / other._low, self._high / other._high))
    
              

        

# Q3

class MissManners:
    """A container class that only forward messages that say please.

    >>> v = VendingMachine('teaspoon', 10)
    >>> v.restock(2)
    'Current teaspoon stock: 2'

    >>> m = MissManners(v)
    >>> m.ask('vend')
    'You must learn to say please first.'
    >>> m.ask('please vend')
    'You must deposit $10 more.'
    >>> m.ask('please deposit', 20)
    'Current balance: $20'
    >>> m.ask('now will you vend?')
    'You must learn to say please first.'
    >>> m.ask('please hand over a teaspoon')
    'Thanks for asking, but I know not how to hand over a teaspoon.'
    >>> m.ask('please vend')
    'Here is your teaspoon and $10 change.'

    >>> really_fussy = MissManners(m)
    >>> really_fussy.ask('deposit', 10)
    'You must learn to say please first.'
    >>> really_fussy.ask('please deposit', 10)
    'Thanks for asking, but I know not how to deposit.'
    >>> really_fussy.ask('please please deposit', 10)
    'Thanks for asking, but I know not how to please deposit.'
    >>> really_fussy.ask('please ask', 'please deposit', 10)
    'Current balance: $10'
    """
    "*** YOUR CODE HERE ***"
    polite_str = 'please'
    def __init__(self, obj):
        self.obj = obj
        
    def ask(self, asking, *args):
        if len(asking) < len(MissManners.polite_str) or asking[:len(MissManners.polite_str)] != MissManners.polite_str :
            return 'You must learn to say please first.'
        else:
            call_method = asking[len(MissManners.polite_str)+1:]
            if hasattr(self.obj, call_method):
                return getattr(self.obj,call_method)(*args)
            else:
                return 'Thanks for asking, but I know not how to {0}.'.format(call_method)

# Q4, Q5, and Q6

class Link:
    """
    >>> s = Link(1, Link(2, Link(3)))
    >>> s
    Link(1, Link(2, Link(3)))
    >>> len(s)
    3
    >>> s[2]
    3
    >>> s = Link.empty
    >>> len(s)
    0
    """
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest is not Link.empty:
            rest_str = ', ' + repr(self.rest)
        else:
            rest_str = ''
        return 'Link({0}{1})'.format(repr(self.first), rest_str)

    def __len__(self):
        """ Return the number of items in the linked list.

        >>> s = Link(1, Link(2, Link(3)))
        >>> len(s)
        3
        >>> s = Link.empty
        >>> len(s)
        0
        >>> len(ints_list(100000)) # Check for iterative solution
        100000
        """
        "*** YOUR CODE HERE ***"
        link_len = 0
        temp_link = self
        while temp_link is not Link.empty:
            link_len += 1
            temp_link = temp_link.rest
        return link_len

    # The following method may be useful for implementation of the
    # __getitem__ and insert methods.
    def _get_link(self, i):
        """An internal utility method that returns the Ith Link after
        self (I == 0 returns self, I == 1 returns self.rest, etc.).  Returns
        empty if I is len(self).  Raises IndexError unless 0 <= I <= len(self).
        >>> L = Link(1, Link(2, Link(3)))
        >>> L._get_link(0)
        Link(1, Link(2, Link(3)))
        >>> L._get_link(1)
        Link(2, Link(3))
        >>> L._get_link(2)
        Link(3)
        >>> L._get_link(3)
        ()
        >>> L._get_link(4)
        Traceback (most recent call last):
           ...
        IndexError: list index out of range
        >>> L._get_link(-1)
        Traceback (most recent call last):
           ...
        IndexError: list index out of range
        >>> (ints_list(100000))._get_link(1).first
        2
        """
        if i < 0:
            raise IndexError("list index out of range")
        "*** YOUR CODE HERE ***"
        temp_link = self
        while i > 0 :
            temp_link = temp_link.rest
            i -= 1
        return temp_link

    def __getitem__(self, i):
        """Returns the element found at index I.

        >>> s = Link(1, Link(2, Link(3)))
        >>> s[1]
        2
        >>> s[2]
        3
        >>> (ints_list(100000))[1]  # Check for iterative solution
        2
        """
        if i < 0:
            i = len(self) + i
        "*** YOUR CODE HERE ***"
        return self._get_link(i).first

    def __add__(self, lst):
        """Returns the result of non-destructively appending LST to the
        end of the sequence starting with self.
        """
        "*** YOUR CODE HERE ***"
        if self == Link.empty:
            return lst
        else:
            p =result= Link(self.first)
            q = self
            for i in range(1, len(self)):
                p.rest = Link(q.rest.first)
                p = p.rest
                q = q.rest
            p.rest = lst

            return result

    def insert(self, k, val):
        """Destructively insert VAL into the list headed by SELF at index
        K, moving the previous item K and later items right.  Returns the
        resulting linked list.  Assumes 0 <= K <= len(self).
        """
        "*** YOUR CODE HERE ***"
        temp_link = self
        if k < len(self):
            q = add(self._get_link(k), Link.empty)
            while k > 0 :
                temp_link = temp_link.rest
                k -= 1
            
            temp_link.first = val
            temp_link.rest = q
        elif k == len(self):
            while k > 1 :
                temp_link = temp_link.rest
                k -= 1
            temp_link.rest = Link(val)
        else:
            raise IndexError()
        return self

# ints_list is used to test that a method does not use recursion by making
# sure that a very long list does not cause a large recursion depth.
def ints_list(k):
    """A linked list containing the numbers 1 to K."""
    if k < 1:
        return Link.empty
    p = result = Link(1)
    for i in range(2, k + 1):
        p.rest = Link(i)
        p = p.rest
    return result

def add(L0, L1):
    """Return the list formed by non-destructively appending the items in L1
    to the end of those in L0.

    >>> s = Link(1, Link(2))
    >>> s + Link.empty
    Link(1, Link(2))
    >>> s + Link(3, Link(4))
    Link(1, Link(2, Link(3, Link(4))))
    >>> s   # Non-destructive
    Link(1, Link(2))
    >>> add(Link.empty, s)
    Link(1, Link(2))
    >>> s = ints_list(100000) + Link(100001)  # Check for iterative solution
    """
    if L0 is Link.empty:
        "*** YOUR CODE HERE ***"
        return L1
    else:
        return L0 + L1

def insert(L, k, val):
    """Destructively insert VAL into L at position K, returning the
    resulting list.  Assumes 0 <= K <= len(L).

    >>> L = Link(1, Link(2, Link(3)))
    >>> L.insert(1, 5)
    Link(1, Link(5, Link(2, Link(3))))
    >>> L
    Link(1, Link(5, Link(2, Link(3))))
    >>> L.insert(4, 6)  # Insert off the end.
    Link(1, Link(5, Link(2, Link(3, Link(6)))))
    >>> L.insert(0, 7)  # Insert at front
    Link(7, Link(1, Link(5, Link(2, Link(3, Link(6))))))
    >>> L  # New element is "left of" L
    Link(7, Link(1, Link(5, Link(2, Link(3, Link(6))))))
    >>> L.insert(7, 8)
    IndexError
    >>> insert((), 0, 3)
    Link(3)
    """
    if L is Link.empty:
         return Link(val)
    else:
         return L.insert(k, val)

class Tree:
    def __init__(self, label, children=()):
        self.label = label
        for branch in children:
            assert isinstance(branch, Tree)
        self.children = list(children)

    def __repr__(self):
        if self.children:
            children_str = ', ' + repr(self.children)
        else:
            children_str = ''
        return 'Tree({0}{1})'.format(self.label, children_str)

    def is_leaf(self):
        return not self.children

# Q7

def same_shape(t1, t2):
    """Returns whether two Trees t1, t2 have the same shape. Two trees have the
    same shape iff they have the same number of children and each pair
    of corresponding children have the same shape.

    >>> t, s = Tree(1), Tree(3)
    >>> same_shape(t, t)
    True
    >>> same_shape(t, s)
    True
    >>> t = Tree(1, [Tree(2), Tree(3)])
    >>> same_shape(t, s)
    False
    >>> s = Tree(4, [Tree(3, [Tree(2, [Tree(1)])])])
    >>> same_shape(t, s)
    False
    """
    "*** YOUR CODE HERE ***"
    if t1 is ():
        if t2 is ():
            return True
        else:
            return False
    elif t2 is ():
        return False
    else:
        if len(t1.children) != len(t2.children):
            return False
        else:
            for child1, child2 in zip(t1.children, t2.children):
                if not same_shape(child1, child2):
                    return False
            return True

class Tree:
    def __init__(self, label, children=()):
        self.label = label
        for branch in children:
            assert isinstance(branch, Tree)
        self.children = list(children)

    def __repr__(self):
        if self.children:
            children_str = ', ' + repr(self.children)
        else:
            children_str = ''
        return 'Tree({0}{1})'.format(self.label, children_str)

    def is_leaf(self):
        return not self.children

# Q8

def long_paths(tree, n):
    """Return a list all paths in tree with length at least n.

    >>> t = Tree(3, [Tree(4), Tree(4), Tree(5)])
    >>> left = Tree(1, [Tree(2), t])
    >>> mid = Tree(6, [Tree(7, [Tree(8)]), Tree(9)])
    >>> right = Tree(11, [Tree(12)])
    >>> whole = Tree(0, [left, Tree(13), mid, right])
    >>> for path in long_paths(whole, 2):
    ...     print(path)
    ...
    Link(0, Link(1, Link(2)))
    Link(0, Link(1, Link(3, Link(4))))
    Link(0, Link(1, Link(3, Link(4))))
    Link(0, Link(1, Link(3, Link(5))))
    Link(0, Link(6, Link(7, Link(8))))
    Link(0, Link(6, Link(9)))
    Link(0, Link(11, Link(12)))
    >>> for path in long_paths(whole, 3):
    ...     print(path)
    ...
    Link(0, Link(1, Link(3, Link(4))))
    Link(0, Link(1, Link(3, Link(4))))
    Link(0, Link(1, Link(3, Link(5))))
    Link(0, Link(6, Link(7, Link(8))))
    >>> long_paths(whole, 4)
    []
    """
    "*** YOUR CODE HERE ***"
    if tree is ():
        return []
    else:
        sub_lst = []
        if n ==  0:
            for child in tree.children:
                sub_paths = all_paths(child)
                if sub_paths:
                    for path in sub_paths:
                        sub_lst = sub_lst + [ Link(tree.label, path) ]
            if sub_lst == []:
                sub_lst = [Link(tree.label)]
            return sub_lst
        else:
            for child in tree.children:
                subpaths = long_paths(child, n-1)
                if subpaths:
                    for path in subpaths:
                        sub_lst = sub_lst + [ Link(tree.label, path) ]
            return sub_lst


def all_paths(tree):
    if tree is ():
        return []
    else:
        sub_lst = []
        for child in tree.children:
            sub_paths = all_paths(child)
            if sub_paths:
                for path in sub_paths:
                    sub_lst = sub_lst + [Link(tree.label, path)]
                    
        if sub_lst == []:
            return [Link(tree.label)]
        else:
            return sub_lst
