from typing import List

def main():
    print(Solution().findMaxAverage([1,12,-5,-6,50,3], 4))

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxAverage, current = float('-inf'), 0
        start, end = 0, 0

        for end in range(len(nums)):
            current += nums[end]

            if k == (end - start + 1):
                maxAverage = max(maxAverage, current / (end - start + 1))
                current -= nums[start]
                start += 1
        
        return maxAverage

if __name__ == "__main__": 
    main()
