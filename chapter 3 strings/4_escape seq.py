
# 1. Quotation Mark Escapes
# Allow you to include quotes inside a string without ending it.

# Escape Sequence	Meaning	Example	Output

# \' -	Single quote (')	
# \" -	Double quote (")	

print("it\'s MODx") # output - it's MODx
print("hello \"moon\"") #output - hello "moon"



# 2. Backslash Escape
# Allows you to include a literal backslash in a string.

# Escape Sequence	Meaning	Example	Output
# \\ -	Backslash (\)	

print("path:MODx\\") # output - path:MODx\


# 3. Whitespace Escape Characters
# Control spacing and formatting of text.

# Escape Sequence	Meaning	Example	Output
# \n	Newline	print("Hello\nWorld")	Hello
# World
# \t	Horizontal Tab	print("A\tB\tC")	A B C
# \r	Carriage Return	print("Hello\rWorld")	World
# \b	Backspace	print("Hell\blo")	Helo

table = "Name\tAge\tCountry\nJohn\t25\tUSA\nAnna\t30\tUK"
print(table)

# output - Name    Age    Country
#          John    25     USA
#          Anna    30     UK


