class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            if nums[l] == val:
                if nums[r] == val:
                    r -= 1
                    nums.pop()
                    continue
                else: 
                    n = nums[r] 
                    nums[r] = nums[l]
                    nums[l] = n
                    r -= 1
                    nums.pop()
            l += 1
        

        return len(nums)
