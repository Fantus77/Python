import turtle as tt

"""
def branches(levels, fmove):
	if levels >= 2:
		tt.left(45)
		tt.forward(fmove)
		if levels == 3:
			branches(levels, fmove / 2)
		tt.forward(-fmove)
		tt.right(90)
		tt.forward(fmove)
		if levels == 3:
			branches(levels, fmove / 2)
		tt.forward(-fmove)
	
def tree(levels):
	start = 90
	fmove = 100
	tt.left(start)
	tt.forward(fmove)

	branches(levels, fmove / 2)
"""
"""
# This makes a "Y" tree and leaves the turtle perpendicular to the left branch
def branches():
	halfturn = 45
	fullturn = 90
	fmove = 100
	tt.left(fullturn)
	tt.forward(fmove)
	tt.left(halfturn)
	tt.forward(fmove / 2)
	tt.forward(-fmove / 2)
	tt.right(fullturn)
	tt.forward(fmove / 2)
	tt.forward(-fmove / 2)

	def tree(length):
	tt.forward(length)
	tt.left(45)
	level1(length / 2)
	tt.right(90)
	level1(length / 2)
	tt.left(45)
	tt.forward(-length)
"""


def tree(length, levels):
	tt.forward(length)
	if levels >= 2:
		tt.left(45)
		tree(length / 2, levels - 1)
		tt.right(90)
		tree(length / 2, levels - 1)
		tt.left(45)
	tt.forward(-length)

def orientation():
	tt.left(90)
	tt.speed(100)




"""
First function called should set up a counter that increments every time it is run until the value of the counter matches the value of 'levels'.

But what do I do in the case of when the counter == levels? Should it run or stop there? I guess it should run and then NOT increment. How to do that?

Function that is called from the first function should make the branches. The math to do this might just destroy my brain, cause I hate math.

EZ
"""

orientation()
tree(100, 12)



#branches()
#tree(3)
input()