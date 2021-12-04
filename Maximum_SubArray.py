https://leetcode.com/problems/maximum-subarray/


# Using Kadane's Algorithm


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        SubArraySum = 0
        LargestSum = nums[0]
        for i in range(len(nums)):
            SubArraySum += nums[i]
            if SubArraySum > LargestSum:
                LargestSum = SubArraySum
            if SubArraySum < 0:
                SubArraySum = 0
        return LargestSum
        