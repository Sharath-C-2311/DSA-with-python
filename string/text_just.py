class Solution:
    def fullJustify(self, words, maxWidth):
        result=[]
        i = 0
        while(i<len(words)):
            j=0
            string = []
            req_seq = ""
            k=0
            while(i<len(words) and k+j+len(words[i])<=maxWidth):
                j+=len(words[i])
                string.append(words[i])
                i+=1
                k+=1
            num_words = maxWidth - j
            if i==len(words) or len(string)==1:
                req_seq = " ".join(string)
                req_seq +=(" "*(maxWidth-len(req_seq))) 
            else:
                gaps = len(string)-1
                space_per_word = num_words // gaps
                extra_space = num_words % gaps
                for a in range(gaps):
                    req_seq += string[a]
                    req_seq += " "*(space_per_word + (1 if a<extra_space else 0))
                req_seq += string[-1]
            result.append(req_seq)

        return result
    
# Given an array of strings words and a width maxWidth, 
# format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.
# You should pack your words in a greedy approach; that is, 
# pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.
# Extra spaces between words should be distributed as evenly as possible. 
# If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.
# For the last line of text, it should be left-justified, 
# and no extra space is inserted between words.

# Note:

# A word is defined as a character sequence consisting of non-space characters only.
# Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
# The input array words contains at least one word.
 

# Example 1:

# Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
# Output:
# [
#    "This    is    an",
#    "example  of text",
#    "justification.  "
# ]