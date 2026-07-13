class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mydict = {}
        for index, num in enumerate(nums):
            nxt_sum = target - num
            if nxt_sum in mydict:
                return [mydict[nxt_sum],index]
            else:
                mydict[num] = index