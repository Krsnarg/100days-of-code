# Strings are immutable
a = "Harry"
print(len(a))
print(a.upper())
print(a.lower())

a = "!!!Harry!!!!!!!!!!!!!!!"
print(a)
print(a.rstrip("!"))

a = "!!!Harry!!!!!!!!!Harry"
print(a.replace("Harry", "John"))

a = "!!!Harry!!!!! !!!!!!!!!!! Harry"
print(a.split(" "))


blogheading = "Introduction to js"
print(blogheading.capitalize( ))

str1 = "Welcome to the Console!!!"
print(str1.center(50))
print(len(str1))
print(a.count("Harry"))

str1 = "Welcome yo the Console !!!"
print(str1.endswith("!!!"))

str1 = "Welcome to the Console !!!"
print(str1.endswith("to", 4, 10))

str1 ="He's name is Dan. He is an honest man."
print(str1.find("ishh"))
# print(str1.index("ishh"))


str1 = "WelcomeToTheConsole"
print(str1.isalnum())
str1 = "Welcome"
print(str1.isalpha())

str1 = "hello world"
print(str1.islower())

str1 = "We wish you a Merry Christmas\n"
print(str1)
print(str1.isprintable())

str1 = "         "         #using spacebar
print(str1.isspace())
str2 = "    "           #using Tab
print(str2.isspace())

str1 = "World Health Organization"
print(str1.istitle())

str2 = "To kill a mocking bird"
print(str2.istitle())

str1 = "Python is a Interpreted Language"
print(str1.startswith("Python"))

str1 = "Python is a Interpreted Language"
print(str1.swapcase())

str1 = "His name is Dan. Dan is a honest man."
print(str1.title())
