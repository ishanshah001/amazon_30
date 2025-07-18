def maxProfit(self, prices):
    profit = 0
    buy = prices[0]
    for amt in prices[1:]:
        if buy > amt:
            buy = amt
        elif amt>buy and amt-buy>profit:
            profit = amt - buy
    return profit
    