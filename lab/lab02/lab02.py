"""What would Python Display
    >>> True and 13
    13
    >>> False or 0
    0
    >>> not 10
    False
    >>> not None
    True

    >>> True and 1 / 0 and False
    Error
    >>> True or 1 / 0 or False
    True
    >>> True and 0
    0
    >>> False or 1
    1
    >>> 1 and 3 and 6 and 10 and 15
    15
    >>> -1 and 1 > 0
    True
    >>> 0 or False or 2 or 1 / 0
    2

    >>> not 0
    True
    >>> (1 + 1) and 1
    1
    >>> 1/0 or True
    Error
    >>> (True or False) and False
    False

    """
    

def func(a, b):
    """Test func
    >>> func(10, 6)
    5
    >>> func(4, 6)
    6
    >>> func(0, 3)
    10
    """
    if a == 4:
        return 6
    elif b % 2 == 0:
        return a // 2
    else:
        return 3 * b + 1
    

def how_big(x):
    """ How Big
    >>> how_big(7)
    'big'
    >>> how_big(12)
    huge
    >>> how_big(-1)
    nothing
    """
    if x > 10:
        print('huge')
    elif x > 5:
        return 'big'
    elif x > 0:
        print('small')
    else:
        print("nothing")

def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    "*** YOUR CODE HERE ***"
    if(k == 0):
        return 1
    
    result = n
    count = 0
    while(count < k - 1):
        result*=(n - 1)
        count+=1
        n-=1
    return result
    

def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    "*** YOUR CODE HERE ***"
    repeatNum = len(str(y))

    index = 0
    total = 0
    while(index < repeatNum):
        total += int(str(y)[index])
        index+=1
    return total


###################################################
# Code below here is for extra practice and doesn't count for or against
# your grade on this lab.
def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"
