from typing import List, collections

def main():
    print(Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"]))

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            ans[tuple(count)].append(s)
        return ans.values()

if __name__ == "__main__": 
    main()
