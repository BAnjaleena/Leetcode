# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Start with the head node
        current = head
        
        # Traverse the list until the end
        while current and current.next:
            # If current node's value is the same as the next node's value, skip the next node
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                # Otherwise, move to the next node
                current = current.next
        
        # Return the modified list starting from head
        return head
   