class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict={}
        if nums == []:
            return False
        for i in range(0,len(nums)):
            if nums[i] in dict:
                return True
            elif nums[i] not in dict: 
                dict[nums[i]]=1
                if i == len(nums)-1:
                    return False
