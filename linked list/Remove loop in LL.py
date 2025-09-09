class Solution:
    def removeLoop(self, head):
        fast=slow=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow == fast:
                break
        else:
            return
        
        slow=head
        while slow != fast:
            slow=slow.next
            fast=fast.next
        
        while fast.next!=slow:
            fast=fast.next
        fast.next=None
            
