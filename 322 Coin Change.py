class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        min_coin = [-1 for _ in range(amount + 1)]
        min_coin[0] = 0

        for i in range(amount + 1):
            for coin in coins:
                if i - coin >= 0 and min_coin[i - coin] != -1:
                    if min_coin[i] == -1:
                        min_coin[i] = 1 + min_coin[i - coin]
                    else:
                        min_coin[i] = min(min_coin[i], min_coin[i - coin] + 1)
        return min_coin[amount]
