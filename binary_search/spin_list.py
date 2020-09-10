from typing import List


def spin_list(nums: List[int]) -> int:
    left, right = 0, len(nums) - 1
    while left < right:  # 由于一直存在，不需要等号
        mid = (left+right) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid  # 由于一定存在，所以可以没有"1"
    print(nums[left])
    return nums[left]


spin_list([1, 2, 3, 4, 0])
spin_list([0, 1, 2, 3, 4])
spin_list([4, 5, 6, 1, 2])
