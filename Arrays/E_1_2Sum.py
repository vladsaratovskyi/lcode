from typing import List

def main():
    print(Solution().twoSum([4,2,6,8,0,1], 7))

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i

if __name__ == "__main__":
    main()
