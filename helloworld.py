"""
Defined "hello_world" to accept arguments and change what is printed to the screen based on what is passed
"""
def hello_world(OptionSelect):
	# <- This is an octothorpe
	if OptionSelect == 1:
		print("High")
	elif OptionSelect == 2:
		print("Low")
	else:
		print("Nice Try")
	#print("end of function")


#hello_world(1)
GlobalX = 42
GlobalY = 222
def Scope101(GlobalZ):
#	print(GlobalX)
	print(GlobalY)
	print(GlobalZ)
	GlobalX = 250
	
	
def Cast101(IntString):
	StringToCast = IntString
	print(type(StringToCast))
	StringToCast = int(StringToCast)
	print(type(StringToCast))


#IncomingInput = input()

def Fcast101(InFloat):
	FloatToCast = InFloat
	print(type(FloatToCast))
	FloatToCast = int(FloatToCast)
	print(type(FloatToCast))
	print(FloatToCast)

"""
Fcast101(-10.1)
print("First One Down")
Fcast101(2.2)
print("Second One Down")
Fcast101(2.7)
print("Third One Down")
"""



def recursionExample(count):
	print(count)
	if count <= 0:
		return
	else:	
		recursionExample(count - 1)
		
recursionExample(100)

#print(GlobalX)
#Scope101(1000000)
#print(GlobalX)

"""
GlobalX = 42
GlobalY = 222
From within the function Scope101
GlobalX = 42
GlobalY = 222
GlobalY = 5000
There are two variables with the same name that exist.
Which one do we print?
choose the one at the closest scope to the current executing code.
	That would be the GlobalY function parameter
"""