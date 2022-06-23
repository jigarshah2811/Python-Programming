class solution():
    def PermutationLowerUpper(self, s):
        if len(s) <= 0:
            return []

        def recurPermutationLowerUpper(s, pos, res):
            # Base case
            if pos >= len(s):
                finalres.append(s)
                return finalres

            # Breath
            for i in range(len(s)-1):
                # Is safe
                if s[pos].isdigit():
                    res.append(s[pos])
                    pos += 1
                else:
                    s[pos] = s[pos].lower()
                    res = recurPermutationLowerUpper(s, pos+1, res)

                    s[pos] = s[pos].upper()
                    recurPermutationLowerUpper(s, pos + 1, res)

        finalres = []
        finalres = recurPermutationLowerUpper(s, 0, [])
        return finalres


s = solution()
s = "a1b2"
print(s.PermutationLowerUpper(s))
