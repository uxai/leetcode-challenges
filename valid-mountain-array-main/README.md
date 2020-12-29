# valid-mountain-array
Check if an array is a mountain
https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/570/week-2-december-8th-december-14th/3561/

Given an array of integers arr, return true if and only if it is a valid mountain array.

Recall that arr is a mountain array if and only if:

    arr.length >= 3
    There exists some i with 0 < i < arr.length - 1 such that:
        arr[0] < arr[1] < ... < arr[i - 1] < A[i]
        arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
        
![Moujntain array diagram](https://github.com/uxai/valid-mountain-array/blob/main/hint_valid_mountain_array.png?raw=true)
