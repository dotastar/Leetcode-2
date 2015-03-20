I)
Say you have an array for which the ith element is the price of a given stock on day i.
If you were only permitted to complete at most one transaction 
(ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        profit = 0; highest = 0
        length = len(prices)
        if length <= 1: return 0
        for i in xrange(length-1,-1,-1):
            highest = max(highest,prices[i])
            profit = max(profit, highest-prices[i])
        return profit 
        
        
II)
Say you have an array for which the ith element is the price of a given stock on day i.
Design an algorithm to find the maximum profit. You may complete as many transactions as you like 
(ie, buy one and sell one share of the stock multiple times). However, you may not engage in multiple 
transactions at the same time (ie, you must sell the stock before you buy again).

The optimization solution is add ALL the profits if Prices[i]>Prices[i-1]
73ms
class Solution:
    # @param prices, a list of integer
    # @return an integer
    # 73ms
    def maxProfit(self, prices):
        length = len(prices)
        if length < 2: return 0
        profit = 0
        for i in xrange(len(prices)-1,0,-1):
            if (prices[i]>prices[i-1]):
                profit += (prices[i]-prices[i-1]) 
        return profit 

III)
Say you have an array for which the ith element is the price of a given stock on day i.
Design an algorithm to find the maximum profit. You may complete at most two transactions.
Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock 
before you buy again).

Analysis:
正向扫一遍, 求出每天的maxProfit放到maxProfitForward里, 再逆向扫一遍, 求出每天的maxProfit放到
maxProfitBackward里, 都是O(N)时间。如果不进行transaction, maxProfit为0。如果只进行一次transaction, 
maxProfit为maxProfitForward[-1]。如果进行两次transaction, 顺序只能是买入->卖出->买入->卖出, 
设第一次卖出发生在前i天, 第二次卖出发生在第i+1天到最后一天之间, 那么maxProfit就是 
maxProfitForward[i-1] + maxProfitBackward[i] 的最大值, 还是O(N)时间。总的时间复杂度是O(N)。

class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if prices == None or prices == []:
            return 0
        
        minV = prices[0]
        length = len(prices)
        f = [ 0 for i in xrange(length)]
        g = [ 0 for i in xrange(length)]
        
        f[0] = 0 
        g[length-1] = 0
        
        for i in xrange(1, length):
            minV = min(minV, prices[i])
            f[i] = max(prices[i]-minV, f[i-1])
            
        maxV = prices[length-1]
        
        for j in xrange(length-2, -1, -1):
            maxV = max(maxV, prices[j])
            g[j] = max(g[j+1], maxV - prices[j])
            
        result = f[length-1]
        for i in xrange(length-1):
            temp = f[i] + g[i+1]
            if temp > result:
                result = temp
        
        return result   
