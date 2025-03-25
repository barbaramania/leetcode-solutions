<<<<<<< HEAD
class Solution(object):
    def maxProfit(self, prices):
        total = 0
        min_price = prices [0]
        for i in prices:
            if i < min_price:
                min_price = i
            elif i - min_price > total:
                total = i - min_price
        return total
=======
class Solution:
    def twoSum(self,nums, target):
        for i in range(1,len(nums)):
            setter = target - nums[i]
            if setter in nums:
                index = nums.index(setter)
                if i != index:
                    return(i,index)
                    break
>>>>>>> 2721809cf6a99fcdc31ba6e71c9ea30a5bbb4f0b
