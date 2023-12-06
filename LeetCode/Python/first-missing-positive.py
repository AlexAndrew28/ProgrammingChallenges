from typing import List

"""
--PROBLEM DETAILS--

41. First Missing Positive
 
Given an unsorted integer array nums, return the smallest missing positive integer.

You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

Example:
Input: nums = [1,2,0]
Output: 3
Explanation: The numbers in the range [1,2] are all in the array.

Acceptance rate: 37.3%
Difficulty: Hard

--SUBMISSION DETAILS--

Status: Accepted
Langauge: Python
Runtime: 378ms (Beats 13.59%)
Memory: 30.3MB (Beats 47.61.16%)

Values correct as of: 04/12/2023

"""


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """ Run through the list swapping the positive integers to the position in the list they should occur if it was a sorted list. After
        going through once to do this, run through again and check if the current number equals the current index. If not then that number is 
        missing. 

        Args:
            nums (List[int]): An unsorted list of numbers

        Returns:
            int: The smallest positive integer not found in the input list nums
        """
        index = 0
        while index < len(nums):
            if nums[index] > 0 and nums[index] < len(nums)+1 and nums[index] != index+1:
                # if the number has occured before and is already at its correct index
                if nums[nums[index]-1] == nums[index]:
                    index += 1
                else:
                    # swap the number with the one at its index
                    temp = nums[nums[index]-1]
                    
                    nums[nums[index]-1] = nums[index]
                    
                    nums[index] = temp
            else:
                index += 1
        for index in range(0, len(nums)):
            # check if the current index equals the number at that index
            if nums[index] != index+1:
                return index + 1
        
        # if all the numbers are present then it must be 1 more than the length of the list
        return len(nums)+1
