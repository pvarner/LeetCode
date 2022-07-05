
from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        tmpMax = 0
        max = 0
        hashList = set()
        numSet = set(nums)
        index = 0
        

        for num in numSet:
            if (num - 1) not in numSet:
                tmpMax += 1
                count = 1
                while num + count in numSet:
                    tmpMax += 1
                    count += 1
                
                if tmpMax > max:
                    max = tmpMax

                count = 0
                tmpMax = 0
                index += 1

            else:
                index += 1

        return max


        
s = Solution()

val = s.longestConsecutive( [100,4,200,1,3,2] )
print (val)

p = [0,3,7,2,5,8,4,6,0,1]
val = s.longestConsecutive(p)
print (val)

p = []
val = s.longestConsecutive(p)
print (val)

p = [1]
val = s.longestConsecutive(p)
print (val)