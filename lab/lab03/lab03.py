def even_weighted(s):
    """
    >>> x = [1, 2, 3, 4, 5, 6]
    >>> even_weighted(x)
    [0, 6, 20]
    """
    # Write your code here
    new_list = s[::2]
    result_list = []
    for index in range(len(new_list)):
        new_int = new_list[index] * (index * 2)
        result_list.append(new_int)
    return result_list

def couple(s, t):
    """Return a list of two-element lists in which the i-th element is [s[i], t[i]].

    >>> a = [1, 2, 3]
    >>> b = [4, 5, 6]
    >>> couple(a, b)
    [[1, 4], [2, 5], [3, 6]]
    >>> c = ['c', 6]
    >>> d = ['s', '1']
    >>> couple(c, d)
    [['c', 's'], [6, '1']]
    """
    assert len(s) == len(t)
    # Write your code here
    new_list = []
    for index in range(len(s)):
        new_list.append([s[index], t[index]])
    return new_list


def count_appearances(lst):
    """Returns a dictionary containing each integer's appearance count
    >>> lst = [0]
    >>> count_appearances(lst)
    {0: 1}
    >>> lst = [0, 0, 1, 2, 1, 1]
    >>> count_appearances(lst)
    {0: 2, 1: 3, 2: 1}
    >>> lst = [0, 0, 0, 0, 0, 3, 0, 0]
    >>> count_appearances(lst)
    {0: 7, 3: 1}
    """
    # Write your code here
    dictionary = {i:lst.count(i) for i in lst}
    return dictionary
    # set_list = list((set(lst)))
    # dictionary = {}
    # for index in range(len(set_list)):
    #     dictionary[set_list] = 
    


def copy_file(input_filename, output_filename):
    """Print each line from input with the line number and a colon prepended,
    then write that line to the output file.
    >>> copy_file('text.txt', 'output.txt')
    1: They say you should never eat dirt.
    2: It's not nearly as good as an onion.
    3: It's not as good as the CS pun on my shirt.
    """
    # Write your code here
    input_file = open(input_filename, 'r')
    output_file = open(output_filename, 'w')

    input_lines = input_file.readlines()

    for index in range(len(input_lines)):
        string_line = str(index + 1) + ': ' + str(input_lines[index])
        output_file.write(string_line)

    input_file.close()
    output_file.close()

########################################################
# OPTIONAL QUESTIONS


def factors_list(n):
    """Return a list containing all the numbers that divide `n` evenly, except
    for the number itself. Make sure the list is in ascending order.

    >>> factors_list(6)
    [1, 2, 3]
    >>> factors_list(8)
    [1, 2, 4]
    >>> factors_list(28)
    [1, 2, 4, 7, 14]
    """
    all_factors = []
    # Write your code here


def slice_and_multiplice(lst):
    """Return a new list where all values past the first are
    multiplied by the first value.

    >>> slice_and_multiplice([1,1,6])
    [1, 6]
    >>> slice_and_multiplice([9,1,5,2])
    [9, 45, 18]
    >>> slice_and_multiplice([4])
    []
    >>> slice_and_multiplice([0,4,9,18,20])
    [0, 0, 0, 0]
    """
    # Write your code here
