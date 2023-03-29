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
    global customerFirstName
    global customerLastName
    global city
    global postalCode
    global creditCardNumber
    global customerId

    customerId = customerId + 1
    customerFirstName = input("First Name: ")
    customerLastName = input("Last Name: ")
    city = input("City: ")
    postalCode = input("Postal Code: ")

    while validatePostalCode(postalCode) != True:
            postalCode = input("Postal Code: ")
    
    creditCardNumber = input("Credit Card Number: ") 
    
    while len(creditCardNumber) < 9:
        creditCardNumber = input("Credit Card Number: ") 

    while validateCreditCard(creditCardNumber) != True:
        creditCardNumber = input("Credit Card Number: ")     

'''
    This function is to be edited to achieve the task.
    It is your decision to make this function a procedural or functional type
    You may place as many or as few parameters as needed
    This function may also be broken down further depending on your algorithm/approach
'''
def validatePostalCode(postalCode):
    'Asks the user for their postal code and checks whether it is valid'
    fileName = folder + "\\postal_codes.csv"
    file = open(fileName, "r")
    csvFile = csv.reader(file, delimiter="|")

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
    'check'
    sum1 = 0
    sum2 = 0
    reverseCard = str(creditCardNumber[::-1])
    for i in range(0, len(str(reverseCard)), 2):
        digit = int(reverseCard[i])
        sum1 += digit
    print(sum1)

    for i in range(1, len(str(reverseCard)), 2):
        digit = int(reverseCard[i])*2
        if digit > 9:
            for x in range(len(str(digit))):
                doubleDigit = int(digit[i])
                digit += doubleDigit
        sum2 += digit
    print(sum2)

    

    #print(reverseCard%10)



'''
    This function is to be edited to achieve the task.
    It is your decision to make this function a procedural or functional type
    You may place as many or as few parameters as needed
    This function may also be broken down further depending on your algorithm/approach
'''
def generateCustomerDataFile():
    print(customerId, customerFirstName, customerLastName, city, postalCode, creditCardNumber)

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