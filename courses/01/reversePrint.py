from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reversePrintV1(self, head: ListNode) -> List[int]:
        re = []
        te = head
        while te is not None:
            re.append(te.val)
            te = te.next
            
        return re[::-1]
        # re.reverse()
        # return re
        
    def reversePrintV2(self, head: ListNode) -> List[int]:
        return self.reversePrintV2(head) + [head.val] if head else []