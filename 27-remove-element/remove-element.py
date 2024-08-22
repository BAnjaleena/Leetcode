class Solution(object):
    def removeElement(self, nums, val):
        # Initialize a pointer for the position to insert the next valid element
        insert_pos = 0
        
        # Loop through each element in the array
        for i in range(len(nums)):
            # If the current element is not the value to remove, 
            # place it at the current insert position and increment the insert position
            if nums[i] != val:
                nums[insert_pos] = nums[i]
                insert_pos += 1
        
        # Return the length of the modified array
        return insert_pos
       