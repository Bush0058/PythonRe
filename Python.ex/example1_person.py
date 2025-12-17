class Person:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Person(name='{self.name}')"

    def __mul__(self, x):
        if not isinstance(x, int):
            raise TypeError("Argument must be an integer")
        self.name = self.name * x
        return self


p = Person("Tim")
p * 3
print(p)
