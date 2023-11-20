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

Acceptance rate: 33.6%
Difficulty: Medium

--SUBMISSION DETAILS--

Status: Accepted
Langauge: Python
Runtime: 936ms (Beats 79.12%)
Memory: 20.49MB (Beats 43.98%)

Values correct as of: 20/11/2023

"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """Sort the list and the iterates through the list using two additional pointers (a high and low) to find 
        combinations of values that add to make zero.

        Args:
            nums (List[int]): A list of integers

        Returns:
            List[List[int]]: A list of all the combinations of values from the input list that add to make zero
        """
        nums.sort()

        solutions = []

        for index in range(len(nums)):
            # if the lowest number is bigger than zero then will not add to make zero
            if nums[index] > 0:
                break
            
            # checks if the current value is the same as the preious - if it is then skip this iteration as we dont want duplicates
            if index == 0 or nums[index] != nums[index -1]:
                low_ptr = index + 1
                high_ptr = len(nums) -1 
                
                while low_ptr < high_ptr:
                    # if too big then move the high pointer down
                    if nums[index] + nums[low_ptr] + nums[high_ptr] > 0:
                        high_ptr -= 1
                    # if too small then move the low pointer up
                    elif nums[index] + nums[low_ptr] + nums[high_ptr] < 0:
                        low_ptr += 1
                    else:
                        solutions.append([nums[index], nums[low_ptr], nums[high_ptr]])
                        
                        # as with before dont want duplicate values - skip over them
                        prev_low_value = nums[low_ptr]
                        prev_high_value = nums[high_ptr]
                        
                        while low_ptr < high_ptr and nums[low_ptr] == prev_low_value:
                            low_ptr += 1
                            
                        while low_ptr < high_ptr and nums[high_ptr] == prev_high_value:
                            high_ptr -= 1


        return solutions