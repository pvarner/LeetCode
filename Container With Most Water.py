#LeetCode: medium 11. Container With Most Water
#note: Does not pass all test cases
# Date: 9/23/2023
from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxHeadH = height[0]
        maxTailH = height[len(height)-1]
        maxTailHIndex = len(height) - 1
        max = 0
        wall = 0

        for i in range(len(height)-1):
            tail = len(height)-1
            maxTailH = 0
            if height[i] > maxHeadH or i == 0:
                maxHeadH = height[i]

                while tail != i and not (i > 0 and tail < maxTailHIndex):
                    if height[tail] > maxTailH or max == 0:
                        maxTailH = height[tail]
                        maxTailHIndex = tail;

                        if height[tail] > height[i]:
                            wall = height[i]
                        else:
                            wall = height[tail]

                        tmpMax = wall * (tail - i)
                        if max < tmpMax or max == 0:
                            max = tmpMax

                    tail -= 1
        return max



s = Solution()
val = s.maxArea([2,3,4,5,18,17,6])
print(val)