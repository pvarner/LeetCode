#LeetCode: 724. Find Pivot Index
# Date: 7/2/2022

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        leftSum = 0
        arrSum = 0
        
        # get the sum total of the array
        for num in nums:
            arrSum = arrSum + num
        
        for index in range(len(nums)):
            if leftSum == (arrSum - nums[index]) - leftSum:
                return index
            else:
                leftSum = leftSum + nums[index]
                
        return -1
            