from functools import reduce

def solution(num_list):
    # 모든 원소의 곱 계산
    product = reduce(lambda x, y: x * y, num_list)
    
    # 모든 원소의 합 계산 후 제곱
    sum_of_elements = sum(num_list)
    square_of_sum = sum_of_elements ** 2
    
    # 비교하여 결과 반환
    return 1 if product < square_of_sum else 0

# 예시 실행
print(solution([3, 4, 5, 2, 1]))  # 출력: 1
print(solution([5, 7, 8, 3]))     # 출력: 0