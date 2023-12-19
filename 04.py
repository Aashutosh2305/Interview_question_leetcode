class solution:

    def maxprofit(self, prices:list[int]):

        n = len(prices)
        minimum = prices[0]
        maxprofit = 0

        for i in range(0,n):

            cost = prices[i] - minimum
            maxprofit = max(maxprofit, cost)
            minimum = min(prices[i], minimum)

        return maxprofit



tata_stockes = solution()
stockes_prices = [7,1,5,3,6,4]
tata_stockes.maxprofit(stockes_prices)
print(tata_stockes.maxprofit(stockes_prices))
