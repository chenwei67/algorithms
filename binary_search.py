from typing import List


def binary_search(nums: List[int], target: int):
    """二分搜索"""
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return None  # 未找到
