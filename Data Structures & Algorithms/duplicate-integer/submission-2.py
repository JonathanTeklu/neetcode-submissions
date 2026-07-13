class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         #u -nderstand- ask questions and assumptions!!!
         #m -atch it to something you've seen in the past
         #p- plan/pseudocode
         #i- implement to real code
         #r- review
         #e- evaluate
        #if a value is found more than once we return false
        # is the array of numbers sorted?
        #"appears more than once" meaning we have to do a lookup
        #hash tables offer constant time lookup
        #plan to iterate through the nums array and add each element to the
        # dictionary, the only chatch is if element is already in the dictionary we automatically return true

       
        dict = {}
        for i in nums:
            if i not in dict:
                dict[i] = 1
            else: 
                return True
        return False

