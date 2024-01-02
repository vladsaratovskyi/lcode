from typing import List, collections

def main():
    print(Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"]))

class Solution:
    def groupAnagrams(self, strings: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)

        for string in strings:
            count = [0] * 26
            for char in string:
                count[ord(char) - ord("a")] += 1
            ans[tuple(count)].append(string)
        return ans.values()

if __name__ == "__main__": 
    main()
