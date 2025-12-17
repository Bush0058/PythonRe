class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def __eq__(self, other):
        return self.grade == other.grade


s1 = Student("Hanan", 10)
s2 = Student("Ali", 10)
s3 = Student("Sara", 7)

print(s1 == s2)
print(s1 == s3)
