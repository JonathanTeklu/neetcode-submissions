class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        apperance = {}
        if len(trust) >= n:
            return -1

        for sub in trust:
            if sub[1] in apperance:
                apperance[sub[1]] += 1 
            else:
                apperance[sub[1]] = 1

        for person in apperance: 
            if apperance[person] == n-1:
                trusted_person = person
            for sub in trust:
                if sub[0] == trusted_person:
                    return -1 
            return trusted_person
        return -1
            
        

