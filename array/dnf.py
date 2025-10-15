#sort 0's 1's and 2's without using any sorting algorithm

arr=list(map(int,input().split()))
la=len(arr)

l=0
m=0
h=la-1

while(m<h):
    if arr[m]==0:
        arr[m],arr[l] = arr[l],arr[m]
        m+=1
        l+=1
        print("0")
    elif arr[m]==2:
        arr[m],arr[h]=arr[h],arr[m]
        h-=1
        # m+=1
        print("2")
    else:
        m+=1
        print("1")

print("Sorted Array : ",arr)

