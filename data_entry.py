from datetime import datetime

date_format = "%d-%m-%Y"
CATAGORIES = {
    "I": "Income",
    "E": "Expense"
}

def get_date(prompt, allow_default=False):
    date_str = input(prompt)

    if allow_default and not date_str:
        return datetime.today().strftime(date_format)
    
    try:
        valid_date = datetime.strptime(date_str, date_format)
        return valid_date.strftime(date_format)
    except ValueError:
        print("Invalid date format please enter the date in dd-mm-yyyy format!")
        return get_date(prompt, allow_default)

def get_amount():
    try:
        amount = float(input("Enter the amount: "))
        if amount <= 0:
            raise ValueError("Amount must be a non-negative non-zero value!")
        return amount
    except ValueError as e:
        print(e)
        return get_amount()

def get_catagory():
    catagory = input("Enter the catagory ('I' for Income or 'E' for Expense): ").upper()
    if catagory in CATAGORIES:
        return CATAGORIES[catagory]
    
    print("Invalid catagory. Please enter 'I' for Income or 'E' for Expense!")

def get_description():
    return input("Enter a description (optional): ")