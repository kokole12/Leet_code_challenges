#!/usr/bin/python3
"""
    approaching the two sum problem
    given a list and a target value. find two values in the list that
    add up to the targe
    eg:
        input:
            list: [1, 4, 8, 2]
            target: 3
        output: [0, 3]

    solution:
        optimizing the code to minimize on its time complexity
        we are going to check throught the list and get a value at a given index and
        get the difference from the target then check if the difference is available on
        list and then return the two indices
"""


def two_sum(nums, target):
    """ Looping throug the list to get indices"""
    for i in range(len(nums)):
        difference = target - nums[i]
        try:
            diff_index = nums.index(difference, i + 1)
            return [i, diff_index]
        except ValueError as e:
            continue

nums = [1, 4, 8, 2]
target = 3

print(two_sum(nums, target))
