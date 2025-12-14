arr = list(map(int, input().split()))

max_sum = arr[0]
curr = arr[0]

for x in arr[1:]:
    curr = max(x, curr + x)
    max_sum = max(max_sum, curr)

print(max_sum)
