import math


"""
import turtle

myturtle = turtle.Turtle()
myturtle.circle(50)
myturtle.getscreen()

"""

"""
DRAW DIAMOND
"""
"""
N = 19
sol = [[1] * N for row in xrange(N)]

print sol

width = 0
for row in xrange(N):
    for col in xrange(N):
        if col == N/2:
            print width
            sol[row][col - width] = 0
            sol[row][col + width] = 0
            if row < N/2:
                width += 1
            else:
                width -= 1

for row in sol:
    print row
"""
"""
DRAW Circle: given radius
http://quiz.geeksforgeeks.org/draw-circle-without-floating-point-arithmetic/

Solution:
Consider a square from -r to +r
Check for each point if that belongs within circumference (X^2 + Y^2 <= R^2)
"""
r = 5
for i in xrange(-r, r+1):
    for j in xrange(-r, r+1):
        # Check if this point in circumeference belongs to Circle
        if (i*i + j*j) <= (r*r) + 1:
            print "*",
        else:
            print " ",
        print " ",
    print "\n"
