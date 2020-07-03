name = input()
last_name = input()
birth_year = input()


class Student:

    def __init__(self, x, y, z):
        self.name = x
        self.last_name = y
        self.birth_year = z
        # calculate the id here
        # self.id = name[0] + last_name + birth_year

    def id(self):
        print(self.name[0] + self.last_name + self.birth_year)
    # def get_id(self):

# j = Student("John", "Smith", "1989")
# print(j.id)


std = Student(name, last_name, birth_year)
std.id()