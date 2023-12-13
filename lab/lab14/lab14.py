import math
from copy import deepcopy

def convert_link(link):
    """Takes a linked list and returns a Python list with the same elements.

    >>> link = Link(1, Link(2, Link(3, Link(4))))
    >>> convert_link(link)
    [1, 2, 3, 4]
    >>> convert_link(Link.empty)
    []
    """
    # Write your code here
    listy = []
    if link is Link.empty:
        return listy
    
    while link is not Link.empty:
        listy.append(link.first)
        link = link.rest
        
    return listy


def store_digits(n):
    """Stores the digits of a positive number n in a linked list.

    >>> s = store_digits(1)
    >>> s
    Link(1)
    >>> store_digits(2345)
    Link(2, Link(3, Link(4, Link(5))))
    >>> store_digits(876)
    Link(8, Link(7, Link(6)))
    """
    listy = []
    iterative_n = n
    while(iterative_n > 0):
        listy.append(iterative_n % 10)
        iterative_n = iterative_n // 10

    listy.reverse()
    return store_helper(listy)
    
def store_helper(listy):
    if len(listy) == 1:
        return Link(listy[0])
    else:  
        return Link(listy[0], store_helper(listy[1:]))

def every_other(link):
    """Mutates a linked list so that all the odd-indexed elements are removed
    (using 0-based indexing).

    >>> s = Link(1, Link(2, Link(3, Link(4))))
    >>> every_other(s)
    >>> s
    Link(1, Link(3))
    >>> odd_length = Link(5, Link(3, Link(1)))
    >>> every_other(odd_length)
    >>> odd_length
    Link(5, Link(1))
    >>> singleton = Link(4)
    >>> every_other(singleton)
    >>> singleton
    Link(4)
    """
    # Write your code here
    if link is Link.empty:
        return None
    
    string = str(link)
    string = string[1:len(string)-1]
    string = string.replace(" ", "")
    
    count = 0
    new_string = ''
    while (count < len(string)):
        new_string += string[count]
        count += 2
    number = int(new_string)
    linked = store_digits(number)
    print(linked)
    return linked
        
    # link_list = convert_link(link)
    # print(link_list)
    # count = 0
    # new_list = []
    # while (count < len(link_list)):
    #     new_list.append(link_list[count])
        
    #     count += 2
    # print(new_list)
    # stringy = ''
    # for item in new_list:
    #     stringy += str(item)
    # stringy = int(stringy)
    # print(stringy)
    # link2 = store_digits(stringy)
    
    # return link2
    

def deep_map_mut(fn, link):
    """Mutates a deep link by replacing each item found with the
    result of calling fn on the item.  Does NOT create new Links (so
    no use of Link's constructor)

    Does not return the modified Link object.

    >>> link1 = Link(3, Link(Link(4), Link(5, Link(6))))
    >>> deep_map_mut(lambda x: x * x, link1)
    >>> link1
    Link(9, Link(Link(16), Link(25, Link(36))))
    """
    # Write your code here


class Link:

    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(
            rest, Link), "Link does not follow proper structure"
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest is not Link.empty:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'
