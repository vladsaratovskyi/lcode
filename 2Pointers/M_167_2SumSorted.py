from typing import List

def main():
    print(Solution().twoSum([2,7,11,15], 9))

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1

        while left < right:
            res = nums[left] + nums[right]
            if res == target:
                return [left + 1, right + 1]
            elif res < target:
                left += 1
            else:
                right -= 1

if __name__ == "__main__":
    main()
