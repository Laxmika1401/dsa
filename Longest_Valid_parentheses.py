# https://leetcode.com/problems/longest-valid-parentheses/


# Input: s = "(()"
# Output: 2
# Explanation: The longest valid parentheses substring is "()".


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if s == "":
            return 0
        else:
            stack = [-1]
            max1 = 0
            len1 = 0
            for i in range(len(s)):
                if s[i] == "(":
                    stack.append(i)
                else:
                    stack.pop()
                    if stack == []:
                        stack.append(i)
                    else:
                        len1 = i - stack[-1]
                        max1 = max(max1,len1)
            return max1
s = Solution()
s.longestValidParentheses("()())")