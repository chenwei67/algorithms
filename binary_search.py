from typing import List


def binary_search(nums: List[int], target: int):
    """二分搜索"""
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1  # 这个"1"必须有，否则当nums[i]=target，可能死循环
        else:
            right = mid - 1  # 这个"1"必须有，否则当target not in nums,可能死循环
    return None  # 未找到

print(binary_search([1,2,3,5], 4))
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
