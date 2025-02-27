from datetime import datetime

Search_Text = "Miami, Florida, USA"
Contact_Name = "Hilton"
Different_Phones_Message = "Hello, the phone numbers on the mobile and website are different"
Room_Order_Message = "I would like to order a room for another day"

def translate_number(number):
    """translates a number with characters
    to only have numbers"""
    translator = {
        'A': '2', 'B': '2', 'C': '2',
        'D': '3', 'E': '3', 'F': '3',
        'G': '4', 'H': '4', 'I': '4',
        'J': '5', 'K': '5', 'L': '5',
        'M': '6', 'N': '6', 'O': '6',
        'P': '7', 'Q': '7', 'R': '7', 'S': '7',
        'T': '8', 'U': '8', 'V': '8',
        'W': '9', 'X': '9', 'Y': '9', 'Z': '9'
    }
    result = ""
    for char in number:
        if char.isalpha():  # If 'char' is a character
            result += translator[char]
        else:
            result += char
    return result

def strip_number(number):
    """Returns the number given as an input without spaces and '-'"""
    return number.replace(" ", "").replace("-", "").replace("+", "")

def get_current_time():
    """Returns the current time with the format [HH:MM AM/PM]"""
    hour = datetime.now().strftime("%I:%M %p")
    if hour[:1] == '0':
        hour = hour[1:]
    return hour

def is_time_after_now(time):
    """Returns True if the time given as an input is later than
    the time right now, otherwise will return a False."""
    time_now = get_current_time()
    if time[-2:] == 'PM' and time_now[-2:] == 'AM':
        return True
    elif time[-2:] == 'AM' and time_now[-2:] == 'PM':
        return False
    elif int(time[:1]) > int(time_now[:1]):
        return True
    elif int(time[2:4]) > int(time_now[2:4]):
        return True
    else:
        return False