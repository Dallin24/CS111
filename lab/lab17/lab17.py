import re
from pair import *
import doctest

def tokenize(expression):
    """ Takes a string and returns a list where each item
    in the list is a parenthesis, one of the four operators (/, *, -, +),
    or a number literal.
    >>> tokenize("(+ 3 2)")
    ['(', '+', '3', '2', ')']
    >>> tokenize("(- 9 3 3)")
    ['(', '-', '9', '3', '3', ')']
    >>> tokenize("(+ 10 100)")
    ['(', '+', '10', '100', ')']
    >>> tokenize("(+ 5.5 10.5)")
    ['(', '+', '5.5', '10.5', ')']
    >>> expr = "(* (- 8 4) 4)"
    >>> tokenize(expr)
    ['(', '*', '(', '-', '8', '4', ')', '4', ')']
    >>> expr = "(* (- 6 8) (/ 18 3) (+ 10 1 2))"
    >>> tokenize(expr)
    ['(', '*', '(', '-', '6', '8', ')', '(', '/', '18', '3', ')', '(', '+', '10', '1', '2', ')', ')']
    """
    # Write your code here
    return re.findall(r'[+-/*()]|\d+(?:\.\d+)?', expression)



# OPTIONAL
def parse_tokens(tokens, index):
    """ Takes a list of tokens and an index and converts the tokens to a Pair list

    >>> parse_tokens(['(', '+', '1', '1', ')'], 0)
    (Pair('+', Pair(1, Pair(1, nil))), 5)
    >>> parse_tokens(['(', '*', '(', '-', '8', '4', ')', '4', ')'], 0)
    (Pair('*', Pair(Pair('-', Pair(8, Pair(4, nil))), Pair(4, nil))), 9)
    """
    # Write your code here
    if(index >= len(tokens)):
        return nil
    if(tokens[index] == '(' and index == 0): 
        return (Pair(tokens[index + 1], parse_tokens(tokens, index + 2)), len(tokens))
    if(tokens[index] == '('): 
        next_close = tokens.index(')')
        short_list = tokens[index-1:next_close]
        return Pair(parse_tokens(short_list, index), parse_tokens(tokens, index + len(short_list)))
    elif(tokens[index] == ')'):
        return nil
    else:
        try:
            converted_token = int(tokens[index])
            return Pair(converted_token, parse_tokens(tokens, index + 1))
        except ValueError:
             return Pair(tokens[index], parse_tokens(tokens, index + 1))
        
    
doctest.testmod()