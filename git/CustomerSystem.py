# Throughout this project, the use of data structures are not permitted 
# Minimal built in functions are to be used and the majority of functions must be
# created yourself

# More packages may be imported in the space below if approved by your instructor
import os
import csv

folder = os.getcwd()

def printMenu():
    print('''
          Customer and Sales System\n
          1. Enter Customer Information\n
          2. Generate Customer data file\n
          3. Report on total Sales (Not done in this part)\n
          4. Check for fraud in sales data (Not done in this part)\n
          9. Quit\n
          Enter menu option (1-9)
          ''')

'''
    This function is to be edited to achieve the task.
    It is your decision to make this function a procedural or functional type
    You may place as many or as few parameters as needed
    This function may also be broken down further depending on your algorithm/approach
'''
def enterCustomerInfo():
    'Asks the user for their first name, last name, city, postal code, and credit card number, and then saves that information'
    global customerId
    global info

    # States the ID of the user, and asks them to input all there information
    customerId = customerId + 1
    customerFirstName = input("First Name: ")
    customerLastName = input("Last Name: ")
    city = input("City: ")
    postalCode = input("Postal Code: ")

    # Validates the postal code by calling the validatePostalCode() function
    while validatePostalCode(postalCode) != True:
            print("Invalid Postal Code")
            postalCode = input("Postal Code: ")

    creditCardNumber = input("Credit Card Number: ") 

    # Validates the credit card number by calling the validateCreditCard() function
    while validateCreditCard(creditCardNumber) != True:
            print("Invalid Credit Card")
            creditCardNumber = input("Credit Card Number: ") 

    info = str(customerId) + "," + customerFirstName + "," + customerLastName + "," +  city, "," + postalCode + "," + creditCardNumber + "\n"

'''
    This function is to be edited to achieve the task.
    It is your decision to make this function a procedural or functional type
    You may place as many or as few parameters as needed
    This function may also be broken down further depending on your algorithm/approach
'''
def validatePostalCode(postalCode):
    'Checks whether the postal code valid, by checking if the first 3 characters are in the postal_codes.csv file'
    # Opens and reads the file using | as the delimiter
    fileName = folder + "\\postal_codes.csv"
    file = open(fileName, "r")
    csvFile = csv.reader(file, delimiter="|")

    # Searches each line of the file for the first 3 letters of the postal code
    for line in csvFile:        
        if postalCode[:3] in line:
            return True
    file.close()

'''
    This function is to be edited to achieve the task.
    It is your decision to make this function a procedural or functional type
    You may place as many or as few parameters as needed
    This function may also be broken down further depending on your algorithm/approach
'''
def validateCreditCard(creditCardNumber):
    'Check whether the credit card number is valid by using the luhn algorithm to check if the sum ends in a 0'
    # Checks if the file has more than 9 characters and is not a string
    if len(creditCardNumber) < 9 or creditCardNumber.isnumeric() != True:
        return False
    
    sum1 = 0
    sum2 = 0

    # Reverses the card number
    reverseCard = str(creditCardNumber[::-1])

    # Adds together all the odd numbers and saves as sum1
    for i in range(0, len(str(reverseCard)), 2):
        oddDigit = int(reverseCard[i])
        sum1 += oddDigit

    # Doubles all the even numbers and if they are more than 9 adds the 2 digits, then saves as sum2
    for i in range(1, len(str(reverseCard)), 2):
        evenDigit = int(reverseCard[i])*2
        if evenDigit > 9:
            evenDigit = str(evenDigit)
            evenDigit1 = evenDigit[0]
            evenDigit2 = evenDigit[1]
            evenDigit = int(evenDigit1) + int(evenDigit2)
        sum2 += evenDigit

    # Adds the 2 sums together
    sum = str(sum1+sum2)
    
    # Checks if the last number in the total sum is 0
    if sum[-1] == "0":
        return True

'''
    This function is to be edited to achieve the task.
    It is your decision to make this function a procedural or functional type
    You may place as many or as few parameters as needed
    This function may also be broken down further depending on your algorithm/approach
'''
def generateCustomerDataFile():
    'Generates or opens the data file, and appends the customers information'
    # Creates the data file if it does not already exist, then appends the new info to it
    fileName = folder + "\\data_file.csv"
    file = open(fileName, "a")
    file.writelines(info)
    file.close()

####################################################################
#       ADDITIONAL METHODS MAY BE ADDED BELOW IF NECESSARY         #
####################################################################




####################################################################
#                            MAIN PROGRAM                          #
#           DO NOT EDIT ANY CODE EXCEPT WHERE INDICATED            #
####################################################################

# Do not edit any of these variables
userInput = ""
enterCustomerOption = "1"
generateCustomerOption = "2"
exitCondition = "9"

# More variables for the main may be declared in the space below
customerFirstName = ""
customerLastName = ""
city = ""
postalCode = ""
creditCardNumber = ""
customerId = 0

while userInput != exitCondition:
    printMenu()                 # Printing out the main menu
    userInput = input();        # User selection from the menu

    if userInput == enterCustomerOption:
        # Only the line below may be editted based on the parameter list and how you design the method return
        # Any necessary variables may be added to this if section, but nowhere else in the code
        enterCustomerInfo()

    elif userInput == generateCustomerOption: 
        # Only the line below may be editted based on the parameter list and how you design the method return
        generateCustomerDataFile()

    else:
        print("Please type in a valid option (A number from 1-9)")

#Exits once the user types 
print("Program Terminated")