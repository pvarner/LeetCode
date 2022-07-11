class Solution:
    
    def helper(self, nums, target, lowIndex, highIndex):
        
        pivot = (highIndex + lowIndex) // 2
        

        
        if nums[pivot] == target:
            return pivot
        elif pivot == highIndex:
            return -1
        elif target > nums[pivot]:
            if pivot == lowIndex and pivot < len(nums) - 1 :
                pivot += 1
            return self.helper(nums, target, pivot, highIndex)
        else:
            return self.helper(nums, target, lowIndex, pivot)
        
        
    
    def search(self, nums: List[int], target: int) -> int:
        
        return self.helper(nums, target, 0, len(nums) - 1)
            
        