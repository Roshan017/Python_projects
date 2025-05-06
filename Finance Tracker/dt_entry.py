from datetime import datetime

date_format = "%d-%m-%Y"
Cat = {"I": "Income", "E": "Expense"}
def getdate(prompt, allow_default = False):
    date_str = input(prompt)
    if allow_default and not date_str:
        return datetime.now().strftime(date_format)
    try:
        valid_date = datetime().strptime(date_str, date_format)
        return valid_date.strftime(date_format)
    except ValueError:
        print("Invalid date format. Please enter in dd-mm-yyyy format.")
        return getdate(prompt, allow_default) 

def get_amt():
    try:
        amt = float(input("Enter amount: "))
        if amt < 0:
            raise ValueError("Amount cannot be negative.")
        return amt
    except ValueError as e:
        print(f"Invalid input: {e}. Please enter a valid amount.")
        return get_amt()


def get_category():
    category = input("Enter category ('I' fro Income and 'E' for Expense): ").upper()
    if category in Cat:
        return Cat[category]
    else:
        print("Invalid category. Please enter 'I' for Income or 'E' for Expense.")
        return get_category()

def get_description():
    
    desc = input("Enter description: ")
    if not desc:
        print("Description cannot be empty.")
        return get_description()
    return desc



