import logging
import os


from src.Calculator.calculator02 import Calculator2Number01


if __name__ == "__main__":
    num1 = int(input("Enter the First Number: "))
    num2 = int(input("Enter the Second Number: "))
    
    calc = Calculator2Number01(num1, num2)
    calc.add()
    
    