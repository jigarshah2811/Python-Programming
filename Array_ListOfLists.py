def depth(l):
    if isinstance(l, list):
        return 1 + max(depth(item) for item in l)
    else:
        return 0


def mul_depth(l, depth):
    global res
    for item in l:
        if not isinstance(item, list):
            res += item * depth
        else:
            mul_depth(item, depth-1)
    return res


def mul_depth_reverse(l, depth):
    global res
    for item in l:
        if not isinstance(item, list):
            res += item * depth
            print res
        else:
            mul_depth_reverse(item, depth+1)

l = [2, [1, 1], [1, 1]]
l = [1, [4, [2]]]
# l = [[1, 1], 2, [1, 1, [4]]]
res = 0
# print mul_depth(l, depth(l))
print mul_depth_reverse(l, 1)
print res
