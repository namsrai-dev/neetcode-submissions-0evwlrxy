# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp = l1
        temp2 = l2
        num1 = 0
        num2 = 0
        cnt = 0
        tmp = ListNode()
        tmp_head = tmp
        while temp:
            num1 = 10 ** cnt * temp.val + num1
            temp = temp.next
            cnt += 1
        cnt = 0
        while temp2:
            num2 = 10 ** cnt * temp2.val + num2
            temp2 = temp2.next
            cnt += 1

        num = num1 + num2
        for num in reversed(str(num)):
            tmp.next = ListNode(int(num))
            tmp = tmp.next            
        # while num:
        #     digit = num % 10
        #     tmp.next = ListNode(digit)
        #     tmp = tmp.next
        #     num = num // 10
        return tmp_head.next

        

