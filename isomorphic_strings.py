class Solution:
    
      
    def isIsomorphic(self, s: str, t: str) -> bool:
        checkedIndexes = []
        matchList = []
        matchList2 = []
        
        if len(s) != len(t):
            return False
        
        for index in range(len(s)):

            if index not in checkedIndexes:
                for i in range(index,len(s)):
                    if s[index] == s[i]:
                        matchList.append(i)

                for i in range(index,len(t)):
                    if t[index] == t[i] :
                        matchList2.append(i)
                        if i not in matchList:
                            return False
                
                if matchList != matchList2:
                    return False

                checkedIndexes.extend(matchList)
                matchList = []
                matchList2 = []
        return True

solution = Solution()
val = solution.isIsomorphic("egg", "add")
print(val)
val = solution.isIsomorphic("foo", "bar")
print(val)
val = solution.isIsomorphic("paper", "title")
print(val)
val = solution.isIsomorphic("badc", "baba")
print(val)