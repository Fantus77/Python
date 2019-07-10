import sys
import random

"""

"""
def Main():
	if len(sys.argv) < 2:
		print("Usage: python Sarcasm.py <Words To Translate>")
	else:
		FinalString = ""
		for index in range(1, len(sys.argv)):
			word = sys.argv[index]
			for char in word:
				if random.randint(0,1) == 1:
					FinalString = FinalString + char.upper()
				else:
					FinalString = FinalString + char.lower()
			FinalString = FinalString + ' '
		print(FinalString)
	return



if __name__ == '__main__':
	Main()