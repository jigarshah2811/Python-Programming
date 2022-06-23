n = 20

squares = [i**2 for i in xrange(n)]

print "The sum of square is %d"  % sum(squares)

def cube(x):
    return x**3

print map(cube, range(n))
