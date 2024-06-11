with open('file.txt', 'r') as f:
    print(type(f))
    # Move to the 10th byte in the file
    f.seek(10)

    # Read the next 5 bytes
    data = f.read(5)
    print(data)

   # Harry is a good boy

  # 123456789tet

print(f.tell())

with open('file.txt', 'w') as f:
    f.write('Hello World3!')
    f.truncate(5)

    with open('sample.txt', 'r') as f:
        print(f.read())

