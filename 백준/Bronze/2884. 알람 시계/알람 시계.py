def calculate_new_alarm(H, M):
    # 분 단위가 45 이상인 경우 단순히 45분을 뺍니다.
    if M >= 45:
        return H, M - 45
    else:
        # 분 단위가 45 미만인 경우, 한 시간을 줄이고 분에 60을 더해 계산합니다.
        new_M = M - 45 + 60
        new_H = H - 1 if H > 0 else 23
        return new_H, new_M

# 사용자 입력을 받습니다.
H, M = map(int, input().split())

# 결과를 계산하고 출력합니다.
new_H, new_M = calculate_new_alarm(H, M)
print(new_H, new_M)