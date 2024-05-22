# -----------THIS IS THE COMMON STEP --------------
import logging
import os

# step1: we have to create a logging string
logging_str = "%(asctime)s-%(name)s-%(filename)s-%(funcName)s-%(levelname)s-%(message)s"

# which folder we want to save the log file
log_folder = "logs"
# naming the log file which would be created
log_file = "logs/running_log.log"
# creating the log folder automatically using python
os.makedirs(log_folder, exist_ok=True)

logging.basicConfig(
    level = logging.INFO, 
    format = logging_str,
    handlers=[logging.FileHandler(log_file)]
    )

logger = logging.getLogger("mylog")
# --------------------------------------------------

class Calculator2Number01:
    def __init__(self,num1,num2):
        self.__num1 = num1
        self.__num2 = num2

    def add(self):
        try:
            if (isinstance(self.__num1, (int,float)) and isinstance(self.__num2, (int,float))):
                result = self.__num1 + self.__num2 
                logger.info(f"The Summation is {result}")
                return result
            else:
                raise Exception("Both Number should be interger or float")    #something wrong from here   
                
        except Exception as e:
            logger.error(f"Enter only integer {e}")