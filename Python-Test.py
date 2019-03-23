# My First Python File
""" To document code
you can use a docstring
by typing text between three double-quotes"""

if 5 < 6:               # If loop example
    print("woot")

swords = ["Kokiri", "Master", "Big Goron"] # Array example

for x in swords:       # For loop example
    print(x)


# Variable declaration below

x = 5               # variable names can be one letter or multiple
myNumber = 5        # python automatically detects what type of variable it is

# Example of number types
    # You can check a variables type with "print(type(variable))"

exampleNumber1 = 5      # Python recognizes as an int type  (can be infinitely long, positive or negative)
exampleNumber2 = 5.1    # Python recognizes as a float type (having decimal)
exampleNumber3 = 5j     # Python recognizes as a complex number (j is always the imaginary piece)


# Casting a variable type
    # You can set a variables type with the following functions

exampleNumber4 = int(5.362)         # Although Python recognizes 5.362 as a float, it will round down to an int
exampleNumber5 = int("3")           # Python sees this as a string, but as long as it is still a number, it will be converted

exampleNumber6 = float(1)           # Python will convert to decimal style (1.0)

exampleString1 = str(3)             # Python will change to a string: "3"
exampleString2 = str(2.275)         # Python will change to a string: "2.275"

# For strings, you can use "double quotes" or 'single quotes'. Both work fine

# Each string init on python creates an array

myString = "I like cookies"         # The array created can be called as shown below
print(myString[3])                  # This will print "i" because "i" is the third letter. Whitespace is ignored

# You can also print pieces of a string (in the syntax, the second number is which character should not be included in calling)

print(myString[5:12])               # This will print "cookies" because characters 5 through 11 are represented as cookies in the string array

# Extra whitespace removal is possible too

myOtherString = "    Hi   "
print(myOtherString.strip())        # The .strip function removes whitespace at the beginning or end of a String. Call it with stringName.strip()   This will print "Hi"

# You can also find the length of a string (based on number of characters with whitespace included)

print(len(myOtherString))           # The len() function helps determine length of a string. use as len(variableName)

# There are functions to change if strings are entered as lowercase or uppercase

print(myOtherString.upper())        # This will print myOtherString as if it were type with CAPS LOCK turned on

print(myOtherString.lower())        # This will take all capital letters in string and make them lowercase

# You can replace parts of a string with the replace function

print(myOtherString.replace("i", "e"))      # This will change the string from "   Hi   " to "   He   "

# The split function changes the string into two other strings based on where the split will occur

myBetterString = "Hello good sir"
mySplitBetterString = myBetterString.split("good")
print(mySplitBetterString)                  # This prints ["Hello "," sir"] because it cuts out good and makes new strings out of the remaining parts


# Human input
    # You can ask the user for input

print("Enter Identification Code:")         # Sets the question for the user to answer
myInput = input()                           # Asks for user input
print("New Identification Code set as:" + myInput)      # Prints the string based off of user input



# Python Arithmatic Operators
    # + (add), - (subtract), * (multipy), / (divide), % (modulus (remainder)), ** (exponent), // (floor division?)

# Python Assignment Operators (col(1) = operator, col(2) = syntax use, col(3) = what operator will do)
"""
=	x = 5	x = 5	
+=	x += 3	x = x + 3	
-=	x -= 3	x = x - 3	
*=	x *= 3	x = x * 3	
/=	x /= 3	x = x / 3	
%=	x %= 3	x = x % 3	
//=	x //= 3	x = x // 3	
**=	x **= 3	x = x ** 3	
&=	x &= 3	x = x & 3	
|=	x |= 3	x = x | 3	
^=	x ^= 3	x = x ^ 3	
>>=	x >>= 3	x = x >> 3	
<<=	x <<= 3	x = x << 3
"""

# Python Comparison Operators
    # == (equals), != (not equal), > (greather than), < (less than), >= (greater than or equal), <= (less than or equal)

# Python Logical Operators (doesn't use symbols like java, just uses words)
    # or (if x or y == true:), and (if x and y == true:), not (if not(x and y == true):)

# Python Identity Operators 
    # is (returns true if two variables are equal (x is y)), is not (returns false if two variables are equal (x is not y))
    # if x is not y:... if x is y:...

# Python Membership Operators
    # in (returns true if variable is present in sequence), not in (returns true if variable is not present in sequence)
    # x = ["woot", "yeet"]
    # if "woot" in x: (returns true)   if "flarp" not in x: (returns true)

# Python Bitwise Operators (don't really know what this is)
"""
& 	AND	Sets each bit to 1 if both bits are 1
|	OR	Sets each bit to 1 if one of two bits is 1
^	XOR	Sets each bit to 1 if only one of two bits is 1
~ 	NOT	Inverts all the bits
<<	Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off
>>	Signed right shift	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off
"""


# Python arrays
    # four types (list - tuple - set - dictionary)


# Python lists
    # Python lists (defined by a square bracket) are ordered and changeable (most likely meaning each entry has a specified number, and you can add entries too it with other code)
myFavoriteFruitsList = ["Strawberry", "Raspberry", "Blueberry"]     # declares the list
print(myFavoriteFruitsList[2])      # to call, use listName[numberAssignedToEntry]. This will print "Blueberry"

# Python lets you change parts of a list
myFavoriteFruitsList[2] = "Mango"   # This will take away "Blueberry" from the list above (since it is the second placement), and replace it with "Mango"
print(myFavoriteFruitsList[2])      # This prints "Mango"

# You can print every item in a list too (for loops are discovered later)
for x in myFavoriteFruitsList:
    print(x)

# Python can check if certain objects are in a list
if "Raspberry" in myFavoriteFruitsList:             # This will print the first option because raspberry is "in" myFavoriteFruitsList
    print("Yay! Raspberry is a favorite fruit!")
else:
    print("Darn, Raspberry is not represented.")

# You can use the len() function to tell how many objects are in a list
print(len(myFavoriteFruitsList))    # This will print "3" because there are 3 fruits listed in myFavoriteFruitsList

# To add items to a list, you can use append(nameOfEntry). This will put newEntry at the highest numbered index in the list
myFavoriteFruitsList.append("Blueberry")    # This makes a new index for blueberry, making 4 fruits

# To add items at a specific index, you can use insert(indexPosition, entryName)
myFavoriteFruitsList.insert(1, "Apple")     # This will put "Apple" where "Raspberry" was, and move all entries with a higher index than one up one place

# You can remove items based off of their entryName with remove(entryName)
myFavoriteFruitsList.remove("Strawberry")   # This removes Strawberry from the list

# You can remove items based off of specific index numbers with pop(indexNumber). If no index number is given, it will remove the latest entry
myFavoriteFruitsList.pop(2)                 # This will remove whatever fruit is in the 2nd index

# Python has a del keyword that can be used too
del myFavoriteFruitsList[1]     # This will have the same occurrence as myFavoriteFruitsList.pop(1)

# The clear function will remove all entries from the list
myFavoriteFruitsList.clear()    # All entries in this list have been cleared, if I were to print this list, it would give no favorite fruits

# The list() constructor can also be used to make a list
myFavoriteFruitsList = list(("Strawberry", "Raspberry", "Blueberry", "Apple"))


# The tuple type of array is ordered and UNCHANGABLE. It is declared with parentheses
myFavoriteGamesTuple = ("Zelda", "League of Legends", "Exploding Kittens")

# To call a piece of a tuple, you still need to use square brackets []
print(myFavoriteGamesTuple[0])      # This will print "Zelda"

# Even if you tried to add or subtract pieces to a tuple, the computer will ignore it
myFavoriteGamesTuple[1] = "Football"    # If I printed myFavoriteGamesTuple[1], it would print "League of Legends"

# Like with lists, you can print every entry in a tuple with a for loop
for x in myFavoriteGamesTuple:      # This will print every object in myFavoriteGamesTuple
    print(x)

# Python can check if an item exists with...
if "Exploding Kittens" in myFavoriteGamesTuple:
    print("Exploding Kittens is a favorite game!")

# Python can check the length of a tuple with the len() function
print(len(myFavoriteGamesTuple))   # will print "3" because there are 3 objects in the tuple

# You cannot add or delete objects to a tuple

# you can delete the entire tuple with the del keyword
del myFavoriteGamesTuple    # the tuple now no longer exists. The computer will give an error if you try to call it

# you can make a tuple with the tuple() constructor
myFavoriteGamesTuple = tuple(("Zelda", "League of Legends", "Exploding Kittens"))   # My tuple exists again!

# some of the built-in functions for tuples include count() (tells how many times a value occurs in the tuple) and index() (Searches for a value and returns its index)


# Python sets are declared below. They use curly braces {} and are unordered but changeable
myCarSet = {"Sienna", "Corolla", "Civic"}

# Since sets are unordered, there is no index value to any of the entries. You need to call with a for loop
for x in myCarSet:
    print(x)

