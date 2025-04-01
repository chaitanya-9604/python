'''
a = " a very long string with emails 

emails = []
3 second

a random access memory is volatile and all its contents are lost
oncea program terminates in order to persist the data forever, we use files.

a data stored in a storage device. A python program can talk to the file by
reading content from it or writing content to it.

'''

f = open("C:\\Users\\chait\\Desktop\\python\\chapter 9 file I or O\\file.txt", "r")
data = f.read()
print(data)
f.close()
# use f.close() s a good practice 


