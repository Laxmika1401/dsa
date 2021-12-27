# https://leetcode.com/problems/valid-parentheses/

# Input: s = "()"
# Output: true



class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if s[i] == "(" or s[i] == "[" or s[i] == "{":
                stack.append(s[i])
            else:
                if stack == []:
                    return False
                else:
                    last = stack[-1]
                    stack.pop()
                    if (s[i] == ")" and last == "(") or (s[i] == "]" and last == "[") or (s[i] == "}" and last == "{"):
                        pass
                    else:
                        return False
        if stack == []:
            return True
        return False
s = Solution()
s.isValid("(){}[]")