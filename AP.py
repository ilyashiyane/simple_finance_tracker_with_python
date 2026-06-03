import questionary
import json
import os
from datetime import datetime
FILE_PATH = "transactions.json"
CATEGORIES = ("Food", "Transport", "Housing", "Health", "Entertainment", "Salary", "Other")

def load_data() :
   if not os.path.exists(FILE_PATH) :
      return []
   try :
      with open(FILE_PATH, "r", encoding="utf-8") as f :
         transactions=json.load(f)
      return transactions
   except (json.JSONDecodeError, FileNotFoundError) :
      return []
def save_data(transactions):
   with open(FILE_PATH, "w", encoding="utf-8") as f :
      json.dump(transactions, f, indent=4, ensure_ascii=False)
   print("  ✓ Data saved successfully.")
      
def filter_by_category(transactions) :
   choice=questionary.select("Choose the category",choices=CATEGORIES).ask()
   for transaction in transactions :
      if transaction["category"]==choice :
         print(f"{transaction}")
def view_summary(transactions) :
   income=0
   expense=0
   for transaction in transactions :
      if transaction["transaction_type"]=="income" :
         income+=transaction["amount"]
      elif transaction["transaction_type"]=="expense" :
         expense+=transaction["amount"]
   print(f"Total income    :{income}")
   print(f"Total expenses  :{expense}")
   print("-----------------------------")
   Current_balance=income-expense
   print(f"Current balance :{Current_balance}")
def add_transaction(transactions,transaction_type,amount,category,description,date) :
     transaction={
       "transaction_type":transaction_type,
       "amount":amount,
       "category":category,
       "description":description,
       "date":date.strftime("%Y-%m-%d")
   }
     transactions.append(transaction)
     
def collect_and_add(transactions, transaction_type):
    """Collect input for income or expense and add to transactions list."""
    while True:
        try:
            amount = float(input("  Amount (DH) : ").strip())
            if amount <= 0:
                print("  Amount must be greater than zero.")
            else:
                break
        except ValueError:
            print("  Enter a valid number.")

    category    = questionary.select("  Category :", choices=CATEGORIES).ask()
    description = input("  Description : ").strip()

    current_year = datetime.now().year
    while True:
        date = input("  Date (YYYY-MM-DD) : ").strip()
        try:
            date_object = datetime.strptime(date, "%Y-%m-%d")
            if 1950 <= date_object.year <= current_year:
                break
            else:
                print(f"  Year must be between 1950 and {current_year}.")
        except ValueError:
            print("  Invalid format. Use YYYY-MM-DD.")

    add_transaction(transactions, transaction_type, amount, category, description, date_object)
transactions = load_data()
while True :
 choice = questionary.select(
    "PERSONAL FINANCE TRACKER",
    choices=["1. Add income", "2. Add expense", "3. View all transactions","4. View summary","5. Filter by category","6. Save & Quit"]
).ask()

 if choice=="1. Add income" :
   collect_and_add(transactions, "income")
 elif choice=="2. Add expense" :
     collect_and_add(transactions, "expense")
 elif choice == "3. View all transactions":
    if not transactions:
        print("  No transactions yet.")
    else:
        for t in transactions:
            sign = "+" if t["transaction_type"] == "income" else "-"
            print(f"  {t['date']}  {t['transaction_type']:<10}  {t['category']:<16}  {sign}{t['amount']:>10.2f} DH  {t['description']}")
 elif choice=="4. View summary" :
   view_summary(transactions)
 elif choice=="5. Filter by category" :
   filter_by_category(transactions)
 elif choice=="6. Save & Quit" :
   save_data(transactions)    
   print("  Goodbye!")
   break
    
