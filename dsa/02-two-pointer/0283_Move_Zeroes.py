class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        '''
        i = 0
        for n in nums:
            if n == 0: 
                nums.append(n)
                nums.remove(nums[i])
            i += 1
        '''
        l = 0
        for r in range(len(nums)):
            if nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
