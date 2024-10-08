class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Stack to keep track of opening brackets
        stack = []
        
        # Dictionary to map closing brackets to their corresponding opening brackets
        bracket_map = {')': '(', '}': '{', ']': '['}
        
        # Iterate through the characters in the string
        for char in s:
            # If it's a closing bracket
            if char in bracket_map:
                # Pop the top element from the stack if it's not empty; otherwise, use a dummy value
                top_element = stack.pop() if stack else '#'
                
                # If the popped element doesn't match the corresponding opening bracket, return False
                if bracket_map[char] != top_element:
                    return False
            else:
                # It's an opening bracket, so push it onto the stack
                stack.append(char)
        
        # If the stack is empty, all the opening brackets had matching closing brackets
        return not stack

        