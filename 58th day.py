# Class Person:
name = "Harry"
occ = "Developer"

def info(self):
    print(f"{self.name} is a {self.occ}")


   # a = Person()
  # print(a.name)
  # a.name = "Divya"
  # a.occ = "HR"
  # a.info()


  # Class Person:

  def __init__(self):
    print("Hey I am a Person")
    # self.name = name

    def __init__(self, n, o):
        print("Hey I am a Person")
        self.name = n
        self.occ = o

        a = Person("Harry", "Developer")
        b = Person("Divya", "HR")
        c = Person(1,2,3)
        a = info()
        b = info()
        # print(a.name)
        # a.name = "Divya"
        