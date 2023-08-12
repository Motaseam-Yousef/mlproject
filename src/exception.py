# import sys 

# def error_message_detail(error):
#     _, _, exc_tb = sys.exc_info()
#     file_name = exc_tb.tb_frame.f_code.co_filename
#     error_message = "Error occurred in python Script name [{0}] line number [{1}] error message [{2}] ".format(
#         file_name, exc_tb.tb_lineno, str(error)
#     )
#     return error_message

# class CustomException(Exception):
#     def __init__(self, error_message) -> None:
#         super().__init__(error_message)
#         self.error_message = error_message_detail(error_message)
    
#     def __str__(self):
#         return self.error_message

import sys 

def error_message_detail(error):
    _, _, exc_tb = sys.exc_info()
    
    # It's better to fetch filename and line number from traceback if it exists.
    if exc_tb is not None:
        file_name = exc_tb.tb_frame.f_code.co_filename
        line_number = exc_tb.tb_lineno
    else:
        file_name = "Unknown"
        line_number = "Unknown"

    error_message = "Error occurred in python Script name [{0}] line number [{1}] error message [{2}] ".format(
        file_name, line_number, str(error)
    )
    return error_message

class CustomException(Exception):
    def __init__(self, error_message) -> None:
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message)
    
    def __str__(self):
        return self.error_message
