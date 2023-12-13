import re
from pair import *

def tokenize(expression):
    return re.findall(r'[+-/*()]|\d+(?:\.\d+)?', expression)

def parse_tokens(tokens, index):
    # Invalid Tokens
    if(re.search(r'[A-Za-z]', str(tokens))):
        raise TypeError
    
    # 1.0
    if(tokens[index] == '('):
        # 1.1
        operator = tokens[index + 1]
        # 1.2
        if(index != 0):
            # 1.2.1
            sub_list, sub_index = parse_tokens(tokens, index + 2)
            index = sub_index
            # 1.2.2
            operator = Pair(operator, sub_list)
        # 1.3
        elif(index == 0):
            index += 2
        # 1.4
        next_list, next_index = parse_tokens(tokens, index)
        index = next_index
        # 1.5
        return Pair(operator, next_list), index
    # 2.0
    elif(tokens[index] == ')'):
        return nil, index + 1
    # 3.0
    else:
        number = 0
        try:
            # 3.1
            if('.' in tokens[index]):
                number = float(tokens[index])
            # 3.2
            else:
                number = int(tokens[index])
        except TypeError:
            number = tokens[index]
        # 3.3
        next_list, next_index = parse_tokens(tokens, index + 1)
        index = next_index
        # 3.4
        return Pair(number, next_list), index
        
        
        