# Time complexity = O(log m + log n)

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # get the possible correct row first
        L1 = 0
        R1 = len(matrix) - 1
        while L1 <= R1:
            i = (L1 + R1) // 2
            curr = matrix[i][0]
            if curr < target:
                L1 = i + 1
            if curr > target:
                R1 = i - 1
            if curr == target:
                return True
        col = L1 - 1
        if col < 0:
            return False

        # now search within the row
        L2 = 0
        R2 = len(matrix[col]) - 1
        while L2 <= R2:
            i = (L2 + R2) // 2
            curr = matrix[col][i]
            if curr < target:
                L2 = i + 1
            if curr > target:
                R2 = i - 1
            if curr == target:
                return True

        return False
