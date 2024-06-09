# READING A FILE

f = open('myfile.txt', 'r')
# print(f)
text = f.read()
print(text)
f.close()

f = open('myfile.txt')
print(f)

# WRITING A FILE

f = open('myfile.txt', 'w')
f.write('Hello, world!')
f.close()
# Hello, world!Hello, world!Hello, world!

with open('myfile.txt', 'a'):
    f.write("Hey I am inside with")

# Hello, world!Hello, world!Hello, world!Hey I am inside with
