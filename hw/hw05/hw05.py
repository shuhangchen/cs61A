# Linked List Class
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
        """
        return 1 + len(self.rest)

    def __getitem__(self, i):
        """Returning the element found at index i.

        >>> s = Link(1, Link(2, Link(3)))
        >>> s[1]
        2
        >>> s[2]
        3
        """
        if i == 0:
            return self.first
        else:
            return self.rest[i-1]

def print_link(link):
    """Print elements of a linked list link.

    >>> link = Link(1, Link(2, Link(3)))
    >>> print_link(link)
    <1 2 3>
    >>> link1 = Link(1, Link(Link(2), Link(3)))
    >>> print_link(link1)
    <1 <2> 3>
    >>> link1 = Link(3, Link(Link(4), Link(5, Link(6))))
    >>> print_link(link1)
    <3 <4> 5 6>
    """
    print('<' + helper(link).rstrip() + '>')

def helper(link):
    if link == Link.empty:
        return ''
    elif isinstance(link.first, Link):
        return '<' + helper(link.first).rstrip() + '> ' + helper(link.rest)
    else:
        return str(link.first) +' '+  helper(link.rest)

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

# Tree definition
class BinTree:
    empty = ()

    def __init__(self, label, left=empty, right=empty):
        self.label = label
        self.left = left
        self.right = right

    def __repr__(self):
        if self.left == self.empty and self.right == self.empty:
            return 'BinTree({})'.format(repr(self.label))
        left = 'BinTree.empty' if self.left == self.empty else repr(self.left)
        right = 'BinTree.empty' if self.right == self.empty else repr(self.right)
        return 'BinTree({}, {}, {})'.format(repr(self.label), left, right)

def binTree(tupleTree):
    """A convenience method for succinctly constructing binary trees.  The
    empty tuple or list stands for BinTree.empty; (V,) or [V] stands
    for BinTree(V); (V, T1, T2) or [V, T1, T2] stands for
    BinTree(V, binTree(T1), binTree(T2)).
    >>> binTree((3,
    ...          (1, (), [2]),
    ...          (6, [5], [7])))
    BinTree(3, BinTree(1, BinTree.empty, BinTree(2)), BinTree(6, BinTree(5), BinTree(7)))
    """
    if len(tupleTree) == 0:
        return BinTree.empty
    elif len(tupleTree) == 1:
        return BinTree(tupleTree[0])
    else:
        return BinTree(tupleTree[0], binTree(tupleTree[1]), binTree(tupleTree[2]))

###########################################################
# Tree printing functions, kindly provided by Joseph Hui. #
# You do not need to look at these.                       #
###########################################################

def print_bintree(tree):
    print(tree_string(tree))

def tree_string(tree):
    return "\n".join(tree_block(tree)[0])

def tree_block(tree):
    r"""Returns a list of strings, each string being
    one line in a rectangle of text representing the
    tree.
    Also returns the index in the string which is
    centered above the tree's root.

    num_width: The width of the widest number in the tree (100 => 3)
    >>> print(tree_string(binTree( (1, (3, (), [2]), (4, [5], [6])) )))
     -1-
    /   \
    3   4
     \ / \
     2 5 6
    """
    #If no children, just return string
    empty = BinTree.empty
    if tree.left is empty and tree.right is empty:
        return [str(tree.label)], len(str(tree.label))//2
    num_width = len(str(tree.label)) #Width of this tree's label
    #If only right child:
    if tree.left is empty:
        r_block, r_cent = tree_block(tree.right)
        #Add left padding if necessary
        if r_cent < num_width*3/2:
            padding = ' '*((num_width*3)//2-r_cent)
            r_cent += ((num_width*3)//2-r_cent) #Record new center
            for line_index in range(len(r_block)):
                r_block[line_index] = padding+r_block[line_index]

        #Generate top two lines
        t_line = str(tree.label)
        t_line += '-'*(r_cent-len(t_line))
        t_line += ' '*(len(r_block[0])-len(t_line))
        m_line = ' '*r_cent + '\\'
        m_line += ' '*(len(r_block[0])-len(m_line))

        return [t_line, m_line]+r_block, num_width//2
    #If only left child:
    if tree.right is empty:
        l_block, l_cent = tree_block(tree.left)
        #Add right padding if necessary
        if len(l_block[0]) < l_cent+1+num_width:
            padding = ' '*(l_cent+1+num_width-len(l_block[0]))
            for line_index in range(len(l_block)):
                l_block[line_index] = l_block[line_index]+padding
        #Generate lines
        t_line = ' '*(l_cent+1)
        t_line += '-'*(len(l_block[0])-l_cent-1-num_width)
        t_line += str(tree.label)
        m_line = ' '*l_cent+'/'
        m_line += ' '*(len(l_block[0]) - len(m_line))
        return [t_line, m_line]+l_block, len(t_line)-num_width//2
    #Otherwise, has both
    l_block, l_cent = tree_block(tree.left)
    r_block, r_cent = tree_block(tree.right)

    #Pad left block
    spacing = r_cent+len(l_block)-l_cent-2
    padding = ' '*max(1, (spacing-num_width))
    for line_index in range(len(l_block)):
        l_block[line_index] = l_block[line_index]+padding

    #Add left and right blocks
    new_block = []
    for line_index in range(max(len(l_block), len(r_block))):
        new_line = l_block[line_index] if line_index < len(l_block) else ' '*len(l_block[0])
        new_line += r_block[line_index] if line_index < len(r_block) else ' '*len(r_block[0])
        new_block.append(new_line)
    r_cent += len(l_block[0])

    #Generate top lines
    my_cent = (l_cent+r_cent)//2
    t_line = ' '*(l_cent+1)
    t_line += '-'*(my_cent-num_width//2-len(t_line))
    t_line += str(tree.label)
    t_line += '-'*(r_cent-len(t_line))
    t_line += ' '*(len(new_block[0])-len(t_line))

    m_line = ' '*l_cent + '/'
    m_line += ' '*(r_cent-len(m_line)) + '\\'
    m_line += ' '*(len(new_block[0])-len(m_line))

    return [t_line, m_line]+new_block, my_cent

import time

def timeit(func):
    """Returns the time required to execute FUNC() in seconds."""
    t0 = time.perf_counter()
    func()
    return time.perf_counter() - t0

# Q1
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
    "*** YOUR CODE HERE ***"
    if t.is_leaf():
        return t
    else:
        branches = []
        for child in t.children:
            branches += [cumulative_sum(child)]
        entry = t.label
        for new_child in branches:
            entry += new_child.label
        return Tree(entry, branches)
# Q2
def link_to_list(link):
    """Takes a Link and returns a Python list with the same elements.

    >>> link = Link(1, Link(2, Link(3, Link(4))))
    >>> link_to_list(link)
    [1, 2, 3, 4]
    >>> link_to_list(Link.empty)
    []
    """
    "*** YOUR CODE HERE ***"
    if link is Link.empty:
        return []
    else:
        return [link.first] + link_to_list(link.rest)
# Q3
def append_link_list(link, elem):
    """returns a linked list with elem as its last element"""
    if link.rest is Link.empty:
        return Link(link.first, Link(elem))
    else:
        return Link(link.first, append_link_list(link.rest, elem))

        
def reverse(link):
    """Returns a Link that is the reverse of the original.

    >>> print_link(reverse(Link(1)))
    <1>
    >>> link = Link(1, Link(2, Link(3)))
    >>> new = reverse(link)
    >>> print_link(new)
    <3 2 1>
    >>> print_link(link)
    <1 2 3>
    """
    "*** YOUR CODE HERE ***"
    if link.rest is Link.empty:
        return link
    else:
        return append_link_list(reverse(link.rest), link.first)

        
# Q4
def has_cycle(link):
    """Return whether link contains a cycle.

    >>> s = Link(1, Link(2, Link(3)))
    >>> s.rest.rest.rest = s
    >>> has_cycle(s)
    True
    >>> t = Link(1, Link(2, Link(3)))
    >>> has_cycle(t)
    False
    >>> u = Link(2, Link(2, Link(2)))
    >>> has_cycle(u)
    False
    """
    "*** YOUR CODE HERE ***"
    q = t =link
    while  q.rest is not Link.empty:
        if q.rest is link:
            return True
        else:
            q = q.rest
    return False
        
def has_cycle_constant(link):
    """Return whether link contains a cycle.

    >>> s = Link(1, Link(2, Link(3)))
    >>> s.rest.rest.rest = s
    >>> has_cycle_constant(s)
    True
    >>> t = Link(1, Link(2, Link(3)))
    >>> has_cycle_constant(t)
    False
    """
    "*** YOUR CODE HERE ***"
    q = t =link
    while  q.rest is not Link.empty:
        if q.rest is link:
            return True
        else:
            q = q.rest
    return False

# Q5
def bst_min(b):
    r""" Returns the min of all the values of each node in b.

    Calling bst_min on the following tree should return 1:

            4
           / \
          2   6
         /   /
        1   5

    >>> t1 = binTree([4, [2, [1], []], [6, [5], []]])
    >>> bst_min(t1)
    1
    >>> t2 = binTree([4])
    >>> bst_min(t2)
    4
    >>> t3 = binTree([4, [2], []])
    >>> bst_min(t3)
    2
    >>> t4 = binTree([4, [], [6]])
    >>> bst_min(t4)
    4
    >>> t5 = binTree([9, [6, [5], [7]], []])
    >>> bst_min(t5)
    5
    >>> # Illegal BST, but if your solution is right, it should NOT
    >>> # print 100.
    >>> t6 = binTree([9, [6, [5], [7]], [-100]])
    >>> bst_min(t6)
    5
    """
    "*** YOUR CODE HERE ***"
    if b.left is BinTree.empty:
        return b.label
    else:
        return bst_min(b.left)

# Q6
def bst_max(b):
    """ Returns the max of all the labels in B, assuming B is a BST.

    Calling bst_max on the following tree should return 6:

            4
           / \
          2   6
         /   /
        1   5

    >>> t1 = binTree([4, [2, [1], []], [6, [5], []]])
    >>> bst_max(t1)
    6
    >>> t2 = binTree([4])
    >>> bst_max(t2)
    4
    >>> t3 = binTree([4, [2], []])
    >>> bst_max(t3)
    4
    >>> t4 = binTree([4, [], [6]])
    >>> bst_max(t4)
    6
    >>> t5 = binTree([4, [], [6, [5], [7]]])
    >>> bst_max(t5)
    7
    >>> # Illegal BST, but if your solution is right, it should NOT
    >>> # print 100.
    >>> t6 = binTree([4, [100], [6, [5], [7]]])
    >>> bst_max(t6)
    7
    """
    "*** YOUR CODE HERE ***"
    if b.right is BinTree.empty:
        return b.label
    else:
        return bst_max(b.right)

# Q7
def is_valid_bst(bst):
    """
    >>> t1 = binTree([4, [2, [1], []], [6, [5], []]])
    >>> is_valid_bst(t1)
    True
    >>> t2 = binTree([4, [100], [6, [5], [7]]])
    >>> is_valid_bst(t2)
    False
    >>> t3 = binTree([6, [5, [3, [1], [4]], [7]], [8, [7], [9]]])
    >>> is_valid_bst(t3)
    False
    >>> t4 = binTree([1])
    >>> is_valid_bst(t4)
    True
    >>> t5 = binTree([6, [5, [3, [4], [1]], []], [8, [7], [9]]])
    >>> is_valid_bst(t5)
    False
    >>> is_valid_bst(BinTree.empty)
    True
    """
    "*** YOUR CODE HERE ***"
    if bst is BinTree.empty:
        return True
    elif bst.right is BinTree.empty and bst.left is BinTree.empty:
        return True
    elif bst.right is BinTree.empty or bst.left is BinTree.empty:
        return (bst.label <= bst_min(bst.right) and is_valid_bst(bst.right)) if bst.left is BinTree.empty else (bst.label >= bst_max(bst.left) and is_valid_bst(bst.left))
    else:
        return bst.label <= bst_min(bst.right) and bst.label >= bst_max(bst.left) and is_valid_bst(bst.left) and is_valid_bst(bst.right)

# Q8
def add_up(n, lst):
    """Returns True if any two non identical elements in lst add up to n.

    >>> add_up(100, [1, 2, 3, 4, 5])
    False
    >>> add_up(7, [1, 2, 3, 4, 2])
    True
    >>> add_up(10, [5, 5])
    False
    >>> add_up(151, range(0, 200000, 2))
    False
    >>> timeit(lambda: add_up(151, range(0, 200000, 2))) < 1.0
    True
    >>> add_up(50002, range(0, 200000, 2))
    True
    """
    "*** YOUR CODE HERE ***"
    # below is the recursive version
    # def add_up_with_set(n, lst, cset):
    #     if lst == []:
    #         return False
    #     elif lst[0] in cset:
    #         if lst[0] + lst[0] == n:
    #             return add_up_with_set(n, lst[1:], cset)
    #         else:
    #             return True
    #     elif len(lst) == 1:
    #         return False
    #     else:
    #         cset.update([n-lst[0]])
    #         return add_up_with_set(n, lst[1:], cset )

    # return add_up_with_set(n, lst, set({}))
    cset =set([])
    for elem in lst:
        if elem in cset:
            if elem + elem != n:
                return True
        else:
            cset.update([n-elem])

    return False
# Q9
def missing_val(lst0, lst1):
    """Assuming that LST0 contains all the values in LST1, but LST1 is missing
    one value in LST0, return the missing value.  The values need not be
    numbers.

    >>> from random import shuffle
    >>> missing_val(range(10), [1, 0, 4, 5, 7, 9, 2, 6, 3])
    8
    >>> big0 = [str(k) for k in range(15000)]
    >>> big1 = [str(k) for k in range(15000) if k != 293 ]
    >>> shuffle(big0)
    >>> shuffle(big1)
    >>> missing_val(big0, big1)
    '293'
    >>> timeit(lambda: missing_val(big0, big1)) < 1.0
    True
    """
    "*** YOUR CODE HERE ***"
    set0 = set(lst0)
    set1 = set(lst1)
    return set.union(set0, set1).difference(set1).pop()


