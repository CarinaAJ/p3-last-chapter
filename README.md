# The Last Chapter

## A website to browse and order books

![Landing Page](readme-assets/landing-page.png)

--------------------------------------

## Table of Contents

--------------------------------------


- [Description](#description)
- [Theme](#theme)
- [User Experience](#user-experience)
- [Features](#features)
    - [Future Features](#future-features)
- [Testing](#testing)
- [Technologies](#technologies)
- [Deployment](#cloning)
- [Credits](#credits)

----------------------------------------

## Description
----------------------------------------

As an avid reader, I wanted to create a little bookshop and allow the user to browse and have a look at the available titles and order a book if he wishes. 

----------------------------------------

## Theme

----------------------------------------
Despite the project being entirely text-based, I implemented a few little things to make it more user-friendly. When the user enters the site, he will be greeted with a big heading and the name of the bookshop, ‘The Last Chapter’. Furthermore, I added emojis throughout the entire programme where appropriate and added slight delays for various reasons. An explanation follows where the sleep function has been used.

![Bookshop Name](readme-assets/theme-last-chapter.png)


-----

## User Experience
----------------------------------------


### User Stories
----------------------------------------
As a first time visitor:

- I want to know which shop I entered and then decide if I want to have a look around or leave the shop 
- I want clear instructions on what I need to enter if I have been asked to do so

As a returning visitor:

- I want to be able to order another book 

----------------------------------------

### Python Logic
----------------------------------------

Before I started my programme I created a flowchart so I knew the structure of my programme and would be able to look at it for guidance during the process.

![Flowchart](readme-assets/flowchart-last-chapter-.png)

----------------------------------------
## Features
----------------------------------------

### Start/first decision

The user is greeted with the name of the bookshop together with a welcome message. Here he can decide if he wishes to see our collection or change his mind and leave the shop instead. The option is to enter either Y or N. I ensured to capture a small letter as well. Throughout the entire programme, I also added the .strip() function in case the user accidentally enters a space before or after the input.
  

![Enter or Leave Shop](readme-assets/first-choice.png)

----------------------------------------
#### Leave Shop 

If the user changes his mind, he can leave the shop by entering N.

![First Choice - Leave Shop](readme-assets/first-choice-no.png)

----------------------------------------
### See Selection/second decision

If the user decides to have a look, a list of books will be printed and displayed. To create anticiptation the .sleep() function has been implemented with a delay of 1 second to display the titles.

![Book List](readme-assets/book-list.png)

----------------------------------------
#### Leave Shop 

If the user decides to not go ahead and order a book, he can enter any other key but the numbers between 1 and 8 to leave the shop.

![Second Choice - Leave Shop](readme-assets/second-choice-exit.png)

----------------------------------------
### Select Book

If the user wants to order a book, he is asked to enter a number between 1 and 8 to choose the desired title. And a couple of examples are being mentioned for guidance.

![Second Choice - Select Title](readme-assets/second-choice-continue.png)

----------------------------------------
### User Information

As this project has been linked to a Google Sheet, I added a small paragraph to inform the user that the data will be added to this sheet but confirm that the data will only be collected for the purpose of this project and only be seen by me. I added a 5 second delay to allow the user enough time to read this message before the programme continues. To highlight it is not part of the programme this text has been put in parentheses.

![User Information](readme-assets/user-information.png)

----------------------------------------
### Enter details

The user is now asked to enter the first and last name and his UK mobile number.

![Details](readme-assets/enter-details.png)

### Enter Details - incorrect mobile number

If the user doesn't enter a valid 11-digit UK number, a message pops up and informs him that it is incorrect. He can then enter the details again. Until the user enters an 11-digit number, the programme keeps looping until a valid number has been entered. 

![Wrong mobile number](readme-assets/enter-details-incorrect-number.png)

### Confirm or correct details

After entering all his details, the user can then read over them again and either confirm the details by entering the digit 1, or enter the number 2 if he wishes to correct something.

![Confirm Details - No](readme-assets/confirm-details-no.png)

If he confirms his choice, a message appears letting the user know we can finish up this order now.

![Confirm Details - Yes](readme-assets/confirm-details-yes.png)

## Confirmed Details & Google Sheet

Once the user has confirmed his details, they are simultaneously added to the Google Sheet.

![Update Google Sheet](readme-assets/confirm-details-add-to-sheet.png)


### Thank you & Receipt

At this stage, the user is being thanked for supporting his local bookshop, and a small receipt will be printed. Another delay of 2 seconds has been added before the receipt has been 'printed'. On this receipt, the user will find the address of the shop, the title and price of the book he ordered, and the date and time.

![Thanks & Receipt](readme-assets/receipt.png)

## Last choice

The user is now being asked if he wishes to place another order or leave the shop. If he wishes to leave, he is asked to enter N, and a goodbye message pops up and the programme ends.

![Leave Shop](readme-assets/last-choice-exit.png)


If he wishes to place another order, he is asked to enter Y and the programme starts again from the beginning.

![Order another book](readme-assets/last-choice-new-start.png)

## Future Features
--------------------------

- To migrate the booklist to a Google sheet and pull out the titles from there for a wider selection
- To give the user the option to enter an email address instead off or addition to a phone number
- To allow the user to order multiple books at the same time


[Back to the Top](#table-of-contents)


-----
## Technologies Used 
---------------------

- Python, to write my code
- Heroku, to deploy my site

-----------------------------

## Python Libraries/Modules
---------------------------

- Time - to add the .sleep() function and delay my code in the terminal
- [Datetime](https://www.programiz.com/python-programming/datetime/strftime) - to print the current date and time on the receipt
- [Sys](https://www.hashbangcode.com/article/stopping-code-execution-python) - to exit the programme
- [Pyfiglet](https://www.geeksforgeeks.org/python-ascii-art-using-pyfiglet-module/) - to create a header    for the bookshop,
- Gspread - as API for my Google Sheet

[Back to the Top](#table-of-contents)


--------------------------------------
## Testing & Issues Encountered
--------------------------------------

The site has been tested by me thoroughly during its creation to ensure that the programme runs as it should and errors are being caught.

I had a lot of fun creating my little bookshop and enjoyed it very much. Nevertheless, I encontered a few issues during the creation: 

1) At first I only had one break statement in my order_book() function, so every time I ran the programme it jumped back to the beginning instead of going ahead to the user_data() function. I had it working before, but only because I entered by chance the only number that had the break statement included. After having posted my question in the Slack Channel, I saw my issue a couple of minutes later and entered a break statement after each choice. This fixed my problem.

2) When printing the receipt, I wanted to display the choice the user made together with a few extra pieces of information but kept running into error messages. After reading over the Code Institute material over and over again, I found a simple solution and made my select_book variable a global variable. This allowed me to show the title the user had selected on the receipt successfully.

3) My biggest issue, however, was adding the customer's details to my Google Sheet. I tried endless variations and looked at the love sandwich project for guidance as well as other similar projects. Unfortunately, none of them helped me find the answer, because unlike them, I wanted to add three variables (fname, lname and mnumber) from one function at the same time (the decision to add the title to the Google Sheet as well came later). At first I thought I might be able to add it with a simple append_row statement within my user_data() function, but it wasn't as easy as that. 

I tried turning these variables into global variables and using them, but this turned out to be a fail too. I then came up with a solution and, on paper, it should have worked, but I kept getting error message after error message. So I contacted Tutor Support, who helped me and pointed out that the add_data.append_row (name1, name2, number) in my update_sheet() function was missing square brackets, converting it to a list rather than a string. After changing this, the entered details finally showed up in my Google Sheet.

[Back to the Top](#table-of-contents)


### Validators Testing
----------------------

The code has been tested by running it through the PeP8. Almost all of the errors that have been encountered were due to trailing whitespaces or either too many or not enough blank lines.

No errors were found during the final check.

![PEP8](readme-assets/pep8-test-final.png)

-----------------------------

### Browser Testing
-----------------------

The programme has been tested on Google Chrome, Firefox and Safari without any issues. Due to the nature of the programme, it is not suitable for mobile phones and smaller devices.

### Issues/Bugs Fixed 
-----------------------------




[Back to the Top](#table-of-contents)


---------------------------
### Deployment to Heroku
---------------------------

The website was deployed to heroku by doing the following: 

1. Navigate to [heroku](https://id.heroku.com/login). 

2. Click "new" and create a new App. 

3. Give your app a name, choose your region and Click "Create app". 

4. The menus that we are concerned with are "Deploy" and "Settings". Click on "Settings" First. 

5. Buildpacks now need to be added. These install future dependancies that we need outside of the requirements file. The first is python and the second is node.js. Select Python first and then node.js and click save. Make sure they are in this order.

6. Then go to the deploy section and choose your deployment method. To connect with github select github and confirm. 

7. Search for your repo, select it and click connect. 

8. You can choose to either deploy using automatic deploys which means heroku will rebuild the app everytime you push your changes. For this option choose the branch to deploy and click enable automatic deploys. This can be changed at a later date to manual. Manual deployment deploys the current state of a branch.  

9. Click deploy branch. 

10. If successful you should be able to view your deployed app by clicking "View". 
    

## Credits 
--------------------

- [Stackoverflow](https://stackoverflow.com/questions/10660435/how-do-i-split-the-definition-of-a-long-string-over-multiple-lines) - for guidance on how to display long string
- [Hashbangcode](https://www.hashbangcode.com/article/stopping-code-execution-python) - how to stop the programme
- [MakeUseOf](https://www.makeuseof.com/how-to-include-emojis-in-your-python-code/) - for the syntax to add emojis
- [W3 School](https://www.w3schools.com/python/gloss_python_loop_dictionary_items.asp) - to provide me with a better option to iterate through a dictionary than my original code 
        * Original solution:
    for key in book_list:
                print(key, book_list[key])*
        * Final version:
    for index_list, title in book_list.items():
                print(index_list, title)
- [Python Basics](https://pythonbasics.org/multiple-return/) - guidane on how to return multiple variables from a function
- [GeeksForGeeks](https://www.geeksforgeeks.org/python-ascii-art-using-pyfiglet-module/) - help on which module to import and how to create my header
- [W3 School](https://www.w3schools.com/howto/howto_css_fixed_footer.asp) - how to fix my social icons to the footer
- Love Sandwiches - for general guidance 

[Back to the Top](#table-of-contents)


-----
## Acknowledegments
---------------------------



[Back to the Top](#table-of-contents)

