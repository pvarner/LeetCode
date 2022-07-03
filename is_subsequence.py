class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        index = 0

        if s == "":
            return True 

        for sIndex in range(len(s)):
            for tIndex in range(index,len(t)):
                if s[sIndex] == t[tIndex]:
                    index = tIndex + 1
                    if sIndex == len(s) -1:
                        return True
                    if tIndex == len(t) - 1:
                        return False
                    break
                elif tIndex == len(t) - 1:
                    return False
        return False
            


s = Solution()
val =s.isSubsequence("aaa", "bbaaaa")
print(val)
val =s.isSubsequence("aaaaaa", "bbaaaa")
print(val)