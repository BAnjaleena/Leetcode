class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 2:
            return x
        
        low, high = 1, x // 2
        
        while low <= high:
            mid = (low + high) // 2
            square = mid * mid
            
            if square == x:
                return mid
            elif square < x:
                low = mid + 1
            else:
                high = mid - 1
                
        return high  # high is the truncated integer square root
