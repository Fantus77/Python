import turtle as tt

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
	tt.speed(1)



orientation()
tree(100, 5)
input()