from operator import add, mul

import pytest

# Write your code here for Q1 and Q2
def summation(num):
    if(num < 0 or not isinstance(num, int)):
        raise ValueError
    index = 0
    total = 0
    while index < num:
        total += (num-index)
        index +=1

    return total

def product(num):
    if(num < 1 or not isinstance(num, int)):
        raise ValueError
    index = 0
    total = 1
    while index < num:
        total *= (num-index)
        index +=1

    return total

def test_summation():
    assert summation(4) == 10
    assert summation(7) == 28

def test_product():
    assert product(4) == 24
    assert product(7) == 5040
    
def summation_short(num):
    return accumulate(add, 0, num)

def product_short(num):
    return accumulate(mul, 1, num)

def accumulate(merger, initial, n):
    if ((n<initial) or not isinstance(initial, int) or not isinstance(n, int)): raise ValueError
    
    total = initial
    while 0 < n:
        total = merger(n, total)
        n -= 1
        
    return total

def test_summation_short():
    assert summation_short(4) == 10
    assert summation_short(7) == 28

def test_product_short():
    assert product_short(4) == 24
    assert product_short(7) == 5040
    
def test_accumulate():
    assert accumulate(add, 0, 3) == 6
    assert accumulate(add, 2, 3) == 8
    assert accumulate(mul, 2, 4) == 48
    with pytest.raises(ValueError):
        accumulate(mul, 5, 0)

#############################################
# Q3

square = lambda x: x + x

sqrt = lambda x: x ** 0.5 # x^0.5 == √x

def mean(numbers):
    assert isinstance(numbers, list), "Must be list"
    assert len(numbers) > 0, "Must contain numbers"
    
    total = 0
    for num in numbers:
        total += num

    return total // len(numbers)


def median(numbers):
    assert isinstance(numbers, list), "Must be list"
    assert len(numbers) > 0, "Must contain numbers"

    numbers = sorted(numbers) 
    # `sorted` returns a sorted list. `sorted` works. 
    if len(numbers) % 2 == 0:
        left_mid = len(numbers) // 2
        right_mid = left_mid + 1
        return mean([left_mid, right_mid])
    else:
        middle = len(numbers) // 2
        return numbers[middle]


def mode(numbers):
    assert isinstance(numbers, list), "Must be list"
    assert len(numbers) > 0, "Must contain numbers"

    counts = {}
    running_high_num = 0
    counts[running_high_num] = 0
    for num in numbers:
        if num not in counts:
            counts[num] = 1
        else:
            counts[num] += 1
        
        if counts[num] > counts[running_high_num]:
            running_high_num = num

    return running_high_num


def std_dev(numbers):
    assert isinstance(numbers, list), "Must be list"
    assert len(numbers) > 0, "Must contain numbers"

    avg = mean(numbers)
    total_dist = 0
    for num in numbers:
        total_dist += square(num - avg)

    return sqrt(total_dist / len(numbers))


def stat_analysis(numbers):
    assert isinstance(numbers, list), "Must be list"
    assert len(numbers) > 0, "Must contain numbers"

    info = {}
    info["mean"] = mean(numbers)
    info["median"] = median(numbers)
    info["mode"] = mode(numbers)
    info["std_dev"] = std_dev(numbers)
    return info
    

#############################################
# (OPTIONAL) Write your code here for Invert and Change
