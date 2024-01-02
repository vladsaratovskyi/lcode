from typing import List

def main():
    print(Solution().threeSum([-1,0,1,2,-1,-4]))

class Solution:
    def threeSum(self, nums: List[int]) -> List[int]:
        res = []
        nums.sort()

        for i, n in enumerate(nums):
            if i > 0 and nums[i - 1] == n:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                threeSum = n + nums[left] + nums[right]
                if threeSum == 0:
                    res.append([n, nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                elif threeSum < 0:
                    left += 1
                else:
                    right -= 1
        return res

if __name__ == "__main__":
    main()
