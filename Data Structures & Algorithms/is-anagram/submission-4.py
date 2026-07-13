class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #UMPIRE
        # understand that for a word to be an anagram of another word they have to be the same length
        # can we just sort and compare?
        # Match it - return true or false based on string comparison
        #matching we can see that dictionaries store frequencies of occurences like in the last priblem we did
        #if we iterate through bothe strings and add their elements to a hash table that stores frquencies of each element then we can comppare if the two tables are the same
        # we have a string s and a string t 
        #sorted_s =''.join(sorted(s))
        #sorted_t = ''.join(sorted(t))
        #if sorted_t == sorted_s:
          #  return True
        #return False
        s_dict = {}
        t_dict = {}
        for letter in s:
            if letter in s_dict:
                s_dict[letter] += 1
            else:
                s_dict[letter] = 1
        for i in t:
            if i in t_dict:
                t_dict[i] += 1
            else:
                t_dict[i] = 1

        if s_dict == t_dict:
            return True 
        return False




