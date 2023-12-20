from typing import List, Optional

"""
--PROBLEM DETAILS--

23. Merge k Sorted Lists


You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

Example:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

Acceptance rate: 53.3%
Difficulty: Hard

--SUBMISSION DETAILS--

Status: Accepted
Language: Python
Runtime: 97ms (Beats 56.28%)
Memory: 20.63MB (Beats 22.79%)

Values correct as of: 22/11/2023

"""



class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """ Combines all of the linked lists into a single unsorted list. Proceeds to sort the list and convert back into a linked list

        Args:
            lists (List[Optional[ListNode]]): A list of linked lists to combine and sort

        Returns:
            Optional[ListNode]: A final sorted linked list containing all of the items from each of the linked lists
        """
        all_values = []
        
        # pull all the values in all of the linked lists into a single list
        for linked_list in lists:
            while linked_list is not None:
                all_values.append(linked_list.val)
                linked_list = linked_list.next
        
        # sort the list
        all_values.sort()

        # build a linked list from the sorted list
        dummy_head = ListNode()
        current = dummy_head
        for i in all_values:
            current.next = ListNode(val=i)
            current = current.next
            
            
        return dummy_head.next