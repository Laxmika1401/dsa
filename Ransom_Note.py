#  https://leetcode.com/problems/ransom-note/
 
  
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashmap = {}
        for char in ransomNote:
            if char in hashmap:
                hashmap[char] +=1
            else:
                hashmap[char] = 1 
    
        for char in magazine:
            if char in hashmap:
                hashmap[char] -=1 
                if hashmap[char] == 0:
                    del(hashmap[char])
            
        if not hashmap:
            return True
        
        return False
