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


def is_permutation_of_palindrome(string):
    count_odd = 0
    table = [0 for i in range(128)]

    for char in string:
        value = ord(char)
        table[value] += 1
        if table[value] % 2 == 1:
            count_odd += 1
        else:
            count_odd -= 1
    return count_odd <= 1


def one_edit_away(first_string, second_string):
    if len(first_string) == len(second_string):
        return one_edit_replace(first_string, second_string)
    elif (len(first_string) + 1) == len(second_string):
        return one_edit_insert(first_string, second_string)
    elif first_string == (len(second_string) + 1):
        return one_edit_insert(second_string, first_string)
    return False


def one_edit_replace(first_string, second_string):
    found_difference = False
    for index in range(0, len(first_string)):
        if first_string[index] != second_string[index]:
            if found_difference:
                return False
            found_difference = True
    return True


def one_edit_insert(first_string, second_string):
    index1 = 0
    index2 = 0

    while index1 < len(first_string) and index2 < len(second_string):
        if first_string[index1] != second_string[index2]:
            if index1 != index2:
                return False
            index2 += 1
        else:
            index1 += 1
            index2 += 1
    return True


def string_compression(string):
    counter = 0
    compressed = []
    array_string = list(string)

    for i in range(len(array_string)):
        if i != 0 and array_string[i] != array_string[i - 1]:
            compressed.append(array_string[i - 1] + str(counter))
            counter = 0
        counter += 1

    if len(array_string):
        compressed.append(array_string[-1] + str(counter))

    return min(''.join(array_string), ''.join(compressed), key=len)


def rotate_matrix(matrix):
    n = len(matrix)
    for layer in range(n // 2):
        first, last = layer, n - layer - 1
        for i in range(first, last):
            top = matrix[layer][i]

            matrix[layer][i] = matrix[-i - 1][layer]
            matrix[-i - 1][layer] = matrix[-layer - 1][-i - 1]
            matrix[-layer - 1][-i - 1] = matrix[i][- layer - 1]
            matrix[i][- layer - 1] = top
    return matrix


