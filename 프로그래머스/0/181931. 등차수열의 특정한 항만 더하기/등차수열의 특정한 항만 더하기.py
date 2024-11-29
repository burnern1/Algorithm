def solution(a, d, included):
    total_sum = 0
    # included 배열의 길이만큼 반복
    for i in range(len(included)):
        if included[i]:  # 해당 항이 포함되는 경우
            term = a + i * d  # i번째 항 계산 (0-based index)
            total_sum += term  # 합산
    return total_sum

# 예시 실행
a = 3
d = 4
included = [True, False, False, True, True]
result = solution(a, d, included)
print(result)  # 출력: 37