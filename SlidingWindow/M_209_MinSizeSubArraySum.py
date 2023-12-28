from typing import List

def main():
    print(Solution().minSubArrayLen(7, [2,3,1,2,4,3]))

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minLen, current = 0, 0
        start, end = 0, 0

        for end in range(len(nums)):
            current += nums[end]

            while current >= target:
                if minLen == 0:
                    minLen = end - start + 1

                current -= nums[start]
                minLen = min(minLen, end - start + 1)
                start += 1


        return minLen
            

if __name__ == "__main__": 
    main()
