import pandas as pd
import csv
from datetime import datetime
from dt_entry import getdate, get_amt, get_category, get_description


class CSV:
    CSV_FILE = 'data.csv'
    dt_format = "%d-%m-%Y"
    COLS = ["date","amount","category","description"]

    @classmethod
    def write_csv(cls):
        try:
            pd.read_csv(cls.CSV_FILE)
        except FileNotFoundError:
            df = pd.DataFrame(columns= cls.COLS)
            df.to_csv(cls.CSV_FILE,index=False) 
    @classmethod
    def add_entry(cls,date,amount,category,description):
        new_entry={
            "date":date,
            "amount": amount,
            "category": category,
            "description": description
        }

        with open(cls.CSV_FILE, "a", newline= '') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames= cls.COLS)
            writer.writerow(new_entry)
        print("Entry added successfully!")

    @classmethod
    def get_trans(cls, start_date, end_date):
        df = pd.read_csv(cls.CSV_FILE)
        df['date'] = pd.to_datetime(df['date'], format=CSV.dt_format)


def add():
    CSV.write_csv()
    date = getdate("Enter date (dd-mm-yyyy): ", allow_default=True)
    amount = get_amt()
    category = get_category()
    description = get_description()
    
    CSV.add_entry(date, amount, category, description)


