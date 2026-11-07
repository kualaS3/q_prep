class Solution:
    def search(self, nums: list[int], target: int) -> int:
        # At any midpoint, one side of the array is always still sorted.
        # Find the sorted side, check whether the target lives inside its
        # range, and search there; otherwise search the other side.
        LEFT = 0
        RIGHT = len(nums) - 1

        while LEFT <= RIGHT:
            MID = (LEFT + RIGHT) // 2
            if nums[LEFT] <= nums[MID]:  # left half is sorted
                if target >= nums[LEFT] and target < nums[MID]:
                    RIGHT = MID - 1
                else:
                    LEFT = MID + 1
            else:  # right half is sorted
                if target > nums[MID] and target <= nums[RIGHT]:
                    LEFT = MID + 1
                else:
                    RIGHT = MID - 1
            if target == nums[MID]:
                return MID

        return -1
