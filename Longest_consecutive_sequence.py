# https://leetcode.com/problems/longest-consecutive-sequence/
# Time Complexity = O(N)+O(N)+O(N) ===> O(3N)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        Longest_sequence = 0
        hashset = set(nums)
        for i in range(len(nums)):
            if nums[i] - 1 not in hashset:
                current = nums[i]
                count = 1
                while(current + 1 in hashset):
                    current += 1
                    count += 1
                    
                Longest_sequence = max(Longest_sequence,count)
        return Longest_sequence