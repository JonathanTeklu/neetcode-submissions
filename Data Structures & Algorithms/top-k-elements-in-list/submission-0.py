class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        empty_dict = {}
        totals = []     # empty dict =  {2:3 , 1: 4 , 5:2}
        for num in nums:     #total dict = [ ,]  
            if num in empty_dict:  
                empty_dict[num] += 1
            else:
                empty_dict[num] = 1
        for i in range(k):
            max_val = max(empty_dict, key = empty_dict.get)
            totals.append(max_val)
            del empty_dict[max_val]
        return totals
        
        

