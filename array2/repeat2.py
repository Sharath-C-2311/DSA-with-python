# an element can only occur for 2 or less than 2 times 
# elements are given in sorted order

nums = [int(i) for i in input().split()]

#brute force method that came to my mind without using inbuilt function .count() 

maxel = max(nums)+1
p1 = 0
p2= 1
n = 0
while(p2 < len(nums)):
    print(p2,p1, "nums : ",nums[p1],nums[p2])
    if nums[p1] == nums[p2]:
        p2+=1
    else:
        print(nums[p1],nums[p2])
        if p2-p1 > 1:
            for k in range(p1+2,p2):
                n+=1
                nums[k] = maxel
        p1 = p2
        p2+=1

if p2-p1 > 2:
    for k in range(p1+2,p2):
        n+=1
        nums[k] = maxel

nums.sort()

print(nums,n)


# using inbuilt function .count() takes a lot of time
# for e in nums:
#     while nums.count(e) > 2:
#         nums.remove(e)
# print(len(nums))