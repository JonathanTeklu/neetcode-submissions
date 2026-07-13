class Solution:
    def hasDuplicate(self, nums:List[int])->bool:
        number_occurence = {}
        for i in nums:
            if i in number_occurence:
                return True
            else:
                number_occurence[i] = 1
        return False
