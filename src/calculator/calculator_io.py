class CalculatorIO:
    def read(self, text):
        input_expression = input(f"{text}")
        return input_expression
    
    def write(self, output):
        if output is not None:
            print(output)

calculator_io = CalculatorIO()