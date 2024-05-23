tup = (1, 5, 6)
print(type(tup), tup)
tup (1)
print(type(tup), tup)
tup = (1, 2, 76, 342, 32)
# tup[0] = 90
print(type(tup), tup)

tup = (1, 2, 76, 342, 32, "green", True)
# tup[0] = 90
print(type(tup), tup)
print(tup[0])
print(tup[1])
print(tup[2])
# print(tup[34])
print(tup[-1])


if 3421 in tup:
    print("Yes 342 is present in this tuple")
    tup2 =tup[1:4]
    print(tup2)
    