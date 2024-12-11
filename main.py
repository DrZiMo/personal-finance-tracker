import pandas as pd
import csv
from datetime import datetime
from data_entry import get_date, get_amount, get_catagory, get_description

class CSV:
    CSV_FILE = "finance_data.csv"
    COLUMNS = ["date", "amount", "catagory", "description"]
    FORMAT = "%d-%m-%Y"

    @classmethod
    def initialize_csv(cls):
        try:
            pd.read_csv(cls.CSV_FILE)
        except FileNotFoundError:
            df = pd.DataFrame(columns = cls.COLUMNS)
            df.to_csv(cls.CSV_FILE, index=False)
    
    @classmethod
    def add_entry(cls, date, amount, catagory, description):
        new_entry = {
            "date": date,
            "amount": amount,
            "catagory": catagory,
            "description": description
        }
        with open(cls.CSV_FILE, "a", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=cls.COLUMNS)
            writer.writerow(new_entry)
        print("Entry added successfully!")
    
    @classmethod
    def get_transaction(cls, start_date, end_date):
        df = pd.read_csv(cls.CSV_FILE)
        df["date"] = pd.to_datetime(df["date"], format=CSV.FORMAT)
        start_date = datetime.strptime(start_date, CSV.FORMAT)
        end_date = datetime.strptime(end_date, CSV.FORMAT)

        mask = (df["date"] >= start_date) & (df["date"] <= end_date)
        filtered_df = df.loc[mask]

        if filtered_df.empty:
            print ("No transactions found in the given data range!")
        else:
            print(f"Transaction from {start_date.strftime(CSV.FORMAT)} to {end_date.strftime(CSV.FORMAT)}")
            print(filtered_df.to_string(index=False, formatters={"date": lambda x: x.strftime(CSV.FORMAT)}))

            total_income = filtered_df[filtered_df["catagory"] == "Income"]["amount"].sum()
            total_expense = filtered_df[filtered_df["catagory"] == "Expense"]["amount"].sum()

            print("\nSummary:")
            print(f"Total Income: ${total_income:.2f}")
            print(f"Total Expense: ${total_expense:.2f}")
            print(f"Net savings: ${(total_income - total_expense):.2f}")

        return filtered_df

def add():
    CSV.initialize_csv()
    date = get_date("Enter the date of the transaction (dd-mm-yyy) or enter for todays date: ", allow_default=True)
    amount = get_amount()
    catagory = get_catagory()
    description = get_description()
    CSV.add_entry(date, amount, catagory, description)

CSV.get_transaction("01-01-2023", "20-07-2024")