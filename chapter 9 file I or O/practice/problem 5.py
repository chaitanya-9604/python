word = ["Donkey", "bad", "stupid"]

with open("C:\\Users\\chait\\Desktop\\python\\chapter 9 file I or O\\practice\\file.txt", "r") as f:
    content = f.read()
    
for word in word:
  content = content.replace(word, "*" * len(word)) 

with open("C:\\Users\\chait\\Desktop\\python\\chapter 9 file I or O\\practice\\file.txt", "w") as f:
    f.write(content)

