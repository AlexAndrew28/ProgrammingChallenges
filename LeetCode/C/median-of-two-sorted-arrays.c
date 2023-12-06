#include <stdio.h>
#include <stdbool.h> 

/*
--PROBLEM DETAILS--

4. Median of Two Sorted Arrays

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

Example:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Acceptance rate: 38.5%
Difficulty: Hard

--SUBMISSION DETAILS--

Status: Accepted
Langauge: C
Runtime: 17ms (Beats 33.3%)
Memory: 7.1MB (Beats 60.20%)

Values correct as of: 6/12/2023

*/

/// @brief Finds the median from two seporate sorted arrays by merging them and locating the central value
/// @param nums1 The first sorted array
/// @param nums1Size The length of the first sorted array
/// @param nums2 The second sorted array
/// @param nums2Size The length of the second sorted array
/// @return The median value, if even length the average of the two median values
double findMedianSortedArrays(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    // build a new array with space n+m where n and m are the sizes of the respective arrays
    int mergedArray[nums1Size + nums2Size];

    int nums1Pointer = 0;
    int nums2Pointer = 0;
    int mergedPointer = 0;

    // iterate through the two arrays with two pointers
    while(nums1Pointer < nums1Size || nums2Pointer < nums2Size){
        if(nums1Pointer < nums1Size && (nums2Pointer == nums2Size || *(nums1+nums1Pointer) <= *(nums2+nums2Pointer))){
            // if the value at the pointer in array 1 is smaller than the value at the pointer in array 2
            mergedArray[mergedPointer] = *(nums1+nums1Pointer);
            nums1Pointer ++;
        }
        else{
            // if the value at the pointer in array 2 is smaller than the value at the pointer in array 1
            mergedArray[mergedPointer] = *(nums2+nums2Pointer);
            nums2Pointer ++;
        }

        mergedPointer ++;
    }

    // now that there is a single sorted array can just access the median value
    int mid = (nums1Size+nums2Size) / 2;
    double ans;

    if((nums1Size+nums2Size)% 2 == 0){
        // if even length get average between two median values
        ans = ((double) (mergedArray[mid-1] + (double) mergedArray[mid])) / 2;
    }
    else{
        ans = mergedArray[mid];
    }

    return ans;
}