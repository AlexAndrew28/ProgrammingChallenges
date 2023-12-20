"""
--PROBLEM DETAILS--

44. Wildcard Matching

Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*' where:

    '?' Matches any single character.
    '*' Matches any sequence of characters (including the empty sequence).

The matching should cover the entire input string (not partial).

Example:
Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Acceptance rate: 27.4%
Difficulty: Hard

--SUBMISSION DETAILS--

Status: Accepted
Language: Python
Runtime: 50ms (Beats 95.36%)
Memory: 16.19MB (Beats 97.53%)

Values correct as of: 21/11/2023

"""



class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """ Uses two pointers, one for the pattern and one for the string. Advances them both following the set rules until either
        the pattern does not match or it reaches the end of the string. If the pattern does not match but there is a star in the 
        pattern the program backtracks to the star and increases the number of characters it matches to. 

        Args:
            s (str): The string
            p (str): The pattern

        Returns:
            bool: True if the string fits the pattern
        """
        string_pointer = 0
        pattern_pointer = 0

        star_index = -1
        star_string_pos = 0


        while string_pointer < len(s):

            # reach the end of the pattern but not the string -> backtrack to a star and try and make the star represent more of the string
            if pattern_pointer == len(p):
                if star_index == -1:
                    return False
                else:
                    # increase what the star covers
                    string_pointer = star_string_pos
                    pattern_pointer = star_index
                    star_string_pos += 1
            # save this position as a star and move on (dont advance the string as a star can represent empty string)
            elif p[pattern_pointer] == "*":
                star_index = pattern_pointer + 1
                star_string_pos = string_pointer
                pattern_pointer += 1
            
            # advance both pattern and string
            elif p[pattern_pointer] == "?":
                string_pointer += 1
                pattern_pointer += 1
                
            # must be a letter if not a * or ?
            else:
                # check if can advance the string and pattern
                if p[pattern_pointer] == s[string_pointer]:
                    string_pointer += 1
                    pattern_pointer += 1
                else:
                    # if cannot advance, try and backtrack to a star
                    if star_index == -1:
                        return False
                    else:
                        string_pointer = star_string_pos
                        pattern_pointer = star_index
                        star_string_pos += 1
                 
        # since * can represent empty string need to check if there are trailing * at the end of the pattern not used up       
        while pattern_pointer < len(p):
            if p[pattern_pointer] == "*":
                pattern_pointer += 1
            else:
                break
            
        # if used the whole pattern then it must match
        if pattern_pointer == len(p):
            return True
        else:
            return False