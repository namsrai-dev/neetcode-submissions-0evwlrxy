class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        arr = []
        for my_node in lists:  
            temp = my_node
            while temp:
                arr.append(temp.val)
                temp = temp.next

        head = ListNode()
        temp_head = head
        for num in sorted(arr):
            temp_head.next = ListNode(num)
            temp_head = temp_head.next


        return head.next