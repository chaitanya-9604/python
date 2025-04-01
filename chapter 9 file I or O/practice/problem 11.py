with open("C:\\Users\\chait\\Desktop\\python\\chapter 9 file I or O\\practice\\old.txt") as f:
    content = f.read()

with open("C:\\Users\\chait\\Desktop\\python\\chapter 9 file I or O\\practice\\this_copy.txt", "w") as f:
    f.write(content)

