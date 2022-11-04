digits = [5,6,7,8]
print("Walk array forward ----> ")
for i, digit in enumerate(digits):    # Walk array forward
    print(f"index: {i}, Digit: {digit}")

print("Walk array backwards <---- ")
for i, digit in enumerate(digits[::-1]):    # Walk array backwards
    print(f"index: {i}, Digit: {digit}")