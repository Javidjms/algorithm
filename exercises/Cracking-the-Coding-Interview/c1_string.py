def reverse_string(string):
    arr_string = list(string)
    start = 0
    end = len(string) - 1
    while start <= end:
        arr_string[start], arr_string[end] = arr_string[end], arr_string[start]
        start += 1
        end -= 1
    return arr_string


def is_unique_chars(string):
    if len(string) > 128:
        return False

    char_set = [False for i in range(128)]

    for char in string:
        val = ord(char)
        if char_set[val]:
            return False
        char_set[val] = True
    return True


def is_unique_chars_with_hash_map(string):
    char_dict = {}

    for char in string:
        if char in char_dict:
            return False
        char_dict[char] = True

    return True


def is_unique_chars_with_sort(string):
    sorted_string = sorted(string)

    for i in range(1, len(string)):
        if sorted_string[i-1] == sorted_string[i]:
            return False
    return True


def check_is_permutation(first_string, second_string):
    if len(first_string) != len(second_string):
        return False
    return sorted(first_string) == sorted(second_string)


def check_is_permutation_optimal(first_string, second_string):
    if len(first_string) != len(second_string):
        return False

    char_set = [0 for i in range(128)]

    for char in first_string:
        val = ord(char)
        char_set[val] += 1

    for char in first_string:
        val = ord(char)
        char_set[val] -= 1
        if char_set[val] < 0:
            return False

    return True


def urlify(string, length):
    array_string = list(string)
    sparse_count = 0

    for i in range(length):
        char = array_string[i]
        if char == ' ':
            sparse_count += 1
    index = length + sparse_count * 2

    for i in range(length-1, -1, -1):
        char = array_string[i]
        if char == ' ':
            array_string[index-3:index] = '%20'
            index -= 3
        else:
            array_string[index-1] = array_string[i]
            index -= 1

    return ''.join(array_string)


