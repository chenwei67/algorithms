from typing import List


""" 
mid ,left, right的关系:
mid向下取整时:
    分普通情况（left < right）和边界条件（left = right）讨论：
        left <= mid < right (left < right, 当且仅当right= left + 1时，左边的等号成立)
        left = mid = right
"""

"""
左右指针确定能收敛到target，即不错过吗?
能
"""


def binary_search_v1(nums: List[int], target: int):
    """二分搜索"""
    left, right = 0, len(nums) - 1
    while left <= right:  # 当left=mid=right的结果可能不满足时需要
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1  # 这个"1"必须有，否则当nums[i]=target，可能死循环
        else:
            right = mid - 1  # 这个"1"必须有，否则当target not in nums,可能死循环
    return None  # 未找到


def binary_search_wrong1(nums: List[int], target: int):
    left, right = 0, len(nums) - 1

    """当 nums[mid]等于target，死循环"""
    while left < right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1


def binary_search_v2(nums: List[int], target: int):
    if not nums:
        return None

    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] >= target:
            right = mid  # right指向大于等于target的值，并且是"归档"的
    # 结束时,left==mid==right
    return nums[left] == target
