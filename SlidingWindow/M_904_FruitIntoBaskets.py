from typing import List

def main():
    print(Solution().totalFruit([1,2,3,2,2]))

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        baskets = {}
        start, end = 0, 0
        maximum = 0

        for end in range(len(fruits)):
            if len(baskets) < 2 and not fruits[end] in baskets:
                baskets[fruits[end]] = True
                maximum = max(maximum, end - start + 1)
            elif fruits[end] in baskets:
                maximum = max(maximum, end - start + 1)
            else:
                baskets = {}
                baskets[fruits[end]] = True
                baskets[fruits[end - 1]] = True
                start = end - 1

                while fruits[start] == fruits[start - 1]:
                    start -= 1

        return maximum

if __name__ == "__main__": 
    main()
