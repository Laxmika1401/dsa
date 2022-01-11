
# https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/
# Given an integer array nums and an integer k, return the number of pairs (i, j) where i < j such that |nums[i] - nums[j]| == k.

# The value of |x| is defined as:

# x if x >= 0.
# -x if x < 0.
class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
# Optimized Approach
        nums_dict, result  = {}, 0
        for i in nums:
            if i in nums_dict:
                nums_dict[i] += 1
            else:
                nums_dict[i] = 1
        answer = []
        for i in nums_dict:
            answer.append(i)
        for i in answer:
            if (i+k) in nums_dict:
                result += nums_dict[i] * nums_dict[i+k]
        return result
        
                   
# Brute Force Approach ====>

#         count = 0
#         for i in range(len(nums)):
#             for j in range(i+1,len(nums)):
#                 if nums[i] > nums[j]:
#                     if nums[i] - nums[j] == k:
#                         count += 1
#                     else:
#                         continue
#                 else:
#                     if nums[j] - nums[i] == k:
#                         count += 1
#                     else:
#                         continue
#         return count
        