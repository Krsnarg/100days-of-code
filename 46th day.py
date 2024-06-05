import os

os.mkdir("date")

for i in range(0, 100):
    os.mkdir(f"data/Day{i+1}")

    if (os.path.exists()):
      os.mkdir("data")

    if (not os.path.exists("data")):
       os.mkdir("data")

       import os

       for i in range(0, 100):
          os.rename(f"data/Tutorial{i+1}", f"data/Tutorial{i+1}")

          import os
          folders = os.listdir("data")

          print(folders)

          for folder in folders:
             print(folder)

             print(os.listdir(f"data/{folders}"))

             import os
             folders = os.listdir("data")

             print(os.getcwd())
             os.chdir("/Users")
             print(os.getcwd())
             