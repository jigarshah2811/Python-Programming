def InterLeavedStrings_Recur(str1, str2, i, j, res):
    # Base Case
    if i >= len(str1) and j >= len(str2):
        print "".join(res)
        return

    # Consume str1 till available
    if i < len(str1):
        res.append(str1[i])
        InterLeavedStrings_Recur(str1, str2, i + 1, j, res)
        res.remove(str1[i])

    # If str1 is consumed
    # Consume str2 till available
    if j < len(str2):
        res.append(str2[j])
        InterLeavedStrings_Recur(str1, str2, i, j + 1, res)
        res.remove(str2[j])


def InterLeavedStrings(str1, str2):
    res = []
    return InterLeavedStrings_Recur(str1, str2, 0, 0, res)
    

def PermParan_Recur(l, r, total, string):
    # Base case
    # When all left and right paran are consumed
    if l == 0 and r == 0:
        print "".join(string)
        return

    # Breath 2 pos combination, consume l paran or consume r paran

    # Consume l when available
    if l > 0:
        string.append("(")
        PermParan_Recur(l - 1, r, total, string)
        string.remove("(")

    # Consume r when at-least > l being consumed
    if r > l:
        string.append(")")
        PermParan_Recur(l, r - 1, total, string)
        string.remove(")")


def PermParan(total):
    return PermParan_Recur(total, total, total, [])


str1 = "AB"
str2 = "CD"
print InterLeavedStrings(str1, str2)

str1 = "((("
str2 = ")))"
print InterLeavedStrings(str1, str2)

print PermParan(5)
