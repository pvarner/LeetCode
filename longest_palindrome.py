class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        l = sorted(s)
        addOne = 0
        pairs = 0
        i = 0

        while i < len(l):

            if i < len(l)-1:
                if l[i] == l[i+1]:
                    pairs += 1
                    i += 2
                else:
                    addOne = 1
                    i += 1

            else:
                addOne = 1
                break

        return (pairs*2) + addOne


s = Solution()

p = "abccccdd"
val = s.longestPalindrome(p)
print(val)


p = "a"
val = s.longestPalindrome(p)
print(val)

p = "abcde"
val = s.longestPalindrome(p)
print(val)

p = "aAbcde"
val = s.longestPalindrome(p)
print(val)

p = "aaae"
val = s.longestPalindrome(p)
print(val)