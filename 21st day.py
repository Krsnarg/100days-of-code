def average():
    print("The average is ", (a+b)/2)

    average()

    def average(a=9, b=1):
        print("The average is ", (a,b)/2)

        # average(4, 6)
        average(5)

        average(b = 9)

        def name(fname, mname = "John", lname = "Whatson"):
            print("Hello,", fname, mname, lname)

            name("Amy", "Agarwal", "Jain")


            def average(a, b, c=1):
                print("The average is ", (a+ b+ c)/2)

                # average(4, 6)
                # average(b=9)

                average(5, 6)

                def average(*numbers):
                    for i in numbers:
                        sum = sum + i
                        print("Average is: ", sum/len(numbers))
                        sum = 0
                        # print(type(numbers))

                        def name(**name):
                            print("Hello,", name["fname"], name["mname"], name["lname"])

                            name(mname = "Buchanan", lname = "Barnes", fname = "James")

                            print(type(name))

                # print("Average is: ", sum / len(numbers))
                # return 7
                return sum / len(numbers)
            
            