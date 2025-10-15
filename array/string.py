# remove capital character
# s = input()

# news=""
# for i in s:
#     c=i
#     if ord(i)<90:
#         c = chr(ord(i) + ord("a") - ord("A"))
#     news+=c

# print("Before : ",s)
# print("After : ",news)


# palindrome 


s = input()

if s==s[::-1]:
    print("the string is palindrome")
else:
    print('the string is not palindrome')

 