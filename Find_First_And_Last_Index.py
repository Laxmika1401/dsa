# Binary Search Question

# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

# O(Log N) Complexity Answer 
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first = 0
        last = len(nums) - 1
        ans = [-1, -1]
        while(first <= last):
            mid = (first + last) // 2
            if nums[mid] == target:
                ans[0] = mid
                last = mid - 1
            elif nums[mid] < target:
                first = mid + 1
            else:
                last = mid - 1
                
        first = 0
        last = len(nums)-1
        while(first <= last):
            mid = (first + last) // 2
            if target == nums[mid]:
                ans[1] = mid
                first = mid + 1
            elif nums[mid] < target:
                first = mid + 1
            else:
                last = mid - 1
        return ans