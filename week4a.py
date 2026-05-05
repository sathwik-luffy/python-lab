class Calculator:

    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        if b == 0:
            return "Cannot divide by zero"
        return a / b


class Scientific(Calculator):

    def fact(self, n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * self.fact(n - 1)


ob = Calculator()

print("Add:", ob.add(1, 2))
print("Sub:", ob.sub(1, 2))

sc = Scientific()

print("Mul:", sc.mul(2, 3))
print("Div:", sc.div(6, 2))
print("Factorial:", sc.fact(5))