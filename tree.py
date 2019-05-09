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

	branches(levels, fmove / 2).
	
	
	
	
	
tree(3)
input()