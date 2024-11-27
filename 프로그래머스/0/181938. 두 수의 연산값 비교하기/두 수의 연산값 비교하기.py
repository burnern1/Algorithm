def solution(a, b):
    answer = 0
    str1 = str(a) + str(b)
    str2 = 2 * a * b

    if (int(str1) >= str2):
        answer = int(str1)
    else:
        answer = str2

    return answer