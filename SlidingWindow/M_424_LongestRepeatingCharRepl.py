from typing import List
import operator

def main():
    print(Solution().characterReplacement("AABABBA", 1))

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charMap = {}
        start, end = 0, 0
        maxLen = 0
        maxF = 0

        for end in range(len(s)):
            charMap[s[end]] = 1 + charMap.get(s[end], 0)
            maxF = max(maxF, charMap[s[end]])

            while (end - start + 1) - maxF > k:
                charMap[s[start]] -= 1
                start += 1

            maxLen = max(maxLen, end - start + 1)
        
        return maxLen
        

if __name__ == "__main__": 
    main()
