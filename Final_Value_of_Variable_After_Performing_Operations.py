#LeetCode: Easy 2011. Final Value of Variable After Performing Operations Concatenation of Array
# Date: 9/22/2023

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        sum = 0;
        
        for i in operations:
            if i[0] != 'X':
                if i[0] == '+':
                    sum += 1;
                else:
                    sum -= 1;
            else:
                if i[len(i)-1] == '+':
                    sum += 1;
                else:
                    sum -= 1;

        return sum;
