from typing import List

def main():
    print(Solution().removeDuplicates([1,1,1,2,2,3]))

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l, r = 0, 0

        while r < len(nums):
            span = 1

            while r + 1 < len(nums) and nums[r] == nums[r + 1]:
                span += 1
                r += 1
            
            for i in range(min(2, span)):
                nums[l] = nums[r]
                l += 1
            
            r += 1
            print(nums)
        
        return l
    
if __name__ == "__main__":
    main()
    