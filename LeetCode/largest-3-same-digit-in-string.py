"""
--PROBLEM DETAILS--

2264. Largest 3-Same-Digit Number in String

You are given a string num representing a large integer. An integer is good if it meets the following conditions:

    It is a substring of num with length 3.
    It consists of only one unique digit.

Return the maximum good integer as a string or an empty string "" if no such integer exists.

Note:

    A substring is a contiguous sequence of characters within a string.
    There may be leading zeroes in num or a good integer.

Example:
Input: num = "6777133339"
Output: "777"
Explanation: There are two distinct good integers: "777" and "333".
"777" is the largest, so we return "777".

Acceptance rate: 68.5%
Difficulty: Hard

--SUBMISSION DETAILS--

Status: Accepted
Langauge: Python
Runtime: 30ms (Beats 98.24%)
Memory: 16.3MB (Beats 24.76%)

Values correct as of: 04/12/2023

"""





class Solution:
    def largestGoodInteger(self, num: str) -> str:
        prev_value = ""
        current_run_length = 1
        highest_digit = "-1"
        GOOD_LENGTH = 3
        
        for digit in num:
            if digit == prev_value:
                current_run_length += 1
            else:
                current_run_length = 1
                prev_value = digit

            if current_run_length >= GOOD_LENGTH and int(digit) > int(highest_digit):
                highest_digit = digit
        
        if highest_digit != "-1":
            return highest_digit*3
        else:
            return ""