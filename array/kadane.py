current_sum=0 #stores sum of all previous elements
max_p=0
l=list(map(int,input().split()))
for i in l:
    temp=current_sum+i
    if temp<i: #if previous sum + current element less than current element
        current_sum=i
    else:
        current_sum+=i
    if max_p<current_sum:
        max_p=current_sum
print("max profit : ",max_p)