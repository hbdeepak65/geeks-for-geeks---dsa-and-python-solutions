class Solution:
    def getMiddle(self, head):
        fast=slow=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        return slow.data if slow else None
