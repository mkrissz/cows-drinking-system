from datetime import datetime

def get_current_timestamp():
    # Get the current date and time and format it as a string
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def float_form(number):
    # Round the number to 2 decimal places
    return round(number, 2)
