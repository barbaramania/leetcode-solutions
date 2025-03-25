<<<<<<< HEAD
class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False

        else:
            number_str = str(x)
            if number_str == number_str[::-1]:
                return True
            else:
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
>>>>>>> 2721809cf6a99fcdc31ba6e71c9ea30a5bbb4f0b
                return False