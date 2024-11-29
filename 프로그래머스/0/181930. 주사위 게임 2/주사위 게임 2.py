def solution(a, b, c):
    # 세 숫자의 합, 제곱의 합, 세제곱의 합을 미리 계산
    score_sum = a + b + c
    score_square = a**2 + b**2 + c**2
    score_cube = a**3 + b**3 + c**3

    # 모든 숫자가 같을 경우
    if a == b == c:
        return score_sum * score_square * score_cube
    # 두 숫자가 같을 경우
    elif a == b or b == c or a == c:
        return score_sum * score_square
    # 모든 숫자가 다를 경우
    else:
        return score_sum

# 예시 실행
print(solution(1, 1, 1))  # 출력: 27 (모두 같음)
print(solution(1, 1, 2))  # 출력: 12 (두 개 같음)
print(solution(1, 2, 3))  # 출력: 6 (모두 다름)