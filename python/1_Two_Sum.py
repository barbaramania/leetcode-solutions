class Solution:
    def twoSum(self,nums, target):
        for i in range(1,len(nums)):
            setter = target - nums[i]
            if setter in nums:
                index = nums.index(setter)
                if i != index:
                    return(i,index)
                    break