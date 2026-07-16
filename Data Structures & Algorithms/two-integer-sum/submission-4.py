class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mydic = {}
        for index, num in enumerate(nums):
            mydic[num] = index
        for i, n in enumerate(nums):
            diff = target -  n
            if diff in mydic:
                return [i, mydic[diff]]
        return []