# p.99 1이 될 때까지

n, k = 25, 5    # map(int, input().split())
result = 0

while n >= k:
    # n이 k로 나눠지지 않으면 '1'빼기
    while n % k != 0:
        n -= 1
        result += 1
    
    # k로 나누기
    n = n // k  # n //= k
    result += 1

# 마지막으로 남은 수
while n > 1:
    n -= 1
    result += 1

print(result)