https://leetcode.com/problems/maximize-distance-to-closest-person/

class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        i = 0
        maximum_distance = 0
        while(i<len(seats) and seats[i] == 1):
            i += 1
            s = i
        while(i<len(seats)):
            s = i
            count = 0
            while(i<len(seats) and seats[i] == 0):
                count += 1
                i += 1
            temp = i-s
            if (s == 0 or i == len(seats)):
                maximum_distance = max(maximum_distance , temp)
            else:
                maximum_distance = max(maximum_distance , (temp + 1)//2)
            while(i<len(seats) and seats[i] == 1):
                i += 1
        return maximum_distance