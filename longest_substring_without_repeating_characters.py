# Not working yet
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        headIndex = 0
        tailIndex = 1
        tmpLongest = 1
        longest = 0

        if len(s) == 0:
            return 0
        
        while tailIndex < len(s):
                if s[tailIndex] not in s[headIndex:tailIndex]:
                    tailIndex += 1
                    tmpLongest += 1

                else:
                    headIndex += 1 
                    tailIndex = headIndex + 1 
                    if tmpLongest > longest:
                        longest = tmpLongest

                    tmpLongest = 1

        if tmpLongest > longest:
            longest = tmpLongest
          
            

        return longest
        #if headIndex < len(s) - 1 and s[-1] not in s[headIndex:tailIndex-1]:
            #tmpLongest += 1
            #if tmpLongest > longest:
                #longest = tmpLongest



        return longest



s = Solution()

print("test: abcabcbb:")
val = s.lengthOfLongestSubstring("abcabcbb")
if s.lengthOfLongestSubstring("abcabcbb") == 3:
    print("pass" )
else:
    print("fail - "  + str(val))

print("test: bbbbb:")
val = s.lengthOfLongestSubstring("bbbbb")
if s.lengthOfLongestSubstring("bbbbb") == 1:
    print("pass")
else:
    print("fail - "  + str(val))


print("test: :")
if s.lengthOfLongestSubstring("") == 0:
    print("pass")
else:
    print("fail")


print("test: abcxasdfjkl")
val = s.lengthOfLongestSubstring("abcxasdfjkl")
if s.lengthOfLongestSubstring("abcxasdfjkl") == 10:
    print("pass")
else:
    print("fail - " + str(val))


print("test: pwwkew")
val = s.lengthOfLongestSubstring("pwwkew")
if s.lengthOfLongestSubstring("pwwkew") == 3:
    print("pass")
else:
    print("fail - " + str(val))