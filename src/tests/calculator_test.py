import unittest
from calculator.calculator import Calculator

class StubIO:
    def __init__(self):
        self.inputs = []
        self.outputs = []

    def read(self, text=""):
        return self.inputs.pop(0)

    def write(self, output):
        self.outputs.append(output)

    def set_inputs(self, inputs: list):
        self.inputs = inputs + ["exit"]

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.io = StubIO()
        self.calculator = Calculator(self.io)

    def test_exit_expression_quits(self):
        self.io.set_inputs(["exit"])

        self.calculator.start()

        output = self.io.outputs[5]

        self.assertEqual(output, "Exiting...")
    
    def test_invalid_operation_error(self):
        self.io.set_inputs(["5"])

        self.calculator.start()

        output = self.io.outputs[5]

        self.assertEqual(output, "Invalid Input")

    def test_sum_calculation(self):
        self.io.set_inputs(["1", "1", "1"])

        self.calculator.start()

        output = self.io.outputs[5]

        self.assertEqual(output, "1.0 + 1.0 = 2.0")

    def test_subtract_calculation(self):
        self.io.set_inputs(["2", "1", "1"])

        self.calculator.start()

        output = self.io.outputs[5]

        self.assertEqual(output, "1.0 - 1.0 = 0.0")

    def test_multiply_calculation(self):
        self.io.set_inputs(["3", "3", "7"])

        self.calculator.start()

        output = self.io.outputs[5]

        self.assertEqual(output, "3.0 * 7.0 = 21.0")

    def test_divide_calculation(self):
        self.io.set_inputs(["4", "24", "3"])

        self.calculator.start()

        output = self.io.outputs[5]

        self.assertEqual(output, "24.0 / 3.0 = 8.0")
        
    def test_next_calculation(self):
        self.io.set_inputs(["1", "1", "1", "yes"])

        self.calculator.start()

        output = self.io.outputs[6]

        self.assertEqual(output, "Select operation:")
        
    def test_invalid_number_error(self):
        self.io.set_inputs(["1", "Not a number"])

        self.calculator.start()

        output = self.io.outputs[5]

        self.assertEqual(output, "Invalid input. Please enter a number.")
        