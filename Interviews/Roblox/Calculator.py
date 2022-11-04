class Solution:
    def calculate(self, s):
        num, sign, res = 0, 1, 0
        stack = []
        
        for c in s:     # Parse each char from string
            match c:
                case " ":
                    continue                
                # Calc result upon + or -
                case "+" | "-":
                    if num:
                        res += int(num) * sign 
                    
                    # Prepare for next iteration, RESET num & sign
                    num  = ""
                    sign = 1 if c == "+" else -1
                    
                                        
                case "(":   # Push last res, sign on stack to retrive in future
                    stack.append((res, sign))
                    
                    # RESET everything... Prepare for next iteration
                    num, sign, res = 0, 1, 0
                    
                case ")":
                    # Calc res till now
                    if num:
                        res += int(num) * sign
                    print(f"res at start: {res}")
                    
                    # pop last res, sign from stack and calc latest res                    
                    lastRes, sign = stack.pop()
                    # Add (sign -) / Remove (sign +) this res FROM last result 
                    lastRes += res * sign
                    res = lastRes
                    
                    print(f"res at end: {res}, lastRes: {lastRes}, lastSign: {sign} ")
                    # RESET everything... Prepare for next iteration
                    num, sign = 0, 1

                case _:
                    if c.isdigit():
                        num += c
                        
        # Flush out last num, sign
        if num:
            res += int(num) * sign
        return res