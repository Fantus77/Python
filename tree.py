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
def branches(fmove):
	if counter == 1:
		



def tree(levels):
	counter = 0
	halfturn = 45
	fullturn = 90
	fmove = 100
	tt.left(fullturn)
	tt.forward(fmove)
	if counter < levels:
		branches(fmove)
		counter = counter + 1
		tree()
	elif counter == levels:
		branches(fmove)






"""
First function called should set up a counter that increments every time it is run until the value of the counter matches the value of 'levels'.

But what do I do in the case of when the counter == levels? Should it run or stop there? I guess it should run and then NOT increment. How to do that?

Function that is called from the first function should make the branches. The math to do this might just destroy my brain, cause I hate math.

EZ
"""




tree(3)
input()