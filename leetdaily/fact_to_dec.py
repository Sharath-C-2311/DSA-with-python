# Given two integers representing the numerator and denominator of a fraction, 
# return the fraction in string format.
# If the fractional part is repeating, enclose the repeating part in parentheses.
# If multiple answers are possible, return any of them.
# It is guaranteed that the length of the answer string is less than 104 for all the given inputs.


class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        result=[]
        if numerator==0:
            return "0"
        if (numerator<0 and denominator>0) or (numerator>0 and denominator<0) :
            result.append("-")

        numerator,denominator=abs(numerator),abs(denominator)

        result.append(str(numerator//denominator))

        rem = numerator%denominator

        if rem==0:
            return "".join(result)
        result.append(".")
        m = {}
        while rem:
       
            if rem in m:
                result.insert(m[rem],"(")
                result.append(")")
                break
            m[rem] = len(result)
            rem*=10
            result.append(str(rem//denominator))
            rem%=denominator
         
        return "".join(result)
    
s=Solution()
result = s.fractionToDecimal(4,333)
print(result)
