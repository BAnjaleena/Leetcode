class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        # Initialize pointers for a and b starting from the last character
        i, j = len(a) - 1, len(b) - 1
        carry = 0
        result = []
        
        # Loop through both strings from the end to the start
        while i >= 0 or j >= 0 or carry:
            # Sum the carry with the current digits
            sum = carry
            
            # If i is still in bounds, add the corresponding digit of a
            if i >= 0:
                sum += int(a[i])
                i -= 1
                
            # If j is still in bounds, add the corresponding digit of b
            if j >= 0:
                sum += int(b[j])
                j -= 1
                
            # Compute the new digit and the new carry
            carry = sum // 2
            result.append(str(sum % 2))
        
        # Join the result list in reverse order to get the final binary string
        return ''.join(result[::-1])

# Example usage:
solution = Solution()
print(solution.addBinary("11", "1"))  # Output: "100"
print(solution.addBinary("1010", "1011"))  # Output: "10101"
