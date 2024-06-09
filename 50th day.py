# Harry bhai python course is great

f = open('myfile.txt', 'r')
while True:
    line = f.readline()
    if not line:
        break
    print(line)

    print(line, type(line))
    break

# Harry bhai python course is great
# And this tutorial is also awesome
# This is also good

56, 45, 67
12, 34, 63
13, 64, 23

f = open('myfile.txt', 'r')
i = 0
while True:
    i = i + 1
    line = f.readline()
    m1 = f.split(",")[0]
    m2 = f.split(",")[1]
    m3 = f.split(",")[2]
    print(f"Marks of student {i} in Maths is: {m1}")
    print(f"Marks of student {i} in English is: {m1}")
    print(f"Marks of student {i} in SST is: {m1}")
    if not line:
        break
    print(line)

    while True:
        i = i + 1
        line = f.readline()
        if not line:
            break
        m1 = int(line.split(",")[0])
        m2 = int(line.split(",")[1])
        m3 = int(line.split(",")[2])
        print(f"Marks of student {i} in Maths is: {m1*2}")
        print(f"Marks of student {i} in English is: {m2*2}")
        print(f"Marks of student {i} in SST is: {m3*2}")
        print(line)
        
        f = open('myfile2.txt', 'w')
        lines = ['line 1\n', 'line 2\n', 'line 3\n']
        f.writelines(lines)
        f.close()
        