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
        applying brute force method to solve the problem where we get one element from
        the list and add it to every other element on the list
"""


def two_sum(nums, target):
    """ looping to get the first element for addition to other elements"""
    for i in range(len(nums)):
        """ looping again through the list to get the next elements"""
        for j in range(i + 1, len(nums)):
            sum_of_two = nums[i] + nums[j]
            if sum_of_two ==  target:
                return [i, j]


nums = [1, 4, 8, 2]
targe = 3

print(two_sum(nums, targe))
