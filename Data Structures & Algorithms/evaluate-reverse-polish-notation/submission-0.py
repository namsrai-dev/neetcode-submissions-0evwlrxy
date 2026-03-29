class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        idx = 2
        opers = ["*", "/", "-", "+"]
        while len(tokens) > 2:
            if tokens[idx] in opers:
                if tokens[idx] == "*":
                    tokens[idx-1] = int(tokens[idx-2]) * int(tokens[idx-1])
                    tokens.pop(idx)
                    tokens.pop(idx-2)
                elif tokens[idx] == "/":
                    tokens[idx-1] = int(tokens[idx-2]) / int(tokens[idx-1])
                    tokens.pop(idx)
                    tokens.pop(idx-2)
                elif tokens[idx] == "-":
                    tokens[idx-1] = int(tokens[idx-2]) - int(tokens[idx-1])
                    tokens.pop(idx)
                    tokens.pop(idx-2)
                elif tokens[idx] == "+":
                    tokens[idx-1] = int(tokens[idx-2]) + int(tokens[idx-1])
                    tokens.pop(idx)
                    tokens.pop(idx-2)
                idx -= 1
            else:
                idx +=1
        return int(tokens[0])