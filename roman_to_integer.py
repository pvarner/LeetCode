# LeetCode: 13. Roman to Integer
# Date: 7/1/2022


class Solution:
    
    def convertRoman(self, romanNum):
        if (romanNum == 'I'):
            return 1;
        elif(romanNum == 'V'):
            return 5;
        elif(romanNum == 'X'):
            return 10;
        elif(romanNum == 'L'):
            return 50;
        elif(romanNum == 'C'):
            return 100;
        elif(romanNum == 'D'):
            return 500;
        elif(romanNum == 'M'):
            return 1000;
        else:
            return 0
    
    def romanToInt(self, s: str) -> int:
        val = s
        tempSum = 0
        totalSum = 0
        for index in val:
            if (tempSum == 0 and totalSum == 0):
                tempSum = self.convertRoman(index)
                prev = index
            else:

                if(self.convertRoman(prev) < self.convertRoman(index)):
                    totalSum = totalSum + self.convertRoman(index) - self.convertRoman(prev)
                    tempSum = 0
                    prev = index
                else:
                    totalSum = totalSum + tempSum
                    tempSum = self.convertRoman(index)
                    prev = index

        totalSum = totalSum + tempSum
        return totalSum