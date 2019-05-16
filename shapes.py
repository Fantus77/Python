import turtle

# Shape functions live here

def square():
	turtle.forward(100)
	turtle.left(90)
	turtle.forward(100)
	turtle.left(90)
	turtle.forward(100)
	turtle.left(90)
	turtle.forward(100)

def diamond():
	turtle.left(45)
	turtle.forward(100)
	turtle.left(90)
	turtle.forward(100)
	turtle.left(90)
	turtle.forward(100)
	turtle.left(90)
	turtle.forward(100)

def triangle():
	turtle.forward(100)
	turtle.left(135)
	turtle.forward(150)
	turtle.left(90)
	turtle.forward(150)
	turtle.left(135)
	turtle.forward(120)

# Main functions to make menu and selections

def runme():
	restart = True
	while restart == True:
		print("Please select which shape you would like to see:")
		print("1 - Square")
		print("2 - Diamond")
		print("3 - Triangle")
		print("4 - Exit")
		restart = choice(input())

def choice(input):
	selection = float(input)
	if selection == 1:
		square()
		return True
	elif selection == 2:
		diamond()
		return True
	elif selection == 3:
		triangle()
		return True
	elif selection == 4:
		exit
	elif selection < 1:
		print("Not a valid selection, try again...")
		return True
	elif selection > 4:
		print("Not a valid selection, try again...")
		return True

runme()
