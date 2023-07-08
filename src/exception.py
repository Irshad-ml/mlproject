import sys
import traceback

try:
    # Code that may raise an exception
    1 / 0
except:
    # Get the exception details
    exc_type, exc_value, exc_traceback = sys.exc_info()
    
    # Print the exception details
    print("Exception Type:", exc_type)
    print("Exception Value:", exc_value)
    
    # Print the traceback
    traceback_details = traceback.format_exception(exc_type, exc_value, exc_traceback)
    traceback_text = "".join(traceback_details)
    print("Traceback:")
    print(traceback_text)