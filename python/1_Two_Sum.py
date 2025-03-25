<<<<<<< HEAD
class Solution:
    def twoSum(self,nums, target):
        for i in range(1,len(nums)):
            setter = target - nums[i]
            if setter in nums:
                index = nums.index(setter)
                if i != index:
                    return(i,index)
                    break
=======
class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False

        else:
            number_str = str(x)
            if number_str == number_str[::-1]:
                return True
            else:
                return False
>>>>>>> 2721809cf6a99fcdc31ba6e71c9ea30a5bbb4f0b
