class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
                my_dict = {}

                for element in nums:
                    if element in my_dict:
                        return True
                    my_dict[element] = 1
                return False

            