from typing import List

def main():
    print(Solution().maxProfit([4,2,6,8,0,1]))

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        start, end = 0, 1
        res = 0

        while end < len(prices):
            if prices[start] < prices[end]:
                profit = prices[end] - prices[start]
                res = max(res, profit)
            else:
                start = end
            end += 1
            
        return res

if __name__ == "__main__": 
    main()
