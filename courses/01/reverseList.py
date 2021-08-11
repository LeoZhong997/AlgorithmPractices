# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    """
    定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。
    输入: 1->2->3->4->5->NULL
    输出: 5->4->3->2->1->NULL
    """
    def reverseListV1(self, head: ListNode) -> ListNode:
        cur = head
        if cur is None:
            return cur
        if cur.next is None:
            return cur
        nex = cur.next  # save next pointer
        cur.next = None # init last node's next pointer = None

        while nex:
            tem = cur   # save current head
            cur = nex   
            nex = cur.next  # save new next pointer
            cur.next = tem  # change current node's next pointer
        return cur
    
    def reverseListV2(self, head: ListNode) -> ListNode:
        """
        迭代-双指针: 考虑遍历链表，并在访问各节点时修改 next 引用指向
        """
        cur, pre = head, None
        while cur:
            tmp = cur.next # 暂存后继节点 cur.next
            cur.next = pre # 修改 next 引用指向
            pre = cur      # pre 暂存 cur
            cur = tmp      # cur 访问下一节点
        return pre

    def reverseListV3(self, head: ListNode) -> ListNode:
        """
        递归: 考虑使用递归法遍历链表，当越过尾节点后终止递归，在回溯时修改各节点的 next 引用指向。
        """
        def recur(cur, pre):
            if not cur: return pre     # 终止条件
            res = recur(cur.next, cur) # 递归后继节点
            cur.next = pre             # 修改节点引用指向
            return res                 # 返回反转链表的头节点
        
        return recur(head, None)       # 调用递归并返回
