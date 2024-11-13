class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        result = 0
        if b < 0:
            b = self.subtract(b, self.add(b,b))
            a = self.subtract(a, self.add(a,a))

        for i in range(b):
            result = self.add(result, a)

        return result

    def divide(self, a, b):
        if b == 0 or a == 0:
            return 0
        
        flag = (a < 0) ^ (b < 0) #XOR
        a = self.multiply(a, -1) if a < 0 else a
        b = self.multiply(b, -1) if b < 0 else b

        result = 0
        while a >= b:
            a = self.subtract(a, b)
            result += 1
        
        if flag:
            result = self.multiply(result, -1)

        return result
    
    def modulo(self, a, b):
        if b == 0:
            return 0
        dividend = self.divide(a,b)
        quotient = self.multiply(dividend, b)
        return self.subtract(a,quotient)

# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(1, 2))
    print("Example: subtraction: ", calc.subtract(4, 2))
    print("Example: multiplication: ", calc.multiply(2, 3))
    print("Example: division: ", calc.divide(10, 2))
    print("Example: modulo: ", calc.modulo(10, 3))