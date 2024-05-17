# Strings are immutable
a = "!!!Harry!! !!!!!!!!!!!!! Harry"
print(len(a))
print(a)
print(a.upper())
print(a.lower())
print(a.rstrip("!"))
print(a.replace("Harry", "John"))
print(a.split(" "))
blogheading = "introduction tO jS"
print(blogHeading.capitalize())

str1 = "Welcome to the Console!!!"
print(len(str1))
print(len(str1.center(50)))
print(a.count("Harry"))

str1 = "Welcome to the Console!!!"


print("Hello world from ...")
os.system ("Python --version")

x = 4
# x is the variable to match
match x:
    # if x is 0
    case 0:
        print("x is zero")
        # case with if-condition
        case _ if x is < 10:
        print("x is < 10")
        # default case(will only be matched if the above cases were not matched)
        # so it is basically just an else:
        case _:
        print(x)

        case 4:
        print("case is 4")

        case _ if x!=90:
        print(x, "is not 90")
        
case _ if x!=80:
print(x, "is not 80")

