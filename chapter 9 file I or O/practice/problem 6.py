with open("C:\\Users\\chait\\Desktop\\python\\chapter 9 file I or O\\practice\\log.txt") as f:
   content = f.read()

if ("python" in content):
    print("Python is present")
else:
    print("Python is not present")

