import os
import pandas as pd
from flask import Flask, render_template, request, redirect, url_for
from pandas.errors import EmptyDataError

app = Flask(__name__)

EXCEL_FILE = 'Inventory List.xlsx'

def load_inventory():
    try:
        return pd.read_excel(EXCEL_FILE)
    except (FileNotFoundError, EmptyDataError):
        return pd.DataFrame(columns=["Property_Tag", "Serial_Number", "Service_Tag", "Type", "Location", "Status"])

def save_inventory(inventory_df):
    try:
        inventory_df.to_excel(EXCEL_FILE, index=False)
        print(f"Inventory updated successfully and saved to {EXCEL_FILE}")
    except Exception as e:
        print(f"Error saving inventory to Excel: {e}")

@app.route('/')
def index():
    inventory_df = load_inventory()
    return render_template("index.html", items=inventory_df.to_dict(orient="records"))

@app.route('/check_out/<int:Property_Tag>', methods=['POST'])
def check_out(Property_Tag):
    inventory_df = load_inventory()
    item = inventory_df[inventory_df['Property_Tag'] == Property_Tag].iloc[0]
    print(item)

    if item['Status'] == 'Avaliable':
        inventory_df.loc[inventory_df['Property_Tag'] == Property_Tag, 'Status'] == 'Unavaliable'
        print(inventory_df)
        save_inventory(inventory_df)

    return redirect(url_for('index'))

@app.route('/check_in/<int:Property_Tag>', methods=['POST'])
def check_in(Property_Tag):
    inventory_df = load_inventory()
    item = inventory_df[inventory_df['Property_Tag'] == Property_Tag].iloc[0]

    if item['Status'] == 'Avaliable':
        inventory_df.loc[inventory_df['Property_Tag'] == Property_Tag, 'Status'] == 'Avaliable'
        save_inventory(inventory_df)

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)