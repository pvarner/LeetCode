#LeetCode: Medium 16. 3Sum Closest
# times out
# Date: 9/25/2023

from typing import List



def threeSumClosest(nums: List[int], target: int) -> int:

    a=0
    b=1
    c=2
    nums.sort()

    bestSum = nums[a] + nums[b] + nums[c]

    while a < len(nums)-2:
        
        while b < len(nums)-1:

            while c < len(nums):

                tempSum =nums[a] + nums[b] + nums[c] 
                if abs(target - bestSum) > abs(target - tempSum):
                     bestSum = tempSum

                if tempSum > target:
                    break
                c+=1
            b+=1
            c=b+1
        a+=1
        b=a+1
        c=b+1

    return bestSum


val = threeSumClosest([-1,2,1,-4], 1)
print(val)

