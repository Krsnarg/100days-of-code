a = input("Enter the number: ")
print(f"Multiplication table of {a} is: ")

for i in range(1, 11):
    print(f"{int(a)} X {i} = {int(a)*i}")


    print("Some lines of code")
print("End of program")
print("Some imp lines of code")
Exception object
except Exception as e:
print(e)
print("sorry some error occurred")
print("Invalid Input")


try:
    num = int(input ("Enter an interger: "))
    a = [6, 3]
    print(a[num])

except ValueError:
    print("Number entered is not an interger.")

except IndexError:
    print("Index Error")
    
