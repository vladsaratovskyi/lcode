from typing import List

def main():
    print(Solution().isPalindrome("a b#ap^a b a"))

class Solution:
    def isPalindrome(self, s: str) -> bool:
        r = len(s) - 1
        l = 0

        while l < r:
            if not s[l].isalnum():
                l += 1
                continue
            if not s[r].isalnum():
                r -= 1
                continue

            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1

        return True  

if __name__ == "__main__":
    main()
