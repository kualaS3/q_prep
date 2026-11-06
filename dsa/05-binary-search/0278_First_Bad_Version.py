# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        good, bad = 1, n
        while good < bad :
            curr = (good + bad) // 2
            if isBadVersion(curr) :
                bad = curr
            else :
                good = curr + 1
        return bad
