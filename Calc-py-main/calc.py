import math

class Calculator:
    def display_menu(self):
        print("Calculator Menu:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Power")
        print("6. Square Root")
        print("7. Sine")
        print("8. Cosine")
        print("9. Tangent")
        print("10. Logarithm")
        print("0. Exit")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")

            if choice == "0":
                print("Exiting...")
                break

            try:
                if choice == "1":
                    a = float(input("Enter the first number: "))
                    b = float(input("Enter the second number: "))
                    print("Result:", self.add(a, b))
                elif choice == "2":
                    a = float(input("Enter the first number: "))
                    b = float(input("Enter the second number: "))
                    print("Result:", self.subtract(a, b))
                elif choice == "3":
                    a = float(input("Enter the first number: "))
                    b = float(input("Enter the second number: "))
                    print("Result:", self.multiply(a, b))
                elif choice == "4":
                    a = float(input("Enter the numerator: "))
                    b = float(input("Enter the denominator: "))
                    print("Result:", self.divide(a, b))
                elif choice == "5":
                    a = float(input("Enter the base: "))
                    b = float(input("Enter the exponent: "))
                    print("Result:", self.power(a, b))
                elif choice == "6":
                    a = float(input("Enter the number: "))
                    print("Result:", self.square_root(a))
                elif choice == "7":
                    a = float(input("Enter the angle in radians: "))
                    print("Result:", self.sin(a))
                elif choice == "8":
                    a = float(input("Enter the angle in radians: "))
                    print("Result:", self.cos(a))
                elif choice == "9":
                    a = float(input("Enter the angle in radians: "))
                    print("Result:", self.tan(a))
                elif choice == "10":
                    a = float(input("Enter the number: "))
                    print("Result:", self.log(a))
                else:
                    print("Invalid choice. Please try again.")
            except ValueError as e:
                print("Error:", str(e))
            except ZeroDivisionError:
                print("Error: Cannot divide by zero")

                
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    def power(self, a, b):
        return math.pow(a, b)

    def square_root(self, a):
        if a < 0:
            raise ValueError("Cannot take the square root of a negative number")
        return math.sqrt(a)

    def sin(self, a):
        return math.sin(a)

    def cos(self, a):
        return math.cos(a)

    def tan(self, a):
        return math.tan(a)

    def log(self, a):
        if a <= 0:
            raise ValueError("Cannot take the logarithm of a non-positive number")
        return math.log(a)

if __name__ == "__main__":
    calculator = Calculator()
    calculator.run()


