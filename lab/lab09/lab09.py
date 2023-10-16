import random


def in_range1(input):
    """Write a function that checks to see if input is 
    within the range of 1-100 and have it return False if not
    >>> in_range1(9)
    True
    >>> in_range1(-4)
    False
    """
    "*** YOUR CODE HERE ***"
    return (0 < input <= 100)


def main():
    """Write code in the main function that generates 1000 
    random numbers between 1 and 101 and calls the generated 
    function to validate the number generated."""
    "*** YOUR CODE HERE ***"
    for number in range(100):
        rand_num = random.randint(1,101)
        in_range1(rand_num)


def in_range2(input):
    """Redo in_range1, but throw an exception instead of 
    throwing false
    """
    "*** YOUR CODE HERE ***"
    if (not (0 < input <= 100)):
        raise ValueError
