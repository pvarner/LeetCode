#LeetCode: Easy 1470. Shuffle the Array 
# Date: 9/22/2023
from typing import List

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        index = 1;

        for i in range(n):
            val = nums[n + i]
            del nums[n+i]
            nums.insert(index,val);
            index += 2;

        return nums;



s = Solution();
val = s.shuffle([1,2,3,4,4,3,2,1], 4)
print(val)