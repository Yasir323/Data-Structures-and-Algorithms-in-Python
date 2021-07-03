"""
Given a value N, if we want to make change for N
cents, and we have infinite supply of each of
S = { S1, S2, .. , Sm} valued coins, how many ways
can we make the change? The order of coins doesn’t
matter.
"""
# NAIVE APPROACH


def coin_change(coins: list, n: int, target: int) -> int:
    # If target is 0, we don't need to give any coins
    if target == 0:
        return 1

    # If it is less than 0, this is not possible
    # If the no of coins is less than 0, return 0
    if target < 0 or n <= 0:
        return 0

    return coin_change(coins, n - 1, target) + \
        coin_change(coins, n, target - coins[n - 1])



arr = [1, 2, 3]
m = len(arr)
print(coin_change(arr, m, 4))

"""
C() --> count()
                             C({1,2,3}, 5)
                           /             \
                         /                 \
             C({1,2,3}, 2)                 C({1,2}, 5)
            /       \                      /      \
           /         \                    /         \
C({1,2,3}, -1)  C({1,2}, 2)        C({1,2}, 3)    C({1}, 5)
               /    \             /     \           /     \
             /       \           /       \         /        \
    C({1,2},0)  C({1},2)   C({1,2},1) C({1},3)    C({1}, 4)  C({}, 5)
                   / \     / \        /\         /     \
                  /   \   /   \     /   \       /       \
                .      .  .     .   .     .   C({1}, 3) C({}, 4)
                                               / \
                                              /   \
                                             .      .
Since same suproblems are called again, this problem
has Overlapping Subprolems property. So the Coin
Change problem has both properties of a dynamic
programming problem. Like other typical Dynamic
Programming(DP) problems, recomputations of same
subproblems can be avoided by constructing a
temporary array table[][] in bottom up manner.
"""
