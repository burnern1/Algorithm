def solution(d, budget):
    d.sort()
    total = 0
    count = 0
    for amount in d:
        if total + amount > budget:
            break
        total += amount
        count += 1
    return count