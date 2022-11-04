def reverseWords(text: str) -> str:
    rs = ""

    start = 0
    for end, c in enumerate(text):
        if c == " ":    # End of this word
            if start == end:
                start = end+1
                continue
            w = reverseStr(text[start:end])
            rs += w     # reversed word
            rs += " "   # space
            start = end+1   # RESTART for next word
    
    # Last word will not have hit space, so reverse taht as wwell
    w = reverseStr(text[start:])
    rs += w
    # rs += " " # No space for last word

    # Reverse entire string now
    return reverseStr(rs)


    """ reverseStr: Given a str, returns a reversed string """
def reverseStr(text: str) -> str:
    """TypeError: 'str' object does not support item assignment
    Convert string into List for index operations!
    """
    text = list(text)
    start, end = 0, len(text)-1
    while start < end:
        text[start],text[end] = text[end], text[start]
        start += 1
        end -= 1
    return "".join(text)    # Convert List to Str back!

text = "Apple is Banana"
print(reverseWords(text))
text = "   Apple is Banana"     # leading spaces
print(reverseWords(text))
text = "Apple is Banana       "    # trailing spaces
print(reverseWords(text))

