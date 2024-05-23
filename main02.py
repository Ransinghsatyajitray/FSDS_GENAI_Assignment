import logging
import os


from src.Calculator.calculator02 import Calculator2Number01


if __name__ == "__main__":
    
    # Take the input as it is, in the method conduct the check
    num1 = input("Enter the First Number: ")
    num2 = input("Enter the Second Number: ")
    
    
    calc = Calculator2Number01(num1,num2)
    
    calc.menu()
    

    
    
    
    
   