import sys # This is used to get the information about the current exception
from src.logger import logging # This is used to log the error message

def error_message_detail(error,error_detail:sys): # This function will return the error message with the file name and line number where the error occurred
    _,_,exc_tb=error_detail.exc_info() # This will get the current exception information
    # exc_info() returns a tuple of three values: the exception type, the exception value, and the traceback object.
    # The traceback object contains information about the call stack at the point where the exception was raised.
    # We are using the _ to ignore the first two values of the tuple, which are not needed for our purpose.
    # The traceback object contains information about the call stack at the point where the exception was raised
    # We are using the exc_tb variable to get the traceback object.
    # The traceback object contains information about the call stack at the point where the exception was raised
    # exc_tb.tb_frame is the frame object for the current function call
    # exc_tb.tb_frame.f_code is the code object for the current function call
    # exc_tb.tb_frame.f_code.co_filename is the name of the file where the current function call was made
    # exc_tb.tb_lineno is the line number where the current function call was made
             
    file_name=exc_tb.tb_frame.f_code.co_filename # This will get the name of the file where the error occurred
    # exc_tb.tb_frame.f_code.co_filename is the name of the file where the current function call was made
    # exc_tb.tb_lineno is the line number where the current function call
    error_message = "Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(
    file_name, exc_tb.tb_lineno,str(error) # This will get the error message

    )
    return error_message # This will return the error message with the file name and line number where the error occurred
    

class CustomeException(Exception): # This is a custom exception class that inherits from the built-in Exception class
        """Custom Exception class for handling exceptions in the application."""
        def __init__(self, error_message, error_detail:sys): # This is the constructor method that initializes the custom exception with an error message and error details
            super().__init__(error_message) # This will call the constructor of the parent class Exception 
            self.error_message = error_message_detail(error_message, error_detail = error_detail) # This will get the error message with the file name and line number where the error occurred

        def __str__(self): # This is the string representation of the custom exception 
            return self.error_message # This will return the error message with the file name and line number where the error occurred
            


#if __name__ == "__main__": # This is the main function that will be executed when the script is run
    #try:
        #a = 1 / 0 # This will raise a ZeroDivisionError
    #except Exception as e: # This will catch the exception and print the error message
        #logging.info("ZeroDivisionError occurred") # This will log the error message
        #raise CustomeException(e, sys) # This will raise the custom exception with the error message and error details


