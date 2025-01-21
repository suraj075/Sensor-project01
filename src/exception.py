#the sys module in Python helps you interact with the Python program itself and the computer it’s running on. It’s like a toolbox to control or get information about the program.
import sys


def error_message_detail(error, error_details: sys):
    """
    Extracts detailed error information.

    :param error: The error/exception instance.
    :param error_details: The sys module to get exception info.
    :return: A formatted string with detailed error information.
    """
    _, _, exc_tb = error_details.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    error_message = f"Error occurred in script: {file_name} at line: {line_number} - {str(error)}"
    return error_message

# error_details.exc_info() gives details about the current exception.
# exc_tb contains information about where the error occurred in the program.
# exc_tb.tb_frame gives the frame where the exception occurred.
# tb_frame.f_code.co_filename extracts the name of the file where the error happened.
# exc_tb.tb_lineno gives the line number in the file where the error occurred.



# Custom exception class
class CustomException(Exception):
    def __init__(self, error_message, error_details: sys):
        """
        Custom exception initializer.

        :param error_message: A brief error description.
        :param error_details: The sys module for detailed traceback info.
        """
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_details)

    def __str__(self):
        return self.error_message


# super().__init__(error_message): Calls the parent Exception class to store the basic error message.
# self.error_message: Stores the detailed error message created by the error_message_detail function.