class Polynomial:
    def __init__(self, coeffs):
        self.coeffs = coeffs

    def __repr__(self):
        return "Polynomial({})".format(self.coeffs)

    def __add__(self, other):
        return Polynomial([
            x + y for x, y in zip(self.coeffs, other.coeffs)
        ])

    def __len__(self):
        return len(self.coeffs)

    def __call__(self, x):
        result = 0
        for power, coeff in enumerate(self.coeffs):
            result += coeff * (x ** power)
        return result


p1 = Polynomial([1, 2, 3])   # 1 + 2x + 3x^2
p2 = Polynomial([3, 4, 5])   # 3 + 4x + 5x^2

print(p1)
print(p1 + p2)
print(len(p1))
print(p1(2))
