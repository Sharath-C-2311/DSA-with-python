#299. Bulls and Cows

#brute force method that came to my mind , we have more efficient approach to solve this 
class Solution:
    def getHint(self, secret, guess):
        cow=0
        bull=0
        dic={}
        dic2={}
        for i in secret:
            dic[i] = secret.count(i)
        for i in guess:
            dic2[i] = guess.count(i)

        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bull+=1
                dic[secret[i]]-=1
                dic2[secret[i]]-=1
        
        for key,val in dic.items():
            if dic2.get(key) != None:
                cow+=min(val,dic2[key])
        
        return f"{bull}A{cow}B"
    
#efficient approach
class Solution:
    def getHint(self, secret, guess):
        cow=0
        bull=0
        dic={}
        
        for i in range(len(secret)):
            if secret[i]==guess[i]:
                bull+=1
            dic[secret[i]] = dic.get(secret[i],0) + 1
        

        for i in guess:
            if dic.get(i,0) > 0:
                dic[i]-=1
                cow+=1
                    
        return f"{bull}A{cow-bull}B"