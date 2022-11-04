def permParan_util(sol, open, close, pairs):
    # Base case
    # Print pairs when all open & close are used
    if open == 0 and close == 0:
        print sol
        return

    # If open available, consume it
    if open > 0:
        sol += '('
        permParan_util(sol, open-1, close, pairs)
        sol = sol[:-1]

    # If close doesn't create invalid combination, consume it
    if close > open:
        sol += ')'
        permParan_util(sol, open, close-1,  pairs)
        sol = sol[:-1]


def permParan(pairs):
    sol = ""
    permParan_util(sol, pairs, pairs, pairs)

n = 3
print permParan(n)


