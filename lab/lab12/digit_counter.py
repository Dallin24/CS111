def digit_counter(func, num):
    """Return the number of digits when func(num) is true"""
    counter = 0

    while num > 0:
        print(f'DEBUG: num is {num}')
        if func(num % 10):
            counter += 1
            
            
        num = num // 10
        print(f'DEBUG: counter is {counter}')
        
    return counter


# Function to test with
def is_even(x):
    return x % 2 == 0


"""ADD_TESTING_CODE"""
def main():
    print(f'DEBUG: is_even(5) = {is_even(5)}')
    print(f'DEBUG: is_even(340) = {is_even(340)}')
    print(f'DEBUG: is_even(12303) = {is_even(12303)}')
    print(f'DEBUG: is_even(857) = {is_even(857)}')
    print(f'DEBUG: is_even(948) = {is_even(948)}')
    print(f'DEBUG: RESULT: {digit_counter(is_even, 59)}')
    print(f'DEBUG: RESULT: {digit_counter(is_even, 5234)}')
    print(f'DEBUG: RESULT: {digit_counter(is_even, 526742)}')
    print(f'DEBUG: RESULT: {digit_counter(is_even, 4720573)}')

if __name__ == '__main__':
    main()