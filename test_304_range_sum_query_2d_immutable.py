from code_304_range_sum_query_2d_immutable import NumMatrix
def test_example_1():
    num_matrix = NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]])
    r0 = num_matrix.sumRegion(2,1,4,3)
    assert r0 == 8

    r1 = num_matrix.sumRegion(1,1,2,2)
    assert r1 == 11

    r2 = num_matrix.sumRegion(1,2,2,4)
    assert r2 == 12