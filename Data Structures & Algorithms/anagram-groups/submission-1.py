class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mydick = {}

        for word in strs:
            sortedword = ''.join(sorted(word))

            if sortedword in mydick:
                mydick[sortedword].append(word)

            else:
                mydick[sortedword] = [word]
        return list(mydick.values())