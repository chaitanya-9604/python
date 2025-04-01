with open("C:\\Users\\chait\\Desktop\\python\\chapter 9 file I or O\\practice\\file.txt") as f:
    content1 = f.read()

with open("C:\\Users\\chait\\Desktop\\python\\chapter 9 file I or O\\practice\\poem.txt") as f:
    content2 = f.read()

if (content1 == content2):
    print("yes these files are isentical")
else:
    print("no these files are not identical")
