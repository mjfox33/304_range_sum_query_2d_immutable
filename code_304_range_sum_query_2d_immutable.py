class NumMatrix:
    def __init__(self, matrix: list[list[int]]):
        self.matrix = matrix
        self.n = len(matrix)
        self.m = len(matrix[0])
        self.prefix_sum = [ [0]*self.m for _ in range(self.n) ]
        for row in range(self.n):
            for col in range(self.m):
                self.prefix_sum[row][col] += self.matrix[row][col]
                if row > 0:
                    self.prefix_sum[row][col] += self.prefix_sum[row-1][col]
                if col > 0:
                    self.prefix_sum[row][col] += self.prefix_sum[row][col-1]
                if row > 0 and col > 0:
                    self.prefix_sum[row][col] -= self.prefix_sum[row-1][col-1]
        return None

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        result = self.prefix_sum[row2][col2]
        if col1 > 0:
            result -= self.prefix_sum[row2][col1-1]
        if row1 > 0:
            result -= self.prefix_sum[row1-1][col2]
        if col1 > 0 and row1 > 0:
            result += self.prefix_sum[row1-1][col1-1]
        return result


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)