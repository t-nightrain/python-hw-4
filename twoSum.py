# Завдання 1
from typing import List


def twoSum(nums: List[int], target: int):
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return None


# print(twoSum([1, 2, 3], 4))
# print(twoSum([2, 7, 11, 15], 9))
# print(twoSum([3, 2, 4], 6))
# print(twoSum([3, 3], 6))
# print(twoSum([1, 3, 6, 7], 10))
