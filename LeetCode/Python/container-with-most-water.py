from typing import List

"""
--PROBLEM DETAILS--

11. Container With Most Water

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Example:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Acceptance rate: 54.3%
Difficulty: Medium

--SUBMISSION DETAILS--

Status: Accepted
Language: Python
Runtime: 603ms (Beats 47.46%)
Memory: 29.2MB (Beats 52.71%)

Values correct as of: 20/11/2023

"""


class Solution:
    def maxArea(self, height: List[int]) -> int:
        """ Uses a left and right pointer and iterativly moves them closer.
        At each step checks if the current volume is bigger than the saved best result.

        Args:
            height (List[int]): _description_

        Returns:
            int: _description_
        """
        left = 0 
        right = len(height)-1
        current_best = 0

        # while pointers do not point to the same value
        while right != left:
            # get current value 
            current_best = max(current_best, min(height[left], height[right]) * (right-left))

            # move the pointer that provides the least value
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            
        return current_best