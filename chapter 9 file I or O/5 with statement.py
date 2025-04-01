f = open("modx.txt")
print(f.read())
f.close()

# best way to open & close a file automatically is a with statement 

with open("modx.txt") as f:
    print(f.read())

