from typing import List

def main():
    print(Solution().removeElement([0,1,2,2,3,0,4,2], 2))

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j = 0

        for i, n in enumerate(nums):
            if n != val:
                nums[j] = nums[i]
                j += 1
        
        print(nums)
        return j

if __name__ == "__main__":
    main()
