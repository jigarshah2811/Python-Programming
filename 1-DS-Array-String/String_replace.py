def reverseString(str):
    low = 0
    high = len(str)-1
    while low < high:
        str[low], str[high] = str[high], str[low]
        low += 1
        high -= 1
    return str

str = "Hello String"
print(reverseString(str))