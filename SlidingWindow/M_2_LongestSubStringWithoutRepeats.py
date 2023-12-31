from typing import List
import operator

def main():
    print(Solution().lengthOfLongestSubstring("pwwkew"))

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        start = 0
        maxSub = 0

        for end in range(len(s)):
            if s[end] not in charSet:
                charSet.add(s[end])
                maxSub = max(maxSub, end - start + 1)
            else:
                while s[end] in charSet:
                    charSet.remove(s[start])
                    start += 1
                charSet.add(s[end])
                maxSub = max(maxSub, end - start + 1)

        return maxSub
        

if __name__ == "__main__": 
    main()
