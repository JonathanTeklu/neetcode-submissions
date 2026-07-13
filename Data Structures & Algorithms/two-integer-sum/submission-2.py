class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mydict = {}

        for index, number in enumerate(nums):
            dif = target - number
            if dif in mydict:
                return [mydict[dif],index]
            mydict[number] = index

            