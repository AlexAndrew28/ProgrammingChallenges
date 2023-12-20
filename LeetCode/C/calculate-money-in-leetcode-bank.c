#include <stdio.h>

/*
--PROBLEM DETAILS--

1716. Calculate Money in Leetcode Bank

Hercy wants to save money for his first car. He puts money in the Leetcode bank every day.

He starts by putting in $1 on Monday, the first day. Every day from Tuesday to Sunday, he will put in $1 more than the day before. On every subsequent Monday, he will put in $1 more than the previous Monday.

Given n, return the total amount of money he will have in the Leetcode bank at the end of the nth day.

Example:
Input: n = 4
Output: 10
Explanation: After the 4th day, the total is 1 + 2 + 3 + 4 = 10.

Acceptance rate: 76.1%
Difficulty: Easy

--SUBMISSION DETAILS--

Status: Accepted
Langauge: C
Runtime: 2ms (Beats 22.78%)
Memory: 6.22MB (Beats 61.19%)

Values correct as of: 6/12/2023

*/

/// @brief Calculates the total money after n days using a loop
/// @param n The number of days
/// @return The total amount of money at the end of n days
int totalMoney(int n){
    int currentDay = 0;
    int prevMondayAmount = 0;
    int total = 0;

    for (int i = 0; i < n; i++){
        if(currentDay == 0){
            total += prevMondayAmount + 1;
            prevMondayAmount += 1;
        }else{
            total += currentDay + prevMondayAmount;
        }
        currentDay += 1;

        if (currentDay == 7){
            currentDay = 0;
        }
    }

    return total;
}

/// @brief Calculates the total amount of money after n days using maths
/// @param n The number of days
/// @return The total amount of money at the end of n days
int totalMoneyImproved(int n){

    static int TOTAL_WEEK_BASE_MONEY = 28;

    if(n == 0){
        return 0;
    }

    int completeWeeks = n / 7;
    int currentDay = n % 7 + 1;

    int total = (currentDay-1)*currentDay/2 + (currentDay-1) * completeWeeks + completeWeeks * TOTAL_WEEK_BASE_MONEY + 7*(completeWeeks-1)*completeWeeks/2; 

    return total;
}

int main () {
    int total = totalMoneyImproved(6);

    printf("%i", total);
}