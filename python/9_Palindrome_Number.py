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