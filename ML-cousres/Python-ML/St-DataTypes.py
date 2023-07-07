print("Hello, World!")


# //DatAType Python
x = 5
y = "John"
z=1.5
print(type(x))
print(type(y))
print(z)

x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)




# Example	Data Type	Try it
# x = "Hello World"	str	
# x = 20	int	
# x = 20.5	float	
# x = 1j	complex	
# x = ["apple", "banana", "cherry"]	list	
# x = ("apple", "banana", "cherry")	tuple	
# x = range(6)	range	
# x = {"name" : "John", "age" : 36}	dict	
# x = {"apple", "banana", "cherry"}	set	
# x = frozenset({"apple", "banana", "cherry"})	frozenset	
# x = True	bool	
# x = b"Hello"	bytes	
# x = bytearray(5)	bytearray	
# x = memoryview(bytes(5))	memoryview	
# x = None	NoneType



# ||||||||||||||||||||STRING pYthon||||||||||||||||||||

a = "Hello, World!"
print(a[1])


for x in "banana":
  print(x)

  a = "Hello, World!"
print(len(a))

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

  txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

  b = "Hello, World!"
print(b[2:5])


a = "Hello, World!"
print(a.upper())

a = "Hello, World!"
print(a.lower())

a = "Hello, World!"
print(a.replace("H", "J"))

a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']


a = "Hello"
b = "World"
c = a + b
print(c)


#$Escape Character
# txt = "We are the so-called "Vikings" from the north."

# txt = "We are the so-called \"Vikings\" from the north."

#|||||||||||||||String find()

txt = "Hello, welcome to my world."

x = txt.find("welcome")

print(x)



#|||||||||||||||||Python divides the operators in the following groups:

#Arithmetic operators
#Assignment operators
#Comparison operators
#Logical operators
#Identity operators
#Membership operators
#Bitwise operators


#||||||Python Arithmetic Operators


# +	Addition	x + y	
# -	Subtraction	x - y	
# *	Multiplication	x * y	
# /	Division	x / y	
# %	Modulus	x % y	
# **	Exponentiation	x ** y	
# //	Floor division	x // y


#\\\\\Python Assignment Operators|||||||||||

# =	x = 5	x = 5	
# +=	x += 3	x = x + 3	
# -=	x -= 3	x = x - 3	
# *=	x *= 3	x = x * 3	
# /=	x /= 3	x = x / 3	
# %=	x %= 3	x = x % 3	
# //=	x //= 3	x = x // 3	
# **=	x **= 3	x = x ** 3	
# &=	x &= 3	x = x & 3	
# |=	x |= 3	x = x | 3	
# ^=	x ^= 3	x = x ^ 3	
# >>=	x >>= 3	x = x >> 3	
# <<=	x <<= 3	x = x << 3


#Python Comparison Operators|||||||||||||||||??????????'[''''']


# ==	Equal	x == y	
# !=	Not equal	x != y	
# >	Greater than	x > y	
# <	Less than	x < y	
# >=	Greater than or equal to	x >= y	
# <=	Less than or equal to	x <= y


#Python Logical Operators////////////////!SECTION

# and 	Returns True if both statements are true	x < 5 and  x < 10	
# or	Returns True if one of the statements is true	x < 5 or x < 4	
# not	Reverse the result, returns False if the result is true	not(x < 5 and x < 10)	

# ||||||||||||||||||Python Identity Operators||||||||||||||||||||||||||||||


# is 	Returns True if both variables are the same object	x is y	
# is not	Returns True if both variables are not the same object	x is not y


# ||||||||||||||||||||Python Membership Operators//////////////////!SECTION


# in 	Returns True if a sequence with the specified value is present in the object	x in y	
# not in	Returns True if a sequence with the specified value is not present in the object	x not in y



#||||||||||||||||||||||||||||||||||||||||Python Bitwise Operators

# Operator	Name	Description	Example	Try it
# & 	AND	Sets each bit to 1 if both bits are 1	x & y	
# |	OR	Sets each bit to 1 if one of two bits is 1	x | y	
# ^	XOR	Sets each bit to 1 if only one of two bits is 1	x ^ y	
# ~	NOT	Inverts all the bits	~x	
# <<	Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off	x << 2	
# >>	Signed right shift	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off	x >> 2


