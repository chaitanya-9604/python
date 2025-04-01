f = open("C:\\Users\\chait\\Desktop\\python\\chapter 9 file I or O\\practice\\poem.txt")

content = f.read()
if ("twinkle"in content ):
    print("the word twinkle is present in the content")

else:
    print("the word twinkle is not present in the content")

f.close()
