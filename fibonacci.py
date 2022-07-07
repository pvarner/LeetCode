class Solution:
    def fib(self, n: int) -> int:
        
        i = 1
        curSum = 1
        prevSum = 0
        
        if n == 0:
            return prevSum
        elif n == 1:
            return curSum
        
        while i < n:
            tmp = curSum + prevSum
            prevSum = curSum
            curSum = tmp
            i+=1
        return curSum
            