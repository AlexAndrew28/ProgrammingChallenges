from typing import List

"""
--PROBLEM DETAILS--

2706. Buy Two Chocolates

You are given an integer array prices representing the prices of various chocolates in a store. You are also given a single integer money, which represents your initial amount of money.

You must buy exactly two chocolates in such a way that you still have some non-negative leftover money. You would like to minimize the sum of the prices of the two chocolates you buy.

Return the amount of money you will have leftover after buying the two chocolates. If there is no way for you to buy two chocolates without ending up in debt, return money. Note that the leftover must be non-negative.

Example:

Input: prices = [1,2,2], money = 3
Output: 0
Explanation: Purchase the chocolates priced at 1 and 2 units respectively. You will have 3 - 3 = 0 units of money afterwards. Thus, we return 0.

Acceptance rate: 69.9%
Difficulty: Easy

--SUBMISSION DETAILS--

Status: Accepted
Langauge: Python
Runtime: 51ms (Beats 99.8%)
Memory: 17.2MB (Beats 23.41%)

Values correct as of: 20/12/2023

*- Interesting note for this problem: The method that sorts the list (O(nlogn)) ran quicker than the method that uses 2 variables and loops through the list (O(n))

"""

def buyChocoSorting(prices: List[int], money: int) -> int:
    """ Finds the amount of money you would have left after buying the two cheapest chocolates available. If cannot buy two, returns starting money.

    Args:
        prices (List[int]):  A list of prices of chocolates
        money (int): The amount of money you have initially to buy chocolates

    Returns:
        int: The amount of money you are left with at the end
    """
    # sorts the list
    prices_sorted = sorted(prices)

    # takes the first two items (the two smallest)
    choc_cost = prices_sorted[0] + prices_sorted[1]
    # calculates total cost and returns money left
    if choc_cost < money:
            return money - choc_cost
    else:
        return money
    
def buyChocoLoop(prices: List[int], money: int) -> int:
    """ Finds the amount of money you would have left after buying the two cheapest chocolates available. If cannot buy two, returns starting money.

    Args:
        prices (List[int]):  A list of prices of chocolates
        money (int): The amount of money you have initially to buy chocolates

    Returns:
        int: The amount of money you are left with at the end
    """
    lowest = 0
    second_lowest = 0

    # iterates through the list to find the two smallest items
    for i in prices:
        if i < lowest:
            # new smallest item bumps both smallest and second smallest up
            second_lowest = lowest
            lowest = i
        elif i < second_lowest:
            # new second smallest item bumps only second smallest up
            second_lowest = i

    # calculates total cost and returns money left
    choc_cost = lowest + second_lowest
    if choc_cost <= money:
        return money - choc_cost
    else:
        return money