import re
from pair import *
from operator import add, sub, mul, truediv, pow

def tokenize(expression):
    return re.findall(r'[+-/*()]|\d+(?:\.\d+)?', expression)
        
def parse(tokens):
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
            except ValueError:
                number = tokens[index]
            # 3.3
            next_list, next_index = parse_tokens(tokens, index + 1)
            index = next_index
            # 3.4
            return Pair(number, next_list), index
        
    var_one, var_two = parse_tokens(tokens, 0)
    return var_one

def to_list(operands):
    rest = operands.rest
    list_form = [operands.first]
    while isinstance(rest, Pair):
        list_form.append(rest.first)
        rest = rest.rest
    if rest is not nil:
        list_form.append(rest)
    return list_form

# def reduce_list(func, operand_list):
#     if len(operand_list) == 1:
#         return operand_list[0]
#     else:
#         return func(operand_list[0], reduce_list(func, operand_list[1:]))
    
# def reduce(func, operands, initial):
#     if(operands == nil):
#         return 0
    
#     operand_list = to_list(operands)
    
#     if (initial == None):
#         return reduce_list(func, operand_list)
#     else:
#         operand_list.insert(0, initial)
#         print(operand_list)
#         return reduce_list(func, operand_list)
    
    
    # if(operands == nil):
    #     return 0
    # if (operands.rest == nil):
    #     return operands.first
    # return func(operands.first, reduce(func, operands.rest, initial))
    
    # if(operands == nil):
    #     return 0
    # if (operands.rest == nil):
    #     return operands.first
    # if (initial == None):
    #     return func(operands.first, reduce(func, operands.rest, None))
    # return func(initial, reduce(func, operands, None))

    # if(operands == nil):
    #     return 0
    # if(operands.rest == nil):
    #     return operands.first
    # if(initial == 'Skip'):
    #     return func(operands.first, reduce(func, operands.rest, 'Skip'))
    # return func(initial, reduce(func, operands, 'Skip'))

    # if(operands == nil):
    #      return 0
    # if(operands.rest == nil):
    #     return operands.first
    # if (initial == 'None'):
    #     return func(operands.first, reduce(func, operands.rest, 'None'))
    # if (initial != 'None'):
    #     return func(initial, reduce(func, operands, 'None'))


#     if(operands == nil):
#         return 0
    
#     return func(initial, reduced(func, operands.rest))

# def reduced(func, operands):
#     if(operands == nil):
#         return 0
#     if (operands.rest == nil):
#         return operands.first
#     return func(operands.first, reduced(func, operands.rest))

def reduce(func, operands, initial):
    if(operands == nil):
        return 0
    if(func == sub and operands.rest != nil):
        list = to_list(operands)
        for value in list:
            initial -= value
        return initial
    if(func == pow and operands.rest != nil):
        list = to_list(operands)
        for value in list:
            initial = pow(initial, value)
        return initial
    if(operands.rest == nil):
        return func(initial, operands.first)
    return func(initial, reduce(func, operands.rest, operands.first))

def apply(operator, operands):
    if(operator == '+'):
        return reduce(add, operands, 0)
    elif(operator == '*'):
        return reduce(mul, operands, 1)
    elif(operator == '-'):
        return reduce(sub, operands.rest, operands.first)
    elif(operator == '/'):
        return reduce(truediv, operands.rest, operands.first)
    else:
        raise TypeError
    
def eval(syntax_tree):
    # 1.0
    if(isinstance(syntax_tree, int) or isinstance(syntax_tree, float)):
        return syntax_tree
    # 2.0
    elif(isinstance(syntax_tree, Pair)):
        # 2.1
        if(isinstance(syntax_tree.first, Pair)):
            # 2.1.1
            first = eval(syntax_tree.first)
            # 2.1.2
            rest = syntax_tree.rest.map(eval)
            # 2.1.3
            return Pair(first, rest)
        # 2.2
        if(syntax_tree.first in ['+','-','*','/']):
            # 2.2.1
            result = syntax_tree.rest.map(eval)
            # 2.2.2
            return apply(syntax_tree.first, result)
    else:
        raise TypeError
            
        
       

def main():
    print('Welcome to the CS 111 Calculator Interpreter.')
    
    user_input = ''
    while(user_input != 'exit'):
        user_input = input("calc >> ")
        if(user_input == 'exit'):
            print('Goodbye!')
        else:
            # print(str(parse(tokenize(user_input))))
            try:
                print(eval(parse(tokenize(user_input))))
            except Exception as error:
                print(error)
                
    
    
    
if __name__ == '__main__':
    main()