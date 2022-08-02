import time 
import sys

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
    or exit
    """
    while True:
        print("Hello and welcome to The Last Chapter!")
# add print statement with nicely formatted logo        
        decision_user = input(
            """Do you want to see some books? """
            """Enter Y to see our selection """
            """or N to exit: """
        )
        decision_user = decision_user.strip()
        if (decision_user == "Y" or decision_user == "y"):
            print("Amazing! This is our list: \n")
            for key in book_list:
                print(key, book_list[key])
            break
        else:
            print("No worries. Thanks for stopping by!\n")
            sys.exit()


#good function to use try and except to catch validation error
def order_book():
    """"
    Function to select a book
    """
    while True:
        print(
            """If you wish to place an order, please """
            """enter the number of the title you wish """
            """to order (i.e. 1 for the first title """
            """2 for the second title etc.). If there """
            """is nothing in our shop for you today don't worry. """
            """Press any other key to exit :)"""
        )
        print()
        global select_book
        select_book = input("Enter the number now: ")
        if select_book == "1":
            select_book = book_list.get('1.')
            print(f"You selected: {select_book}")
            break
        elif select_book == "2":
            select_book = book_list.get('2.')
            print(f"You selected: {select_book}")
            break
        elif select_book == "3":
            select_book = book_list.get('3.')
            print(f"You selected: {select_book}")
            break
        elif select_book == "4":
            select_book = book_list.get('4.')
            print(f"You selected: {select_book}")
            break
        elif select_book == "5":
            select_book = book_list.get('5.')
            print(f"You selected: {select_book}")
            break
        elif select_book == "6":
            select_book = book_list.get('6.')
            print(f"You selected: {select_book}")
            break
        elif select_book == "7":
            select_book = book_list.get('7.')
            print(f"You selected: {select_book}")
            break
        elif select_book == "8":
            select_book = book_list.get('8.')
            print(f"You selected: {select_book}")
            break
        else:
            print("No worries. Have a lovely day :)")
            sys.exit()


# works but also need to validate user input
def user_data():
    """"
    Function to take and check user's details
    """
    while True:
        print("Great. Let me now grab your details.")
        fname = input("Please enter your first name: ")
        lname = input("Please enter your last name: ")
        mobile = int(input("Please enter your mobile number: "))
        print("Perfect. These are your details:\n")
        print(f"First name: {fname}\nLast name: {lname}\nPhone: {mobile}")
        print()
        print("If your details are correct enter 1 and 2 if not")
        check_details = input("Please enter now: ")
        if check_details == "1":
            print("Super! Let's finish your order then.")
            break            
        else:
            print("No worries. Let's fix it!")
            print("Just enter them again to correct them.")
            

def update_sheet():
    """"
    Function to update the Google Sheet
    with the user's details
    """
    pass


def print_receipt():
    """"
    Function to print the receipt
    """
    print(
        """Thank you for supporting your local bookshop! """
        """Your order will be ready to collect """
        """within the next 1 - 3 working days. """
        """But we'll send you a text message when it is ready."""
    )
    print("And here is your receipt:")
    print("----------------------------")
    print(f"You ordered: {select_book}")
    


def main():
    """"
    Main function, which includes
    all functions to run the program
    """
 #   enter_or_exit()
    order_book()
    user_data()
    print_receipt()


main()
