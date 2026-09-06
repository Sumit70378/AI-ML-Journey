nums = [10, 5, 20, 8, 20, 15]
second_largest = 0
max = 0

for i in nums:
    if max<i:
        second_largest=max
        max=i
    elif second_largest<i and i < max:
        second_largest=i

print(second_largest)
print(max)