class Solution:
    def findMin(self, nums: list[int]) -> int:
        # Binary search for the drop: the one place where nums[k] > nums[k+1].
        # At any mid, compare with the right end to tell which chunk mid is in:
        # if nums[mid] > nums[R], mid is in the high chunk and the minimum is
        # to its right. Otherwise mid is in the low chunk and the minimum is
        # at mid or to its left. Stop when L and R are neighbours. The
        # minimum is the smaller of the two.
        L = 0
        R = len(nums) - 1
        while R - L > 1:
            mid = (L + R) // 2
            if nums[mid] > nums[R]:  # min is on the right
                L = mid
            else:
                R = mid
        return min(nums[L], nums[R])
