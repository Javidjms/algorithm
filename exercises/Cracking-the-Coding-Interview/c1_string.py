def reverse_string(string):
    arr_string = list(string)
    start = 0
    end = len(string) - 1
    while start <= end:
        arr_string[start], arr_string[end] = arr_string[end], arr_string[start]
        start += 1
        end -= 1
    return arr_string


