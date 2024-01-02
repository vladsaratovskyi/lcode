from typing import List

def main():
    print(Solution().checkInclusion("adc", "dcda"))

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        start, end = 0, len(s1)
        s1Map, s2Map = {}, {}

        if len(s1) > len(s2):
            return False

        for i in range(len(s1)):
            s1Map[s1[i]] = 1 + s1Map.get(s1[i], 0)
            s2Map[s2[i]] = 1 + s2Map.get(s2[i], 0)

        if s1Map == s2Map:
            return True

        for end in range(len(s1), len(s2)):
            s2Map[s2[start]] -= 1

            if s2Map[s2[start]] == 0:
                del s2Map[s2[start]]

            s2Map[s2[end]] = 1 + s2Map.get(s2[end], 0)

            if s1Map == s2Map:
                return True
            
            start += 1

        return False
        

if __name__ == "__main__": 
    main()
