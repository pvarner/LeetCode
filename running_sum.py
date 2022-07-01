# LeetCode: 1480. Running Sum of 1d Array
# Date: 7/1/2022

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        sums = []
        for val in nums:
            if len(sums) == 0:
                sums.append(val)
            else:
                sums.append(val + sums[len(sums)-1])
        return sums