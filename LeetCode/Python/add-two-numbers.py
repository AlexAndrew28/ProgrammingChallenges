from typing import Optional

"""
--PROBLEM DETAILS--

2. Add Two Numbers

You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Acceptance rate: 41.6%
Difficulty: Medium

--SUBMISSION DETAILS--

Status: Accepted
Language: Python
Runtime: 61ms (Beats 76.81%)
Memory: 16.4MB (Beats 7.48%)


Values correct as of: 20/11/2023

"""

class ListNode:
    def __init__(self, val=0, next=None):
        """ Instantiates a simple linked list node

        Args:
            val (int, optional): Value of the node. Defaults to 0.
            next (_type_, optional): The next node in the linked list. Defaults to None.
        """
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, linked_list_1: Optional[ListNode], linked_list_2: Optional[ListNode]) -> Optional[ListNode]:
        """ 
        Iterates through the two linked lists in reverse order. 
        At each step performs digit-wise addition including a carry value from the previous step. 
        At each step the output of the current digit-wise sum is added into a linked list that forms the output.
        

        Args:
            l1 (Optional[ListNode]): Linked list containing the first number
            l2 (Optional[ListNode]): Linked list containing the second number

        Returns:
            Optional[ListNode]: A linked list containing the answer
        """
        carry = 0
        head = ListNode(0)
        current_pos = head
        # while there is at least one number still left to add
        while linked_list_1 is not None or linked_list_2 is not None or carry != 0:
            
            # get sum of current digit
            ll_1_val = 0
            if linked_list_1 is not None:
                ll_1_val = linked_list_1.val
            ll_2_val = 0
            if linked_list_2 is not None:
                ll_2_val = linked_list_2.val
    
            current = ll_1_val + ll_2_val + carry

            carry = current // 10
            current = current % 10
            
            # advance through the linked lists 
            if linked_list_1 is not None:
                linked_list_1 = linked_list_1.next
            if linked_list_2 is not None:
                linked_list_2 = linked_list_2.next

            # build the output
            new_node = ListNode(current)
            current_pos.next = new_node
            current_pos = new_node

        return head.next