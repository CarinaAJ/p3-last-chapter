import time
from datetime import datetime
import sys
import pyfiglet
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('last_chapter_orders')


book_list = {
    "1.": "Rumo - W.Moers, £20",
    "2.": "The Sober Diaries - C.Pooley, £9.99",
    "3.": "The Flat Share - B.O'Leary, £8.99",
    "4.": "The Swarm - F.Schatzing, £16.99",
    "5.": "Lolita - V.Nabokov, £9.99",
    "6.": "Cybercrime & Digital Forensics - T.Holt, £32.99",
    "7.": "IT - S.King, £10.99",
    "8.": "The Book Thief - M.Zusak, £8.99",
}


def enter_or_exit():
    """"
    Function to either continue to browse
    or leave shop
    """
    while True:
        print("Hello and welcome to The Last Chapter! \U0001F4DA")
        decision_user = input(
            """Do you want to see some books? """
            """Enter Y to see our selection """
            """or N to exit: """
        )
        decision_user = decision_user.strip()
        if (decision_user == "Y" or decision_user == "y"):
            print("Amazing! Let me get the list for you........\n")
            time.sleep(1)
            for index_list, title in book_list.items():
                print(index_list, title)
            break
        elif (decision_user == "N" or decision_user == "n"):
            print("No worries. Thanks for stopping by!\U0001F44B")
            sys.exit()
        else:
            print("Hmm...that doesn't seem right!\U0001F914")
            print("Please make sure to enter Y or N")
            print()
            return enter_or_exit()


def order_book():
    """"
    Function to select a book or leave shop
    """
    while True:
        print()
        print(
            """If you wish to place an order, please """
            """enter the number of the title you wish """
            """to order (i.e. 1 for 'Rumo' """
            """2 for 'The Sober Diaries' etc.). \n\nIf there """
            """is nothing in our shop for you today don't worry.\n"""
            """Press any other key to leave the shop \U0001F642"""
        )
        print()
        global select_book
        select_book = input("Enter the number/other key now: ")
        select_book = select_book.strip()
        if select_book == "1":
            select_book = book_list.get('1.')
            print(f"You selected: {select_book} \U0001F4D5")
            break
        elif select_book == "2":
            select_book = book_list.get('2.')
            print(f"You selected: {select_book} \U0001F4D4")
            break
        elif select_book == "3":
            select_book = book_list.get('3.')
            print(f"You selected: {select_book} \U0001F4D6")
            break
        elif select_book == "4":
            select_book = book_list.get('4.')
            print(f"You selected: {select_book} \U0001F4D7")
            break
        elif select_book == "5":
            select_book = book_list.get('5.')
            print(f"You selected: {select_book} \U0001F4D8")
            break
        elif select_book == "6":
            select_book = book_list.get('6.')
            print(f"You selected: {select_book} \U0001F4D9")
            break
        elif select_book == "7":
            select_book = book_list.get('7.')
            print(f"You selected: {select_book} \U0001F4D4")
            break
        elif select_book == "8":
            select_book = book_list.get('8.')
            print(f"You selected: {select_book} \U0001F4D6")
            break
        else:
            print("No worries. Have a lovely day \U0001F44B")
            sys.exit()

    return select_book


def user_data():
    """"
    Function to take and check user's details
    """
    while True:
        print()
        time.sleep(0.5)
        fname = input("Please enter your first name: ")
        fname = fname.strip()
        if len(fname) < 1 or fname.isdigit():
            print(
                """Hmmm....this doesn't seem right \U0001F914 """
                """ Please make sure to enter a name!"""
            )
            print("Let's start again \U0001F60A")
            return user_data()
        else:
            pass
        lname = input("Please enter your last name: ")
        lname = lname.strip()
        if len(lname) < 1 or lname.isdigit():
            print(
                """Hmmm....this doesn't seem right \U0001F914 """
                """ Please make sure to enter a name!"""
            )
            print("Let's start again \U0001F60A")
            return user_data()
        else:
            pass
        mnumber = input("Please enter your 11-digit UK mobile number: ")
        mnumber = mnumber.strip()
        if validate_number(mnumber):
            print("Perfect. These are your details:\n")
        else:
            continue
        print(f"First name: {fname}\nLast name: {lname}\nPhone: {mnumber}")
        print()
        print("If your details are correct enter 1 and 2 if not")
        check_details = input("Please enter now: ")
        check_details = check_details.strip()
        if check_details == "1":
            print("Alright! \U0001F44D Let's finish your order \U0001F642")
            print("..........................................")
            time.sleep(2)
            break
        elif check_details == "2":
            print("No worries. Let's fix it! \U0001F642")
            print("Just enter them again to correct them.")
            print()
        else:
            print("Hmm...that doesn't seem right!\U0001F914")
            print("Please make sure to enter 1 or 2.")
            print("Let's start again from the top \U0001F60A")

    return fname, lname, mnumber


def validate_number(numbers):
    """"
    Validate mobile number
    """
    try:
        if len(numbers) != 11:
            raise ValueError

    except ValueError:
        print("\nWhoops!\U0001F914 Please make sure you enter 11 digits.")
        print("Let's just try this again from the top \U0001F642")
        print()
        return False

    return True


def update_sheet(name1, name2, number, title, worksheet):
    """"
    Function to update the Google Sheet
    with the user's details and selected title
    """
    add_data = SHEET.worksheet(worksheet)
    add_data.append_row([name1, name2, number, title])


def print_receipt():
    """"
    Function to print the receipt
    """
    print(
        """Thank you for supporting your local bookshop! \U0001F917\n"""
        """Your order will be ready to collect """
        """within the next 1 - 3 working days.\n"""
        """But we'll send you a text message when it is ready \U0001F4F2"""
    )
    print()
    print("And here is your receipt \U0001F9FE:")
    time.sleep(2)
    print("..........................................")
    print("The Last Chapter")
    print("Bookstore Lane 42")
    print("123 ABC London")
    print()
    print(f"You ordered: {select_book} \U0001F4D6")
    print()
    now = datetime.now()
    date_format = now.strftime("%d.%m.%Y %H:%M:%S")
    print(date_format)
    print("..........................................")
    print()


def main():
    """"
    Main function, which includes
    all functions to run the program
    """
    enter_or_exit()
    select_book = order_book()
    print()
    print(
        """(-> Please note: for the purpose of this """
        """project your name and number will be\n"""
        """added to an external sheet so feel """
        """free to add fictional details if """
        """you prefer.\nNo data will be shared """
        """with anyone but me.)"""

    )
    time.sleep(5)
    print()
    print("Let me grab your details now \U0001F58A")
    fname, lname, mnumber = user_data()
    update_sheet(fname, lname, mnumber, select_book, "book_orders")
    print_receipt()


while True:
    welcome_title = pyfiglet.figlet_format("The Last Chapter")
    print(welcome_title)
    main()
    print(
        """If you want to place another order """
        """enter 1. If not enter any other key."""
    )
    stay_or_leave = input("Please choose now: ")
    stay_or_leave = stay_or_leave.strip()
    if stay_or_leave == "1":
        continue
    else:
        print()
        print("See you next time. Have a lovely day \U0001F642")
        break
