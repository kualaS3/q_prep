class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        L = 0
        H = len(matrix) - 1
        while H >= L : 
            MID = (H + L) // 2 
            curr = matrix[MID][0]
            if target == curr:
                return True
            if target < curr:
                H = MID - 1
            if target > curr:
                L = MID + 1
        L2 = 0
        H2 = len(matrix[H]) - 1
        while H2 >= L2:
            MID = (H2 + L2) // 2 
            curr = matrix[H][MID]
            if target == curr:
                return True
            if target < curr:
                H2 = MID - 1
            if target > curr:
                L2 = MID + 1
        return False
