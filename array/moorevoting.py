l=list(map(int ,input().split()))
l.sort()
count=1
maxc=0
maxi=0
for i in range(len(l)-1):
    if l[i]==l[i+1]:
        count+=1
    else:
        if count>maxc:
            maxc = count
            maxi=i
        count=1
if count>maxc:
    maxc=count
    maxi=i
print("max count : ",maxc,"\nmax element : ",l[maxi])
