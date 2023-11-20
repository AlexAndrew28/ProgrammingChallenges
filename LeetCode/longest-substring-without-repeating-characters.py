"""
--PROBLEM DETAILS--

3. Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without repeating characters.

Example:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Acceptance rate: 32.2%
Difficulty: Medium

--SUBMISSION DETAILS--

Status: Accepted
Langauge: Python
Runtime: 54ms (Beats 85.14%)
Memory: 16.4MB (Beats 16.92%)

Values correct as of: 20/11/2023

"""

class Solution:
    def lengthOfLongestSubstring(self, input_string: str) -> int:
        """ Uses a dictionary to keep track of the index of each unique characters and iterates through the string finding the longest
        gap between occurances of the same character

        Args:
            input_string (str): The string to find the longest substring with no repeating characters within 

        Returns:
            int: The length of the longest substring
        """
        string_length = len(input_string)

        if string_length == 0:
            return 0
        
        letter_dict = {}
        max_len = 0
        start = 0 
        for index in range(string_length):
            # check if current letter is in dict and start is smaller than current value of letter
            if letter_dict.get(input_string[index], None) is not None and start <= letter_dict[input_string[index]]:
                # increment the value of start to 1 more than current letter value
                start = letter_dict[input_string[index]] + 1
            else:
                max_len = max(max_len, index-start+1)

            letter_dict[input_string[index]] = index

        return max_len