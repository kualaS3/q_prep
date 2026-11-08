class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        # Mid doesn't locate the peak — read the slope at mid instead.
        # If nums[mid] < nums[mid+1] we're going uphill, so a peak is
        # guaranteed to the right and mid itself can't be it (L = mid + 1).
        # Otherwise we're going downhill, so the peak is at mid or to its
        # left (R = mid). Loop while L < R so mid + 1 always exists, and
        # when L == R that one candidate is the peak.
        L = 0
        R = len(nums) - 1
        if len(nums) == 1:
            return 0
        while L < R:
            mid = (L + R) // 2
            if nums[mid] < nums[mid + 1]:  # uphill — peak is right
                L = mid + 1
            else:  # downhill — peak is mid or left
                R = mid
        return (L + R) // 2
