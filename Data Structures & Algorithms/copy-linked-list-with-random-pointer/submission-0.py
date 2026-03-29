"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        temp = head
        dummy_node = Node(0)
        second_head = dummy_node
        my_dict = {}
        while temp:
            new_node = Node(temp.val)
            my_dict[temp] = new_node
            dummy_node.next = new_node
            dummy_node = dummy_node.next
            temp = temp.next
        # print(my_dict)
        temp2 = head
        temp3 = second_head.next
        while temp2:
            if temp2.random:
                temp3.random = my_dict[temp2.random]
            temp3 = temp3.next
            temp2 = temp2.next 

        return second_head.next