class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        angrms = {}
        for word in strs:
            srt_word = tuple(sorted(word))
            if srt_word in angrms: 
                angrms[srt_word].append(word)
            else:
                angrms[srt_word] = [word]
        return list(angrms.values())
