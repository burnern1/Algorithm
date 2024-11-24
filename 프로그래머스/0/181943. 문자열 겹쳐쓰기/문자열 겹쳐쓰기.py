def solution(my_string, overwrite_string, s):
    left_part = my_string[:s]
    right_part = my_string[s + len(overwrite_string):]
    answer = left_part + overwrite_string + right_part
    return answer