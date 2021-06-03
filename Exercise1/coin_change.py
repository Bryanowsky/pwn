# You are given coins of different denominations and a total amount of money amount.
# Write a function to compute the fewest number of coins that you need to make up that amount.
# If that amount of money cannot be made up by any combination of the coins, return -1.
#
# Example 1:
#
# Input: coins = [1, 2, 5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1
#
# Example 2:
#
# Input: coins = [2], amount = 3
# Output: -1
# Note:
# You may assume that you have an infinite number of each kind of coin.


# To solve this problem we can use recursion to create every possible solution to this situation but it could imply
# a lot of operation and even sometimes resolve the same problem n times, is not efficient so we could use DP instead.

# To use DP the choices are the coins, we want the minimum number of coins.


class Solution:
    def coin_change(self, coins: [int], amount: int) -> int:
        coins_required = [amount+1] * (amount + 1)
        coins_required[0] = 0
        for index in range(1, amount+1):
            for coin in coins:
                if coin <= amount:
                    coins_required[index] = min(1+coins_required[index-coin], coins_required[index])
        if coins_required[-1] > amount:
            return -1
        return coins_required[-1]


solution = Solution()
print(solution.coin_change([1, 2, 5, 10, 20], 7452))
