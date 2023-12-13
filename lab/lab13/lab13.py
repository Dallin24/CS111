import math

def skip_mul(n):
    """Return the product of n * (n - 2) * (n - 4) * ...

    >>> skip_mul(5) # 5 * 3 * 1
    15
    >>> skip_mul(8) # 8 * 6 * 4 * 2
    384
    """
    if n == 2 or n == 1:
        return n * 1
    else:
        return n * skip_mul(n - 2)


def multiply(m, n):
    """ Takes two positive integers and returns their product using recursion.
    >>> multiply(5, 3)
    15
    """
    "*** YOUR CODE HERE ***"
    if (n == 0):
        return 0
    else:
        return m + multiply(m, n - 1)


def is_prime(n):
    """Returns True if n is a prime number and False otherwise.

    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    "*** YOUR CODE HERE ***"
    if n == 1:
        return False
    if n == 2:
        return True
    
    for i in range(2, math.floor(math.sqrt(n)) + 1):
        if is_prime(i):
            if n % i == 0:
                return False
            
    return True