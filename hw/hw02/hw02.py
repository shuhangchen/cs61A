HW_SOURCE_FILE = 'hw02.py'
from math import log, ceil
from operator import sub, mul
def square(x):
    return x * x

def triple(x):
    return 3 * x

def identity(x):
    return x

def increment(x):
    return x + 1

def product(n, term):
    """Return the product of the first n terms in a sequence.

    n    -- a positive integer
    term -- a function that takes one argument

    >>> product(3, identity) # 1 * 2 * 3
    6
    >>> product(5, identity) # 1 * 2 * 3 * 4 * 5
    120
    >>> product(3, square)   # 1^2 * 2^2 * 3^2
    36
    >>> product(5, square)   # 1^2 * 2^2 * 3^2 * 4^2 * 5^2
    14400
    """
    if n==1:
        return term(n)
    else:
        return term(n) * product(n-1, term)
    
def factorial(n):
    """Return n factorial for n >= 0 by calling product.

    >>> factorial(4)
    24
    >>> factorial(6)
    720
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'factorial', ['Recursion', 'For', 'While'])
    True
    """
    "*** YOUR CODE HERE ***"
    return product(n, identity)

from operator import add, mul

def accumulate(combiner, base, n, term):
    """Return the result of combining the first N terms in a sequence.  The
    terms to be combined are TERM(1), TERM(2), ..., TERM(N).  COMBINER is a
    two-argument function.  Treating COMBINER as if it were a binary operator,
    the return value is
        BASE COMBINER TERM(1) COMBINER TERM(2) ... COMBINER TERM(N)

    >>> accumulate(add, 0, 5, identity)  # 0 + 1 + 2 + 3 + 4 + 5
    15
    >>> accumulate(add, 11, 5, identity) # 11 + 1 + 2 + 3 + 4 + 5
    26
    >>> accumulate(add, 11, 0, identity) # 11
    11
    >>> accumulate(add, 11, 3, square)   # 11 + 1^2 + 2^2 + 3^2
    25
    >>> accumulate(mul, 2, 3, square)   # 2 * 1^2 * 2^2 * 3^2
    72
    """
    if n < 2:
        if term(n) == []:
            return base
        else:
            return combiner(base, term(n))
    elif term(n) == []:
        return accumulate(combiner,base,n-1,term)
    else:
        return combiner(term(n),accumulate(combiner,base,n-1,term))

def summation_using_accumulate(n, term):
    """Returns the sum of TERM(1) + ... + TERM(N). The implementation
    uses accumulate.

    >>> summation_using_accumulate(5, square)
    55
    >>> summation_using_accumulate(5, triple)
    45
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'summation_using_accumulate',
    ...       ['Recursion', 'For', 'While'])
    True
    """
    "*** YOUR CODE HERE ***"
    return accumulate(add,0,n,term)

def product_using_accumulate(n, term):
    """An implementation of product using accumulate.

    >>> product_using_accumulate(4, square)
    576
    >>> product_using_accumulate(6, triple)
    524880
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'product_using_accumulate',
    ...       ['Recursion', 'For', 'While'])
    True
    """
    "*** YOUR CODE HERE ***"
    return accumulate(mul,1,n, term)

def true(x):
    return True

def false(x):
    return False

def odd(x):
    return x % 2 == 1

def filtered_accumulate(combiner, base, pred, n, term):
    """Return the result of combining the terms in a sequence of N terms
    that satisfy the predicate PRED.  COMBINER is a two-argument function.
    If v1, v2, ..., vk are the values in TERM(1), TERM(2), ..., TERM(N)
    that satisfy PRED, then the result is
         BASE COMBINER v1 COMBINER v2 ... COMBINER vk
    (treating COMBINER as if it were a binary operator, like +). The
    implementation uses accumulate.

    >>> filtered_accumulate(add, 0, true, 5, identity)  # 0 + 1 + 2 + 3 + 4 + 5
    15
    >>> filtered_accumulate(add, 11, false, 5, identity) # 11
    11
    >>> filtered_accumulate(add, 0, odd, 5, identity)   # 0 + 1 + 3 + 5
    9
    >>> filtered_accumulate(mul, 1, odd, 5, square)  # 1 * 1 * 9 * 25
    225
    >>> # Do not use while/for loops or recursion
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'filtered_accumulate',
    ...       ['While', 'For', 'Recursion', 'FunctionDef'])
    True
    """
    return accumulate(combiner, base, n, lambda x: term(x) if pred(x) else [] )

def repeated(f, n):
    """Return the function that computes the nth application of f.

    >>> add_three = repeated(increment, 3)
    >>> add_three(5)
    8
    >>> repeated(triple, 5)(1) # 3 * 3 * 3 * 3 * 3 * 1
    243
    >>> repeated(square, 2)(5) # square(square(5))
    625
    >>> repeated(square, 4)(5) # square(square(square(square(5))))
    152587890625
    >>> repeated(square, 0)(5)
    5
    """
    "*** YOUR CODE HERE ***"
    def apply_nth(x):
        if n == 1:
            return f(x)
        elif n == 0:
            return x
        else:
            return f(repeated(f, n-1)(x))

    return apply_nth

def compose1(f, g):
    """Return a function h, such that h(x) = f(g(x))."""
    def h(x):
        return f(g(x))
    return h

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
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'g', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    if n < 4:
        return n
    else:
        return g(n-1) + 2* g(n -2) + 3*g(n-3)

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
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'g_iter', ['Recursion'])
    True
    """
    "*** YOUR CODE HERE ***"
    lst = [ 1, 2, 3 ]
    if n < 4:
        return lst[n-1]
    else:
        for i in range(3,n):
            a = lst[i-1] + 2 * lst[i-2] + 3 * lst[i-3]
            lst = lst + [a]
    return lst[n-1]
        

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
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'pingpong', ['Assign', 'AugAssign'])
    True
    """
    "*** YOUR CODE HERE ***"
    def checkDir(n):
        if n ==1:
            return 1
        elif ppcond(n):
            return -1 * checkDir(n-1)
        else:
            return checkDir(n-1)
    
    if n==1:
        return 1
    else:
        return checkDir(n - 1) + pingpong(n-1)
            

def ppcond(n):
    def containsd7(n):
        if n < 10:
            return n == 7
        else:
            return (n % 10) == 7 or containsd7(n//10)
    if n % 7 ==0 or containsd7(n):
        return 1

                
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
    elif k < 10:
        return False
    else:
        return has_seven(k // 10)

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
    "*** YOUR CODE HERE ***"
    def count_change_with(amount,base):
        if amount < 0 or base < 0:
            return 0
        elif amount == 0:
            return 1
        else:
            return count_change_with(amount, base-1) + count_change_with(amount-pow(2,base),base)
    return count_change_with(amount, ceil(log(amount,2)))
    
def print_move(origin, destination):
    """Print instructions to move a disk."""
    print("Move the top disk from rod", origin, "to rod", destination)

def move_stack(n, start, end):
    """Print the moves required to move n disks on the start pole to the end
    pole without violating the rules of Towers of Hanoi.

    n -- number of disks
    start -- a pole position, either 1, 2, or 3
    end -- a pole position, either 1, 2, or 3

    There are exactly three poles, and start and end must be different. Assume
    that the start pole has at least n disks of increasing size, and the end
    pole is either empty or has a top disk larger than the top n start disks.

    >>> move_stack(1, 1, 3)
    Move the top disk from rod 1 to rod 3
    >>> move_stack(2, 1, 3)
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 3
    >>> move_stack(3, 1, 3)
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 3 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 1
    Move the top disk from rod 2 to rod 3
    Move the top disk from rod 1 to rod 3
    """
    def select_3rd(start, end):
        if start != 1 and end != 1:
            return 1
        elif start != 2 and end != 2:
            return 2
        else:
            return 3
    assert 1 <= start <= 3 and 1 <= end <= 3 and start != end, "Bad start/end"
    "*** YOUR CODE HERE ***"
    if n == 1:
        print_move(start, end)
    else:
        move_stack(n-1, start, select_3rd(start, end))
        print_move(start, end)
        move_stack(n-1, select_3rd(start, end), end)
        
###################
# Extra Questions #
###################

from operator import sub, mul

def Y(f):
    """The Y ("paradoxical") combinator."""
    return f(lambda: Y(f))


def Y_tester():
    """
    >>> tmp = Y_tester()
    >>> tmp(1)
    1
    >>> tmp(5)
    120
    >>> tmp(2)
    2
    """
    "*** YOUR CODE HERE ***"
 #   return Y(lambda (lambda x: 1 if x==1 else lambda y: sub(y-1)): lambda z:  )  # Replace
 #   return Y(lambda y: lambda x: 1 if x==1 else mul(x, (lambda y: sub(y,1))))
 #    return Y(lambda : lambda y : 1 if y == 1 else mul(y, lambda :sub(y, 1) )) cannot pass one
 #   return Y(lambda x: lambda y : 1 if y == 1 else mul(y, x(sub(y, 1))))  can pass one!
    return Y(lambda x: lambda y : 1 if y == 1 else mul(y, x()(y-1) ))       # x is a function

    
def zero(f):
    return lambda x: x

def successor(n):
    return lambda f: lambda x: f(n(f)(x))
    
def one(f):
    """Church numeral 1: same as successor(zero)"""
    "*** YOUR CODE HERE ***"
    return lambda f: lambda x: f(zero(f)(x))

def my_succer(n):
    return lambda f: successor(n)
    
def two(f):
    """Church numeral 2: same as successor(successor(zero))"""
    "*** YOUR CODE HERE ***"
    return successor(one)

def three(f):
    """Church numeral 1: same as successor(zero)"""
    "*** YOUR CODE HERE ***"
 #   return lambda f: lambda x: f(two(f)(x))
    return successor(two)
three = successor(two)

def church_to_int(n):
    """Convert the Church numeral n to a Python integer.

    >>> church_to_int(zero)
    0
    >>> church_to_int(one)
    1
    >>> church_to_int(two)
    2
    >>> church_to_int(three)
    3
    """
    "*** YOUR CODE HERE ***"
    f = lambda x : x
    if n(f)(0) == zero(f)(0):
        return 0
    else:
        return 1 + church_to_int(n(f))
        
def add_church(m, n):
    """Return the Church numeral for m + n, for Church numerals m and n.

    >>> church_to_int(add_church(two, three))
    5
    """
    "*** YOUR CODE HERE ***"
    interval = church_to_int(n)
    
    def generate_church(init, seg):
        if seg == 0:
            return init
        else:
            return lambda f: successor(generate_church(init, seg-1))
    return generate_church(m, interval)
    
def mul_church(m, n):
    """Return the Church numeral for m * n, for Church numerals m and n.

    >>> four = lambda f: successor(three)
    >>> church_to_int(mul_church(two, three))
    6
    >>> church_to_int(mul_church(three, four))
    12
    """
    "*** YOUR CODE HERE ***"
    ntimes = church_to_int(n)
    def mul_church_f(init, mulpier, times):
        if times == 1:
            return init
        else:
            return add_church(init, mul_church_f(init,mulpier, times-1))
            
    return mul_church_f(m,n, ntimes)
    

def pow_church(m, n):
    """Return the Church numeral m ** n, for Church numerals m and n.

    >>> church_to_int(pow_church(two, three))
    8
    >>> church_to_int(pow_church(three, two))
    9
    """
    "*** YOUR CODE HERE ***"
    npow = church_to_int(n)
    def pow_church(init, mulpier, times):
        if times == 1:
            return init
        else:
            return mul_church(init, pow_church(init,mulpier, times-1))
            
    return pow_church(m,n, npow)
