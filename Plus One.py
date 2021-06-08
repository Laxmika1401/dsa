# https://leetcode.com/problems/plus-one/
class Solution:
    def plusOne(self, digits):
        l=[str(i) for i in digits]
        s=''.join(l)
        p=int(s)
        p+=1
        res=[int(x) for x in str(p)]
        return res
        
        
t=Solution()
