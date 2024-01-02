from typing import List

def main():
    print(Solution().search([-1,0,3,5,9,12], 9))

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            middle = left + ((right - left) // 2)
            if nums[middle] < target:
                left = middle + 1
            elif nums[middle] > target:
                right = middle - 1
            else:
                return middle
        return -1

if __name__ == "__main__":
    main()
