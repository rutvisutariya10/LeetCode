class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        required = [0] * (amount + 1)
        required[0] = 0
        coins.sort()
        for i in range(1,amount+1):
            minimum = float("inf")
            for coin in coins:
                diff = i - coin
                if diff < 0:
                    break
                minimum = min(minimum,required[diff]+1)
            required[i] = minimum
        
        if required[-1] == float("inf"):
            return -1
        return required[-1]
                    
                
        