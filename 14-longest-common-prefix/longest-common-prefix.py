class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        
        # Start with the first string in the array as the prefix
        prefix = strs[0]
        
        # Iterate over the rest of the strings
        for s in strs[1:]:
            # Reduce the prefix until it's a prefix of the current string
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                # If prefix becomes empty, return ""
                if not prefix:
                    return ""
        
        return prefix       