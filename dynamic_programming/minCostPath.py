"""
Given a cost matrix cost[][] and a position (m, n)
in cost[][], write a function that returns cost of
minimum cost path to reach (m, n) from (0, 0).
Each cell of the matrix represents a cost to
traverse through that cell. The total cost of a
path to reach (m, n) is the sum of all the costs
on that path (including both source and destination).
You can only traverse down, right and diagonally
lower cells from a given cell, i.e., from a given
cell (i, j), cells (i+1, j), (i, j+1), and
(i+1, j+1) can be traversed. You may assume that
all costs are positive integers.
"""
# NAIVE Approach
import sys

ROWS = 3
COLUMNS = 3


def min_cost(cost: list, target: tuple) -> int:
    m, n = target
    if n < 0 or m < 0:
        return sys.maxsize
    elif m == 0 and n == 0:
        return cost[m][n]
    else:
        return cost[m][n] + min(
            min_cost(cost, (m - 1, n - 1)),  # Diagonal
            min_cost(cost, (m - 1, n)),  # Right
            min_cost(cost, (m, n - 1))  # Down
        )


# Driver program to test above functions
cost = [[1, 2, 3],
        [4, 8, 2],
        [1, 5, 3]]
print(min_cost(cost, (2, 2)))

"""
It should be noted that the above function computes the
same subproblems again and again. See the following
recursion tree, there are many nodes which appear more
than once. The time complexity of this naive recursive
solution is exponential and it is terribly slow.

mC refers to minCost()

                            mC(2, 2)
                    /            |            \
                    /             |            \
            mC(1, 1)           mC(1, 2)             mC(2, 1)
        /     |     \       /     |     \           /     |     \
        /      |      \     /      |      \         /      |       \
mC(0,0) mC(0,1) mC(1,0) mC(0,1) mC(0,2) mC(1,1) mC(1,0) mC(1,1) mC(2,0)
"""
