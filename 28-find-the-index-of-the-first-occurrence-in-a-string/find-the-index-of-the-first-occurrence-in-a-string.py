class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # Edge case: if needle is an empty string, return 0
        if not needle:
            return 0
        
        # Use Python's built-in find() method to locate the first occurrence
        index = haystack.find(needle)
        
        return index
