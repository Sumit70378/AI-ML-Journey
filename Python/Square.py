nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nums2 = []

for i in nums:
    if i % 2 == 0 and i*i > 20:
        nums2.append(i * i)
       

print(nums2)