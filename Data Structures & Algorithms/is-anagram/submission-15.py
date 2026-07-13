class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictionary_s = {}
        dictionary_t = {}
        
        if len(s) != len(t):
            return False

        for letter in s: 
            if letter in dictionary_s:
                dictionary_s[letter] += 1
            else:
                dictionary_s[letter] = 1
        
        for char in t: 
            if char in dictionary_t:
                dictionary_t[char] += 1
            else:
                dictionary_t[char] = 1

        if dictionary_s == dictionary_t:
            return True
        return False        
            