# Install required libraries
#!pip install pandas faker ipywidgets

# Import libraries
import pandas as pd
import random
from faker import Faker
import ipywidgets as widgets
from IPython.display import display

fake = Faker()

# Function to generate data based on data type
def generate_data(data_type, length):
    if data_type == 'String':
        return ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz', k=length))
    elif data_type == 'Integer':
        return random.randint(10*(length-1), 10*length-1)
    elif data_type == 'Float':
        return round(random.uniform(1, 10**length), 2)
    elif data_type == 'Email':
        return fake.email()
    elif data_type == 'Date':
        return fake.date()
    elif data_type == 'Phone Number':
        return fake.phone_number()
    elif data_type == 'Address':
        return fake.address()

# Widgets to define the column name, data type, and length
column_name = widgets.Text(description="Column Name")
data_type = widgets.Dropdown(
    options=['String', 'Integer', 'Float', 'Email', 'Date', 'Phone Number', 'Address'],
    description='Data Type',
)
length = widgets.IntSlider(value=5, min=1, max=10, description='Length')
number_of_rows = widgets.IntText(value=10, description="Number of Rows")

columns = []

# Function to add columns
def add_column(_):
    columns.append({'name': column_name.value, 'data_type': data_type.value, 'length': length.value})
    column_name.value = ''  # Clear input
    display_columns()

# Function to display the added columns
def display_columns():
    column_list.value = "\n".join([f"{col['name']} ({col['data_type']}, {col['length']} chars)" for col in columns])

# Button to add columns
add_button = widgets.Button(description="Add Column")
add_button.on_click(add_column)

# Display area for the list of added columns
column_list = widgets.Textarea(description="Columns", disabled=True)

# Function to generate CSV
def generate_csv(_):
    data = {}
    for col in columns:
        data[col['name']] = [generate_data(col['data_type'], col['length']) for _ in range(number_of_rows.value)]

    df = pd.DataFrame(data)
    file_name = 'random_data.csv'
    df.to_csv(file_name, index=False)
    print(f"CSV File '{file_name}' created with {number_of_rows.value} rows and {len(columns)} columns.")

# Button to generate the CSV file
generate_button = widgets.Button(description="Generate CSV")
generate_button.on_click(generate_csv)

# Display the widgets
display(column_name, data_type, length, add_button, column_list, number_of_rows, generate_button)
