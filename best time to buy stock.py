class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sum = 0
        curMax = 0
        curMin = float("inf")
        
        for i in range(len(prices)):

            if prices[i] < curMin:
                curMin = prices[i]
            elif curMax < (prices[i] - curMin):
                curMax = prices[i] - curMin

        return curMax
 

s = Solution()

l = [7,1,5,3,6,4]
val = s.maxProfit(l)
print(val)

l = [1]
val = s.maxProfit(l)
print(val)

l = [3,3]
val = s.maxProfit(l)
print(val)

l = [7,6,4,3,1]
val = s.maxProfit(l)
print(val)

l = [1,2,4]
val = s.maxProfit(l)
print(val)

l = [1,4,2]
val = s.maxProfit(l)
print(val)
