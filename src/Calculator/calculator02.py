# -----------THIS IS THE COMMON STEP --------------
import logging
import os

# step1: we have to create a logging string
logging_str = "%(asctime)s-%(name)s-%(filename)s-%(funcName)s-%(levelname)s-%(message)s"

# which folder we want to save the log file
log_folder = "logs"
# naming the log file which would be created
log_file = "running_log.log"
# creating the log folder automatically using python
os.makedirs(log_folder, exist_ok=True)

logging.basicConfig(
    level = logging.INFO, 
    format = logging_str,
    handlers=[logging.FileHandler(os.path.join(log_folder, log_file)), 
              logging.StreamHandler()]  # For showing in console
    )

logger = logging.getLogger()
# --------------------------------------------------

class Calculator2Number01:
    def __init__(self, num1, num2):
        self.__num1 = num1
        self.__num2 = num2
        
        
    def menu(self):
        user_input = input(    
        """    
        Hi how can i help you?

        1. Press 1 to addition
        2. Press 2 to subtraction
        3. Press 3 to division
        4. Press 4 to multiplication
        5. Press 5 to absolute difference
        6. Press 6 to Exit
        """
        )
        
        if user_input == "1":
            self.add()
            
        if user_input == "2":
            self.sub()
            
        if user_input == "3":
            self.div()
        
        if user_input == "4":
            self.mul()
        
        if user_input == "5":
            self.modu()
            
        if user_input == "6":
            exit()
                     


    def add(self):
        try:
            # This step is required as the entry is number/float as a character
            if (isinstance(float(self.__num1), float) and isinstance(float(self.__num2), float)):
                result = float(self.__num1) + float(self.__num2)
                logger.info(f"The Summation is {result}")
                return result
            else:
                raise Exception()     
                
        except Exception as e:
            logger.error(f"Enter only integer or float {e}") #{e} is for error message
            
            
    
    def sub(self):
        try:
            # This step is required as the entry is number/float as a character
            if (isinstance(float(self.__num1), float) and isinstance(float(self.__num2), float)):
                result = float(self.__num1) - float(self.__num2)
                logger.info(f"The Subtraction is {result}")
                return result
            else:
                raise Exception()     
                
        except Exception as e:
            logger.error(f"Enter only integer or float {e}") #{e} is for error message
            
            
            
    def div(self):
        try:
            # This step is required as the entry is number/float as a character
            if (isinstance(float(self.__num1), float) and isinstance(float(self.__num2), float) and float(self.__num2) != 0 ):
                result = float(self.__num1) / float(self.__num2)
                logger.info(f"The Division is {result}")
                return result
            else:
                raise Exception()     
                
        except Exception as e:
            logger.error(f"Enter only integer or float and denominator should not be 0 : {e}") #{e} is for error message                


    def modu(self):
        try:
            # This step is required as the entry is number/float as a character
            if (isinstance(float(self.__num1), float) and isinstance(float(self.__num2), float)):
                result = abs(float(self.__num1) - float(self.__num2))
                logger.info(f"The absolute difference is {result}")
                return result
            else:
                raise Exception()     
                
        except Exception as e:
            logger.error(f"Enter only integer or float: {e}") #{e} is for error message                
        
