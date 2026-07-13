class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #umpire  
        #hashmap- keep track of the number of occurences of each letter

        my_dict = {}
        t_dict = {}

        for letter in s:
            if letter in my_dict:
                my_dict[letter] += 1
            else:
                my_dict[letter] = 1
        for letter in t: 
            if letter in t_dict:
                t_dict[letter] += 1
            else:
                t_dict[letter] = 1
            
        if my_dict == t_dict:
            return True
        return False
                



