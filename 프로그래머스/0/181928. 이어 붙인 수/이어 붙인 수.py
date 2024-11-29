def solution(num_list):
    # 홀수와 짝수를 각각 문자열로 이어 붙입니다.
    odd_numbers = ''.join(str(num) for num in num_list if num % 2 != 0)
    even_numbers = ''.join(str(num) for num in num_list if num % 2 == 0)
    
    # 이어 붙인 문자열을 정수로 변환합니다.
    odd_value = int(odd_numbers)
    even_value = int(even_numbers)
    
    # 두 정수의 합을 반환합니다.
    return odd_value + even_value

# 예시 실행
print(solution([3, 4, 5, 2, 1]))  # 출력: 393
print(solution([5, 7, 8, 3]))     # 출력: 581