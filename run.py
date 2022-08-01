import time 

book_list = {
    "1": "Title1 - Author1",
    "2": "Title2 - Author2",
    "3": "Title3 - Author3",
    "4": "Title4 - Author4",
    "5": "Title5 - Author5",
    "6": "Title6 - Author6",
    "7": "Title7 - Author7",
    "8": "Title8 - Author8",
}

#works, just need to make sure to add validation error 
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
        if decision_user == "Y":
            print("Amazing! This is our list: \n")
            for key in book_list:
                print(key, book_list[key])
            break
        else:
            print("No worries. Thanks for stopping by!")
            break

#good function to use try and except to catch validation error
def order_book():
    """"
    Function to select a book
    """
    while True:
        print(
            """If you wish to place an order, please """
            """enter the number of the title you wish """
            """ to order (i.e. 1 for the first title """
            """2 for the second title etc.)"""
        )
        select_book = input("Enter the number now: ")
        if select_book == "1":
            print(f"You selected: {book_list.get('1')}")
        elif select_book == "2":
            print(f"You selected: {book_list.get('2')}")
        elif select_book == "3":
            print(f"You selected: {book_list.get('3')}")
        elif select_book == "4":
            print(f"You selected: {book_list.get('4')}")
        elif select_book == "5":
            print(f"You selected: {book_list.get('5')}")
        elif select_book == "6":
            print(f"You selected: {book_list.get('6')}")
        elif select_book == "7":
            print(f"You selected: {book_list.get('7')}")
        elif select_book == "8":
            print(f"You selected: {book_list.get('8')}")
        else:
            pass


def user_details():
    while True:
        print("Great. Let me now grab your details.")
        enter_fname = input("Please enter your first name: ")
        enter_lname = input("Please enter your last name: ")
        email_address = input("Please enter your email address: ")








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
    pass


def main():
    """"
    Main function, which includes
    all functions to run the program
    """
    pass