class Solution:
    def lengthOfLongestSubstring(self, s:str):
        if not s: return 0
        l = 0
        r = 1
        maxsubstring = 0
        charachters = set()

        for r in range(len(s)):
            while s[r] in charachters:
                charachters.remove(s[l])
                l += 1

            charachters.add(s[r])                                 
            maxsubstring = max(maxsubstring, r-l+1)
        return maxsubstring
