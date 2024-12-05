def calculate_end_time(A, B, C):
    # 현재 시각을 분 단위로 변환
    start_minutes = A * 60 + B
    # 요리 시간을 더함
    end_minutes = start_minutes + C
    
    # 24시간 형식으로 변환
    end_hour = (end_minutes // 60) % 24
    end_minute = end_minutes % 60
    
    return end_hour, end_minute

# 사용자 입력을 받습니다.
A, B = map(int, input().split())
C = int(input())

# 결과를 계산하고 출력합니다.
end_hour, end_minute = calculate_end_time(A, B, C)
print(end_hour, end_minute)