word = "Donkey"

with open("C:\\Users\\chait\\Desktop\\python\\chapter 9 file I or O\\practice\\file.txt", "r") as f:
    content = f.read()

contentNew = content.replace("Donkey", "#####") 

with open("C:\\Users\\chait\\Desktop\\python\\chapter 9 file I or O\\practice\\file.txt", "w") as f:
    content = f.write(contentNew)

