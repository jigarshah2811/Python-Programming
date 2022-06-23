"""
Original = AaaabddddddddddddddddddddddA
Encoded  = Aa3bd22A
Decoded  = AaaabddddddddddddddddddddddA
"""


def encode(str):
    i = 0
    result = ""

    result += str[i]
    i += 1

    while i < len(str):

        # Detect repeatation
        repeat = 0
        while str[i] == str[i-1]:
            repeat += 1
            i += 1
        if repeat:
            result += "{}".format(repeat+1)

        # No repeatation
        result += str[i]
        i += 1

    return result if len(result) < len(str) else str


def decode(str):
    i = 0
    result = ""

    result += str[i]
    i += 1

    while i < len(str):

        # Detect repeatation
        digit = ""
        while str[i].isdigit():
            digit += str[i]
            i += 1
        repeat = int(digit) if digit != "" else 0

        if repeat:
            result += str[i-len(digit)-1] * (repeat-1)

        # Pure copy
        result += str[i]
        i += 1

    return result if len(result) > len(str) else str


def main():
    # original = "AaaabdddA"
    original = "AaaabddddddddddddddddddddddA"
    # original = "abcd"

    encoded = encode(original)
    print(encoded)

    decoded = decode(encoded)
    print(decoded)

    assert(original == decoded)

if __name__ == "__main__":
    main()