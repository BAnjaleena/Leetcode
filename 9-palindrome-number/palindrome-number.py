class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # A negative number cannot be a palindrome
        # Also, if the last digit is 0, the number cannot be a palindrome
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        # Reversed half of the number
        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10
        
        # When the length is odd, we can get rid of the middle digit by reversed_half // 10
        return x == reversed_half or x == reversed_half // 10
