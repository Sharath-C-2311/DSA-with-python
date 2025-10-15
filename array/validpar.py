s=input("Enter the input : ")
def valid(s):
    l=[]
    d={
        "]":"[","}":"{",")":"("
    }
    for i in range(len(s)):
        print(l)
        if s[i] in d.values():
            l.append(s[i])
        elif l==[] or d[s[i]]!=l.pop():
            return False

    return len(l)==0

if(valid(s)):
    print("valid parentesis...")
else:
    print("invalid parentesis!!!")
