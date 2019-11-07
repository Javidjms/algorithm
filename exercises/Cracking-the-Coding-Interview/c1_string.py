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


