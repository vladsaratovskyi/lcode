from typing import List

def main():
    print(Solution().evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            match token:
                case "+":
                    val2 = stack.pop()
                    val1 = stack.pop()
                    stack.append(val1+val2)
                case "-":
                    val2 = stack.pop()
                    val1 = stack.pop()
                    stack.append(val1-val2)
                case "*":
                    val2 = stack.pop()
                    val1 = stack.pop()
                    stack.append(val1*val2)
                case "/":
                    val2 = stack.pop()
                    val1 = stack.pop()
                    stack.append(int(val1/val2))
                case _:
                    stack.append(int(token))
                        
        return stack.pop()

if __name__ == "__main__": 
    main()
