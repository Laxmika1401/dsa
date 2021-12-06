# Hard Question
https://leetcode.com/problems/reverse-pairs/

def merge_and_count(nums,begin,end):
    if begin >= end:
        return 0
    
    count = 0
    mid = (begin + end)// 2

    count += merge_and_count(nums ,begin, mid)
    count += merge_and_count(nums, mid+1, end)

    left = begin
    right = mid+1
    while left <= mid and right <= end:
        if nums[left] > 2 * nums[right]:
            count += mid - left + 1
            right += 1
        else:
            left += 1
    nums[begin:end+1] = sorted(nums[begin:end+1])
    
    return count

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        if not nums:
            return 0
        else:
            return merge_and_count(nums,0,len(nums)-1)
        
        