# For Perfect Number
n = int(input())
total = 0

for i in range(1, n):
    if n % i == 0:
        total += i

print("Perfect" if total == n else "Not perfect")
