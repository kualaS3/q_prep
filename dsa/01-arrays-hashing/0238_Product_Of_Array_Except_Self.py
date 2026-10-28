class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        # idea is to instantiate with the product "left" side of every index
        # and then include the product of the "right" side after
        right, left = 1, 1
        answer = [1] * len(nums)
        for i in range(len(nums)):
            answer[i] *= left
            left *= nums[i]
        for j in range(len(nums)-1, -1, -1):
        # if len(nums) = 10, range = 9, 8, 7, 6... 1, 0
            answer[j] *= right
            right *= nums[j]
        
        return answer         
