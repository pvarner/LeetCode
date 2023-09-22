#LeetCode: Easy 1929. Concatenation of Array
# Date: 9/22/2023

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        length = len(nums)
        for i in range(length):
            nums.append(nums[i])
            
        return nums;