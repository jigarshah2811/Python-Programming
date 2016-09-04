class Node:
    def __init__(self, v):
        self.v = v
        self.l = None
        self.r = None


class Serde:
    def serialize(self, s):
        if len(s) < 1:
            return None
        r = Node(s[0])
        q = [r]
        i = 1
        while (len(q) > 0):
            n = q.pop(0)
            if i < len(s):
                n.l = Node(s[i])
                q.append(n.l)
                i += 1
                if i < len(s):
                    n.r = Node(s[i])
                    q.append(n.r)
                    i += 1
        return r

    def deserialize(self, r):
        if r is None:
            return ''
        s = ''
        q = [r]
        i = 0
        while (len(q) > 0):
            n = q.pop(0)
            s += str(n.v)
            if n.l is not None:
                q.append(n.l)
                if n.r is not None:
                    q.append(n.r)
        return s


s = Serde()
r = s.serialize('abcdefghi')
print (s.deserialize(r))
