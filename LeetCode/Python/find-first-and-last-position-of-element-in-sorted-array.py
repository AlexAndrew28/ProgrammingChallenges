from typing import List

"""
--PROBLEM DETAILS--

34. Find First and Last Position of Element in Sorted Array

Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Acceptance rate: 43.5%
Difficulty: Medium

--SUBMISSION DETAILS--

Status: Accepted
Langauge: Python
Runtime: 86ms (Beats 44.67%)
Memory: 17.7MB (Beats 71.10%)

Values correct as of: 20/11/2023

"""


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """Uses Binary search to find an instance of the target number. Once found creates two pointers that move
        up and down the list to find the start and end index of the block of numbers.

        Args:
            nums (List[int]): A sorted list of integers
            target (int): A number to find the start and end index of within the list of numbers

        Returns:
            List[int]: The start and end indexes of the target number
        """
        if nums == []:
            return [-1, -1]

        else: 
            high = len(nums)-1
            low = 0
            found = False

            # binary search to find the number
            while low <= high and found is False:
                search_index = (high+low) // 2
                
                if nums[search_index] > target:
                    high = search_index - 1
                elif nums[search_index] < target:
                    low = search_index + 1
                else:
                    found = True
                    break

            # if the number is in the list
            if found:
                low_ptr = search_index
                high_ptr = search_index
                
                # find the first occurance
                while low_ptr > 0 and nums[low_ptr-1] == target:
                    low_ptr -= 1
                
                # find the last occurance
                while high_ptr < len(nums)-1 and nums[high_ptr+1] == target:
                    high_ptr += 1
                
                
                return [low_ptr, high_ptr]
            else:
                # the number was not in the list
                return [-1, -1]