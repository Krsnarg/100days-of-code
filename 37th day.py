try:
    l = [1, 5, 6, 7]
    i = int(input("Enter the index: "))
    print(l[i])
    return 0

except:
    print("Some error occurred")
    return 1

finally:
    #  print("I am always excecuted")
    print("I am always excecuted")

    x = func1()
    print(x)

