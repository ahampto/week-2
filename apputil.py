import numpy as np


# update/add code below ...

def ways(amount, coins):
    dp = [0] * (amount + 1)
    dp[0] = 1 # base case
    for coin in coins:
        for i in range(coin, amount + 1): # when using range always have to add 1 to iterate through all/ strat iteration after base case
            dp[i] += dp[i - coin]
    return dp[amount] #returns the end amount dp[12]
ways(12, [1,5])

def lowest_scores(name, score):
    low = np.argmin(score)
    return name[low]

def sort_names(name, score):
    dicter = {n:s for n, s in zip(name, score)}
    dicter = dict(sorted(dicter.items(), key=lambda x: x[1], reverse=True))
    for _ in dicter.keys():
        print(_)