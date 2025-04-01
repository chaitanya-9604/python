
with open("C:\\Users\\chait\\Desktop\\python\\chapter 9 file I or O\\practice\\log.txt") as f:
   lines = f.readlines()

lineno = 1
for line in lines:
   
   if ("python" in line):
      print(f"Python is present. line no: {lineno}")
      break
   lineno += 1

else:
  print("Python is not present")


