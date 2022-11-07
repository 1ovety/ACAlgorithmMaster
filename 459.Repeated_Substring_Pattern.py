class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:

        # if there is a k repeating pattern in s, then
        # a k-rotation of s should be equal to s
        for k in range(1, len(s)//2 +1):   
            if s == s[k:] + s[:k]:
                return True
        return False