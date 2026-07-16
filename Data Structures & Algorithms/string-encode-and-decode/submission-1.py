class Solution:

    def encode(self, strs: List[str]) -> str:
        encoder = ""

        for word in strs:
            wordlen = len(word)
            encoder += str(wordlen) + '#' + word
        return encoder

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0 

        while i < len(s):
            delimiter = i

            #keep moving till we find our delimiter

            while s[delimiter] != "#":
                delimiter += 1

            word_length = int(s[i:delimiter]) 

            word_start = delimiter + 1    

            word_end = word_start + word_length

            result.append(s[word_start:word_end])

            i = word_end

        return result





