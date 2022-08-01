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
            continue


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
            """Press any key to exit :)"""
        )
        print()
        select_book = input("Enter the number now: ")
        if select_book == "1":
            print(f"You selected: {book_list.get('1')}")
            break
        elif select_book == "2":
            print(f"You selected: {book_list.get('2')}")
            break
        elif select_book == "3":
            print(f"You selected: {book_list.get('3')}")
            break
        elif select_book == "4":
            print(f"You selected: {book_list.get('4')}")
            break
        elif select_book == "5":
            print(f"You selected: {book_list.get('5')}")
            break
        elif select_book == "6":
            print(f"You selected: {book_list.get('6')}")
            break
        elif select_book == "7":
            print(f"You selected: {book_list.get('7')}")
            break
        elif select_book == "8":
            print(f"You selected: {book_list.get('8')}")
            break
        else:
            print("No worries :)\n")
            enter_or_exit()


# works but also need to validate user input
def user_data():
    """"
    Function to take and check user's details
    """
    while True:
        print("Great. Let me now grab your details.")
        fname = input("Please enter your first name: ")
        lname = input("Please enter your last name: ")
        email = input("Please enter your email address: ")
        print("Perfect. These are your details:\n")
        print(f"First name: {fname}\nLast name: {lname}\nEmail: {email}")
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
    pass


def main():
    """"
    Main function, which includes
    all functions to run the program
    """
    enter_or_exit()
    order_book()
    user_data()


main()
