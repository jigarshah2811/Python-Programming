str = "ABCGRETCABCGR"
k = 3
d = dict()

for i in range(len(str) - 2):
    substr = ""
    for j in range(k):
        substr += (str[i+j])
    # print substr

    try:
        d[substr] += 1
    except KeyError:
        d[substr] = 1

for key, value in list(d.items()):
    if value > 1:
        print(key)
