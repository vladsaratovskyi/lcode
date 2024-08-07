from typing import List

def main():
    print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))

class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = 0
        left, right = 0, len(height) - 1

        while left < right:
            maxHeight = min(height[left], height[right])
            area = max(area, maxHeight * (right - left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return area
         

if __name__ == "__main__":
    main()
