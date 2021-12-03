https://leetcode.com/problems/decompress-run-length-encoded-list/



class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(0,len(nums),2):
            freq = nums[i]
            value = nums[i+1]
            for i in range(freq):
                result.append(value)
        return result
        