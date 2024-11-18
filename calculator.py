class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        result = 0
        negative = False

        # Handle negative numbers
        if a < 0:
            a = self.subtract(0, a)
            negative = not negative
        if b < 0:
            b = self.subtract(0, b)
            negative = not negative

        count = 0
        while count < b:
            result = self.add(result, a)
            count = self.add(count, 1)

        if negative:
            result = self.subtract(0, result)

        return result

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")

        negative = False

        # Handle negative numbers
        if a < 0:
            a = self.subtract(0, a)
            negative = not negative
        if b < 0:
            b = self.subtract(0, b)
            negative = not negative

        result = 0
        while a >= b:
            a = self.subtract(a, b)
            result = self.add(result, 1)

        if negative:
            result = self.subtract(0, result)

        return result

    def modulo(self, a, b):
        if b == 0:
            raise ValueError("Cannot modulo by zero")

        negative = False

        # Handle negative numbers
        if a < 0:
            a = self.subtract(0, a)
            negative = True
        if b < 0:
            b = self.subtract(0, b)

        while a >= b:
            a = self.subtract(a, b)

        if negative:
            a = self.subtract(0, a)

        return a

# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(1, 2))
    print("Example: subtraction: ", calc.subtract(4, 2))
    print("Example: multiplication: ", calc.multiply(2, 3))
    print("Example: division: ", calc.divide(10, 2))
    print("Example: modulo: ", calc.modulo(10, 3))