"""
Sum of 2 odd numbers would be an even:
IsEven(): %2 to morph 1 value to true/false
Weighted Avg = Cost to reach each ele of list / number of ele in list


Hash Functions have to be made equality otherwise it won't work
Math Rule: x == y, then Hash(x) == Hash(y)

The equivivelence class is defined by HashFunc() not the objects consuming HashFunc()
"""

"""
def match(x, elem):
    if x is elem:               return True     # Compares ID of Objects
    if x.hash != elem.hash:     return False    # Compare hash of Objects
    return x == elem
"""
s = [10, 20, 30, 50, 40, 91]
even_odd = [[10, 18, 30, 12], [5, 27, 41, 39]]
wrong_even_odd = [[10, 18, 30, 12, 91], [5, 27, 41, 39]]

x = 39.0


def hash_func(x):
    return int(x % 2)
    # return int(x) & 1             # optimized way to find even/odd


print(x) in s                       # To find an element is O(n) = 5,  But weighted Avg cost = 3

x = 18
print(x) in even_odd[hash_func(x)]    # To find an element is O(n) = 4,  But weighted Avg cost = 2

x = 91
print(x) in even_odd[hash_func(x)]  # Goes to WRONG Hash
