# IMPORTS

import random
import time
import string

# CONSTANTS, VARIABLES

menu = """\nWelcome to the Winchester Hotel
What would you like to do?\n
A: Book a Room
B: Display Customer Details
C: Hotel Information
D: Quit"""
input_prompt = "\n> "
option_not_valid = '\nThat is not a valid option'
COST_PER_NIGHT = 150
room_is_booked = False

# GLOBAL VARIABLES (Just so the program stops hassling me about them)

name = 'Caleb Webster'
period = 1
room_number = 0
day_or_days = 'day'
total_cost = 150


# FONT COLOURS / STYLES (these only work in the "print" function)

class Color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARK_CYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


# WAIT FUNCTIONS

def wait():
    time.sleep(0.1)


def long_wait():
    time.sleep(2.5)


def very_long_wait():
    time.sleep(4)


# MAIN MENU

def main():
    wait()
    print(Color.YELLOW, Color.BOLD, '\n\nMain Menu', Color.END, sep="")
    print(menu)
    selection = input(input_prompt)

    if selection.lower() == 'a':
        enter_name()
    elif selection.lower() == 'b':
        details()
    elif selection.lower() == 'c':
        information()
    elif selection.lower() == 'd':
        print('\nGoodbye!')
    else:
        print(option_not_valid)
        main()


# ROOM BOOKING

# ENTER NAME

def enter_name():
    global name

    wait()
    print(Color.YELLOW, Color.BOLD, '\n\nRoom Booking', Color.END)
    print('\nPlease enter your name')
    name = string.capwords(input(input_prompt))

    try:
        name = float(name)
        print(option_not_valid)
        enter_name()
    except ValueError:

        if name == '':
            print(option_not_valid)
            enter_name()
        elif name.lower() == 'master chief':
            master_chief()
        enter_period()


# ENTER PERIOD

def enter_period():
    global period
    global day_or_days

    wait()
    print('\nHow many days will you be staying for?')

    try:
        period = int(input(input_prompt))

        if period <= 0:
            print(option_not_valid)
            enter_period()
        elif period == 1:
            day_or_days = 'day'
        else:
            day_or_days = 'days'
        booking_details()

    except ValueError:
        print(option_not_valid)
        enter_period()


# DISPLAY BOOKING DETAILS / CONFIRM BOOKING

def booking_details():
    global total_cost

    wait()
    total_cost = COST_PER_NIGHT * period
    print(Color.YELLOW, '\n\nBooking Details:', Color.END)
    print('\nName:', name)
    print('Stay Length:', period, day_or_days)
    print('Total Cost: ', '$', total_cost, sep="")
    print('\nConfirm booking?\ny/n')
    confirm_booking = input(input_prompt)

    if confirm_booking.lower() == 'y':
        booking_confirmed()
    elif confirm_booking.lower() == 'n':
        main()
    else:
        print(option_not_valid)
        booking_details()


# BOOKING CONFIRMED

def booking_confirmed():
    global room_is_booked
    global room_number
    room_is_booked = True
    room_number = random.randint(1, 300)

    wait()
    print(Color.YELLOW, Color.BOLD, '\n\nBooking Confirmed!', Color.END)
    print('\nYour room number is', room_number, '\nPlease proceed to the front desk to collect your room key.')
    print('We hope you enjoy your stay!')
    return_main_menu()


# DISPLAY CUSTOMER DETAILS

def details():
    global name
    global period
    global room_number
    global room_is_booked

    wait()
    print(Color.YELLOW, Color.BOLD, '\n\nCustomer Details', Color.END)

    if room_is_booked is False:  # if this boolean is false, there are no customers booked
        print('\nThere are no customers registered')
        main()
    else:
        print('\nName:', name, '\nStay Period:', period, day_or_days, '\nRoom Number:', room_number)

    # UPDATE DETAILS

    print('\nWould you like to update your details\nor cancel your booking?\ny/n')
    change_details_choice = input(input_prompt)

    if change_details_choice.lower() == 'y':
        change_details()
    elif change_details_choice.lower() == 'n':
        main()
    else:
        print(option_not_valid)
        details()


# CHANGE DETAILS

def change_details():
    wait()
    print(Color.YELLOW, Color.BOLD, '\n\nUpdate Booking Details', Color.END)
    print('\nWhich Details would you like to update?')
    print('\nA: Name\nB: Period\nC: Cancel Booking\nR: Return to Main Menu')
    details_selection = input(input_prompt)

    if details_selection.lower() == 'a':
        change_name()
    elif details_selection.lower() == 'b':
        change_period()
    elif details_selection.lower() == 'c':
        cancel_booking()
    elif details_selection.lower() == 'r':
        main()
    else:
        print(option_not_valid)
        change_details()


# NAME CHANGE FUNCTION

def change_name():  # this function will change the name variable stored in the system
    global name

    wait()
    print(Color.YELLOW, Color.BOLD, '\n\nUpdate Name', Color.END)
    print('\nPlease enter your name:')
    name = string.capwords(input(input_prompt))

    try:
        name = float(name)
        print(option_not_valid)
        change_name()
    except ValueError:

        if name == '':
            print(option_not_valid)
            change_name()
        else:
            print('\nYour name was changed to:', name)

        change_details()


# PERIOD CHANGE FUNCTION

def change_period():
    global period
    global total_cost
    global day_or_days

    wait()
    print(Color.YELLOW, Color.BOLD, '\n\nUpdate Stay Period', Color.END)
    print('\nHow many days will you be staying for?')

    try:
        period = int(input(input_prompt))

        if period <= 0:
            print(option_not_valid)
            change_period()
        elif period == 1:
            day_or_days = 'day'
        else:
            day_or_days = 'days'

        total_cost = COST_PER_NIGHT * period
        print('\nYour stay period was changed to:', period, day_or_days)
        print('\nYour total cost was changed to: ', '$', total_cost, sep="")
        change_details()
    except ValueError:
        print(option_not_valid)
        change_period()


# CANCEL BOOKING FUNCTION

def cancel_booking():
    global room_is_booked

    wait()
    print(Color.YELLOW, Color.BOLD, '\n\nCancel Booking', Color.END)
    print('Are you sure you want to cancel booking for', name, '?', '\ny/n')
    cancel_selection = input(input_prompt)

    if cancel_selection.lower() == 'y':
        room_is_booked = False
        print('\nYour booking was cancelled')
        return_main_menu()
    elif cancel_selection.lower() == 'n':
        change_details()
    else:
        print(option_not_valid)
        cancel_booking()


# INFORMATION

def information():
    wait()
    print(Color.YELLOW, Color.BOLD, '\n\nInformation', Color.END)
    print('\nWelcome to the Information Center\nPlease select one of the options below')
    print('\nA: Pricing\nB: Our Staff\nC: History\nD: Main Menu')
    information_selection = input(input_prompt)

    if information_selection.lower() == 'a':
        pricing()
    elif information_selection.lower() == 'b':
        our_staff()
    elif information_selection.lower() == 'c':
        history()
    elif information_selection.lower() == 'd':
        main()
    else:
        print(option_not_valid)
        information()


# PRICING

def pricing():
    wait()
    print(Color.YELLOW, Color.BOLD, '\nPricing', Color.END)
    print("""\nAt the Winchester Hotel, we charge an reasonable price of 
$150 per night. This includes our premium room service, 
which provides professional cleaning and catering for 
all rooms.""")
    return_information_menu()


# OUR STAFF

def our_staff():
    wait()
    print(Color.YELLOW, Color.BOLD, '\nOur Staff', Color.END)
    print("""\nWe want to ensure you enjoy your stay as much as 
possible, and our crew are professionally trained to 
assist you with anything you may need. Ask about 
our services at the front desk for more information.""")
    return_information_menu()


# HISTORY

def history():
    wait()
    print(Color.YELLOW, Color.BOLD, '\nHistory', Color.END)
    print("""\nFounded in 1915 by sir William Leighton, the Winchester 
Hotel has been a trademark of London. Renowned nation-wide 
for its prestige and quality of service. After undergoing 
massive renovations in 1931 and 1980, the building has been 
improved and modernized to keep up with the ever-changing 
industry standards. Check out our information brochure 
at the front desk for more information.""")
    return_information_menu()


# RETURN TO MAIN MENU

def return_main_menu():
    print('\n\nType "r" to return to the Main Menu')
    return_main = input(input_prompt)

    if return_main.lower() == 'r':
        main()
    else:
        print(option_not_valid)
        return_main_menu()


# RETURN TO INFORMATION MENU

def return_information_menu():
    print('\n\nType "r" to return to the Information Menu')
    return_information = input(input_prompt)

    if return_information.lower() == 'r':
        information()
    else:
        print(option_not_valid)
        return_information_menu()


# EASTER EGGS


def master_chief():
    wait()
    print('\n...')
    long_wait()
    print('\n"Chief!?"')
    wait()
    print('\n...')
    long_wait()
    print('\n"Chief, its Cortana."')
    wait()
    print('\n...')
    long_wait()
    print('\n"Where have you been?!"')
    wait()
    print('\n...')
    long_wait()
    print('\n"The Covenant has taken over earth since you left."')
    wait()
    print('\n...')
    long_wait()
    print('\n"Humanity is lost!"')
    wait()
    print('\n...')
    long_wait()
    print('\n"Wait a minute..."')
    wait()
    print('\n...')
    long_wait()
    print('\n"Why are you checking in at a hotel?"')
    wait()
    print('\n...')
    long_wait()
    print('\n"WHERE ARE YOU!?"')
    wait()
    print('\n...')
    long_wait()
    print('\n--- the transmission cut out ---')
    very_long_wait()
    enter_name()


print("\nA project by Caleb Webster, completed on 25/03/2020")
main()
