from typing import List


def left_boundary_binary_search(nums: List[int], target: int) -> bool:
    if not nums:
        return False

    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] <= target:  # 等于时，mid是可以排除的
            left = mid + 1
        else:
            right = mid
    # 结束时,left==mid==right
    return nums[left] > target


def right_boundary_binary_search_wrong1(nums: List[int], target: int) -> bool:
    if not nums:
        return False

    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        """这时候不能向下取整，否则当前长度为2，即left等于mid时，下面这个if可能死循环"""
        if nums[mid] <= target:
            left = mid
        else:
            right = mid - 1


def right_boundary_binary_wrong2(nums: List[int], target: int) -> bool:
    """
    这种方式有局限性，只能用于无重复元素。[0, 1, 1, 1]就会失效
    """
    if not nums:
        return False

    left, right = 0, len(nums) - 1
    while left < right:
        """mid向上取整"""
        mid = (left + right) // 2 + 1
        if nums[mid] <= target:
            left = mid
        else:
            right = mid - 1
    return nums[left] < target


def right_boundary_binary_search(nums: List[int], target: int) -> bool:
    if not nums:
        return False

    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2 + 1
        if nums[mid] < target:
            left = mid
        else:  # 等于时，排除mid
            right = mid - 1
    return nums[left] < target

print(right_boundary_binary_search([0, 1, 1, 1], 1))