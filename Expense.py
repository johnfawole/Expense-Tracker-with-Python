# code logic

# this is a feature in a personal finance app that enables 
# customers to monitor
# - what they spend on 
# - the amount of their spendings over a period

# so they can be more informed about their spending habits

expenses = []

sampleExpense1 = {"amount": "$1000", "category": "Clothing", "date": "9th of December, 2024"}
expenses.append(sampleExpense1)
sampleExpense2 = {"amount": "$1000", "category": "Vacation", "date": "9th of December, 2024"}
expenses.append(sampleExpense2)
sampleExpense3 = {"amount": "$1000", "category": "Burger", "date": "9th of December, 2024"}
expenses.append(sampleExpense3)
sampleExpense4 = {"amount": "$1000", "category": "Date", "date": "9th of December, 2024"}
expenses.append(sampleExpense4)
sampleExpense5 = {"amount": "$1000", "category": "Metro", "date": "9th of December, 2024"}
expenses.append(sampleExpense5)
sampleExpense6 = {"amount": "$1000", "category": "Mortgage", "date": "9th of December, 2024"}
expenses.append(sampleExpense6)



def printHome():
    print("Kindly choose from the following")
    print("1. Add a new expense")
    print("2. Remove an expense")
    print("3. List all expenses")
    print("4. Exit")

def listAllExpenses():
    print("Here is a list of all your expenses so far")
    print("*********************************")

    counter = 1
    for expense in expenses:
        
        print(counter, "|", expense["amount"], "|", expense["category"], "|", expense["date"])
        counter += 1

def removeExpenses():
    while True:
        try:
          expenseToRemove = int(input("> "))
          del expenses[expenseToRemove]
          break
        except:
            print("the array starts from zero, remember?")
    
    print("the expense has been removed")

def addExpense(amount, category, date):
    expense = {"amount": amount, "category": category, "date": date}
    expenses.append(expense)


if __name__ == "__main__":
    while True:
        printHome()
        optionSelected = input(" ")

        if (optionSelected == "1"):
            print("How much was this expense we are talking about??")
            while True:
                try:
                    amountToAdd = input("$")
                    break
                except:
                    print("that was quite an invalid input")
            print("What category does this expense fall to?")
            while True:
                try:
                    expenseCategory = input(" ")
                    break
                except:
                    print("that was quite an invalid input")
            print("And when was the day you made this purchase??")
            while True:
                try:
                    dateOfPurchase = input(" ")
                    break
                except:
                    print("that was quite an invalid input")
            
        elif (optionSelected == "2"):
            removeExpenses()
        elif (optionSelected == "3"):
            listAllExpenses()
        elif (optionSelected == "4"):
            break

        else:
            print("that was quite an invalid input")
