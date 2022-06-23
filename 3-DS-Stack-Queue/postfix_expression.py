from STACK import Stack
INT_MAX = 65535


def main():
    postFixExpression = ['4', "1", "+", "2.5", "*"]
    postFixExpression = ["5", "80", "40", "/", "*"]

    s = Stack()
    result = ""
    for ele in postFixExpression:
        value = isOperand(ele)
        print(value)
        if value:
            s.push(value)
        else:
            B = s.pop()
            A = s.pop()
            if ele == "+":
                result = A + B
            elif ele == "-":
                result = A - B
            elif ele == "*":
                result = A * B
            elif ele == "/":
                result = A / B
            else:
                raise Exception("Unsupported Operator {}".format(ele))
            s.push(result)
    print("Result of PostFix Expression = {}".format(result))


def isOperator(ele):
    if ele == '+' or ele == '-' or ele == "*" or ele == "/":
        return True
    else:
        return False


def isOperand(ele):
    try:
        # int value
        value = int(ele)
    except ValueError:
        # Float or Operator
        try:
            value = float(ele)
        except ValueError:
            return False

    if 0 < value < INT_MAX:
        return value
    else:
        return False

if __name__ == "__main__":
    main()
