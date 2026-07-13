class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #GOAL:sum to 0 - so if we get a list of all positive numbers it wouldn't work
        #NEED TO BE DISTINCT INDICIES
        #NEEDS TO BE THREE NUMBERS
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if a > 0:
                break
            if i > 0 and a == nums[i-1]:
                continue
            
            l = i + 1
            r = len(nums) - 1

            while l < r: 
                threesum = a + nums[l] + nums[r]
                if threesum == 0: 
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
                    while nums[r] == nums[r+1] and l < r:
                        r -= 1
                elif threesum > 0:
                    r -= 1
                elif threesum < 0:
                    l += 1
        return res
                
