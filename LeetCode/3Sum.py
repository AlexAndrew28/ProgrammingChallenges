from typing import List

"""
--PROBLEM DETAILS--

15. 3Sum

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Acceptance rate: 33.6%
Difficulty: Medium

--SUBMISSION DETAILS--

Status: Accepted
Langauge: Python
Runtime: 936ms (Beats 79.15%)
Memory: 20.5MB (Beats 44.50%)

Values correct as of: 21/11/2023

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