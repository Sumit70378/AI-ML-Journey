nums = [1, 2, 3, 2, 4, 1, 2, 5, 3, 1]
mark = {}
mark = {}

for i in nums:
    mark[i] = mark.get(i, 0) + 1

print(mark)
