"""
minimumAbsDifference.py

Code
Code
Code Sample
Testcase
Testcase
Test Result
1200. Minimum Absolute Difference
Solved
Easy
Topics
premium lock icon
Companies
Hint
Given an array of distinct integers arr, find all pairs of elements with the minimum absolute difference of any two elements.

Return a list of pairs in ascending order(with respect to pairs), each pair [a, b] follows

a, b are from arr
a < b
b - a equals to the minimum absolute difference of any two elements in arr
"""

def minimumAbsDifference(arr):
    sorted_arr = sorted(arr)
    min_abs_diff = 100
    for i in range(1, len(arr), len(arr)):
        temp_min_abs_diff = abs(sorted_arr[i] - sorted_arr[i-1])
        if min_abs_diff > temp_min_abs_diff:
            min_abs_diff = temp_min_abs_diff
    result = []
    for i in range(1, len(arr)):
        if (sorted_arr[i] - sorted_arr[i-1]) == min_abs_diff: 
            result.append([sorted_arr[i-1], sorted_arr[i]])
    
    return result

output = minimumAbsDifference([40,11,26,27,-20])
print(output)