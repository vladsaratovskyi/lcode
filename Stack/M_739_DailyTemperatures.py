from typing import List

def main():
    print(Solution().dailyTemperatures([73,74,75,71,69,72,76,73]))

# Monotonic decreasing stack
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        count = 0

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                topTemp, topInd = stack.pop()
                res[topInd] = (i - topInd)
            stack.append([temp, i])

        return res

if __name__ == "__main__": 
    main()
