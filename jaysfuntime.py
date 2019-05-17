
string1 = "My time is very important"
string2 = "My time is not very fun"
string3 = "My time is going really fast"

def StringCut(string):
    StringToCutOut = "My time is "
    if len(string) < len(StringToCutOut):
        return ""
    for CharacterIndex in range(0, len(StringToCutOut)):
        if StringToCutOut[CharacterIndex] != string[CharacterIndex]:
            return ""

    return string[len(StringToCutOut):]


#string 1 passed to StringCut should result in "very important" being returned
#test case 1
print(StringCut(string1) == "very important")

#test case 2
print(StringCut(string2) == "not very fun")

#test case 3
print(StringCut(string3) == "going really fast")

"""
SWIZZLE THIS
print(string1[3:5])
print(string2[:4])
print(string3[6:])
print(string3[-2])
"""
