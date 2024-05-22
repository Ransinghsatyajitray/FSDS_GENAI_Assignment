from src.Calculator.calculator01 import Calculator2Numbers


# 1. Printing result in console

if __name__ == "__main__":
    calc = Calculator2Numbers(10,20)
    print(f"The addition is {calc.add()}")
    print(f"The subtraction is {calc.sub()}")
    print(f"The division is {calc.div()}")
    print(f"The mul is {calc.mul()}")
