class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sdict = {}
        tdict = {}
        for s in s:
            if s in sdict:
                sdict[s] += 1
            else:
                sdict[s] = 1
        
        for t in t:
            if t in tdict:
                tdict[t] += 1
            else:
                tdict[t] = 1

        if tdict == sdict:
            return True
        return False


        
        
                       
                       
                       
                       
                        #could also sort it and compre strings
                        #intuition- if it can be any letter just needs to contain the 
                        #same letters and the same amount of each letter- simple
                        #dictionary can help with that. compare dictionaries(technique is possible)
         