"STRATEGY: Map (frequency)"
"""
https://www.careercup.com/question?id=5389627422670848
"""


def isomorphic(string1, string2):
    if len(string1) != len(string2):
        return False
    
    map1 = dict()
    map2 = dict()
    for i in range(len(string1)):
        if string1[i] in map1:
            if map1[string1[i]] != string2[i]:
                return False
        if string2[i] in map2:
            if map2[string2[i]] != string1[i]:
                return False
        map1[string1[i]] = string2[i]
        map2[string2[i]] = string1[i]
    return True


# string1 = raw_input("Enter string 1")
# string2 = raw_input("Enter string 2")
print(isomorphic("foo", "app"))
print(isomorphic("foo", "bar"))
print(isomorphic("turtle", "tletur"))
print(isomorphic("ab", "ca"))
