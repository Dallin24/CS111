import re
from pair import *

def tokenize(expression):
    return re.findall(r'[+-/*()]|\d+(?:\.\d+)?', expression)

def parse_tokens(tokens, index):
    if(re.search(r'[A-Za-z]', str(tokens))):
        raise TypeError
    
    try:
        tokens[index]
    except IndexError:
        return nil
    if(tokens[index] == '(' and index == 0): 
        return (Pair(tokens[index + 1], parse_tokens(tokens, index + 2)), len(tokens))
    if(tokens[index] == '('):
            next_open = tokens[index:].index('(')
            next_close = tokens[index:].index(')')
            while(next_open < next_close):
                next_close = tokens[next_open:].index(')')
            short_list = tokens[index:next_close]
            print(index)
            print(tokens[index:])
            print(next_close)
            return Pair(parse_tokens(tokens, index + len(short_list)), parse_tokens(short_list, index))
    elif(tokens[index] == ')'):
        return nil
    else:
        try:
            converted_int_token = int(tokens[index])
            converted_float_token = float(tokens[index])
            if(converted_float_token-converted_int_token != 0):
                return Pair(converted_float_token, parse_tokens(tokens, index + 1))
            else:
                return Pair(converted_int_token, parse_tokens(tokens, index + 1))
        except ValueError:
             return Pair(tokens[index], parse_tokens(tokens, index + 1))