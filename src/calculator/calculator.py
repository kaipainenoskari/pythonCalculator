from calculator.calculator_io import calculator_io

class Calculator:

    def __init__(self, io=calculator_io):
        self.io = io
        self.expression = ""
        self.inputs = []
        self.outputs = []

    # This function adds two numbers
    def add(self, x, y):
        return x + y

    # This function subtracts two numbers
    def subtract(self, x, y):
        return x - y

    # This function multiplies two numbers
    def multiply(self, x, y):
        return x * y

    # This function divides two numbers
    def divide(self, x, y):
        return x / y

    def start(self):
        while True:
            self.io.write("Select operation:")
            self.io.write("1.Add")
            self.io.write("2.Subtract")
            self.io.write("3.Multiply")
            self.io.write("4.Divide")
            user_input = self.io.read("Enter choice(1/2/3/4): ")
            if user_input == "exit":
                self.io.write("Exiting...")
                break
            if user_input in ('1', '2', '3', '4'):
                try:
                    num1 = float(self.io.read("Enter first number: "))
                    num2 = float(self.io.read("Enter second number: "))
                except ValueError:
                    self.io.write("Invalid input. Please enter a number.")
                    continue

                if user_input == '1':
                    self.io.write(f"{num1} + {num2} = {self.add(num1, num2)}")

                elif user_input == '2':
                    self.io.write(f"{num1} - {num2} = {self.subtract(num1, num2)}")

                elif user_input == '3':
                    self.io.write(f"{num1} * {num2} = {self.multiply(num1, num2)}")

                elif user_input == '4':
                    self.io.write(f"{num1} / {num2} = {self.divide(num1, num2)}")
                
                # check if user wants another calculation
                # break the while loop if answer is no
                next_calculation = self.io.read("Let's do next calculation? (yes/no): ")
                if next_calculation != "yes":
                    break
            else:
                self.io.write(self, "Invalid Input")
                        