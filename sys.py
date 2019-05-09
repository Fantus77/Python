import sys
sys.argv

#print(len(sys.argv))

"""
print(sys.argv[0])

for string in sys.argv:
	print(string)

"""
	
index = 0
while index < len(sys.argv):
	print(sys.argv[index])
	index = index + 1
	print(index)