import time 

book_list = {
    "1.": "Title1 - Author1",
    "2.": "Title2 - Author2",
    "3.": "Title3 - Author3",
    "4.": "Title4 - Author4",
    "5.": "Title5 - Author5",
    "6.": "Title6 - Author6",
    "7.": "Title7 - Author7",
    "8.": "Title8 - Author8",
}

#works, just need to make sure to add validation error 
def enter_or_exit():
    """"
    Function to either continue to browse
    or exit
    """
    while True:
        print("Hello and welcome to The Last Chapter!")
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


def order_book():
    """"
    Function to order a book, leave & check details
    or exit
    """
    pass


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