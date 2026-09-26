# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #ends when prev points to new head and curr points to nullptr at end
        prev = None
        curr = head
        while curr: #because curr will be None at the end
            #set a ptr to the +1
            temp = curr.next
            #set the next ptr to the -1 (to reverse it)
            curr.next = prev
            #increment pointers +1
            #move prev to curr +1
            prev = curr
            #move curr to temp +1
            curr = temp
        return prev