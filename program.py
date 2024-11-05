import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('chocolate_house.db')
cursor = conn.cursor()

# Create tables
cursor.execute('''CREATE TABLE IF NOT EXISTS seasonal_flavors (
                    id INTEGER PRIMARY KEY,
                    flavor_name TEXT,
                    description TEXT,
                    available_till DATE)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS ingredient_inventory (
                    id INTEGER PRIMARY KEY,
                    ingredient_name TEXT,
                    quantity INTEGER,
                    unit TEXT)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS customer_suggestions (
                    id INTEGER PRIMARY KEY,
                    customer_name TEXT,
                    suggested_flavor TEXT,
                    allergy_concern TEXT)''')

conn.commit()

# Functions to add data to the tables

def add_seasonal_flavor(flavor_name, description, available_till):
    cursor.execute('''INSERT INTO seasonal_flavors (flavor_name, description, available_till)
                      VALUES (?, ?, ?)''', (flavor_name, description, available_till))
    conn.commit()
    print("Seasonal flavor added successfully!")

def add_ingredient(ingredient_name, quantity, unit):
    cursor.execute('''INSERT INTO ingredient_inventory (ingredient_name, quantity, unit)
                      VALUES (?, ?, ?)''', (ingredient_name, quantity, unit))
    conn.commit()
    print("Ingredient added to inventory successfully!")

def add_customer_suggestion(customer_name, suggested_flavor, allergy_concern):
    cursor.execute('''INSERT INTO customer_suggestions (customer_name, suggested_flavor, allergy_concern)
                      VALUES (?, ?, ?)''', (customer_name, suggested_flavor, allergy_concern))
    conn.commit()
    print("Customer suggestion added successfully!")

# Functions to retrieve data from the tables

def view_seasonal_flavors():
    cursor.execute('''SELECT * FROM seasonal_flavors''')
    flavors = cursor.fetchall()
    for flavor in flavors:
        print(flavor)

def view_ingredient_inventory():
    cursor.execute('''SELECT * FROM ingredient_inventory''')
    ingredients = cursor.fetchall()
    for ingredient in ingredients:
        print(ingredient)

def view_customer_suggestions():
    cursor.execute('''SELECT * FROM customer_suggestions''')
    suggestions = cursor.fetchall()
    for suggestion in suggestions:
        print(suggestion)

# Main Program
while True:
    print("\nWelcome to the Chocolate House Management System")
    print("1. Add Seasonal Flavor")
    print("2. Add Ingredient to Inventory")
    print("3. Add Customer Suggestion")
    print("4. View Seasonal Flavors")
    print("5. View Ingredient Inventory")
    print("6. View Customer Suggestions")
    print("7. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        flavor_name = input("Enter flavor name: ")
        description = input("Enter description: ")
        available_till = input("Enter availability date (YYYY-MM-DD): ")
        add_seasonal_flavor(flavor_name, description, available_till)

    elif choice == '2':
        ingredient_name = input("Enter ingredient name: ")
        quantity = int(input("Enter quantity: "))
        unit = input("Enter unit (e.g., kg, g, liters): ")
        add_ingredient(ingredient_name, quantity, unit)

    elif choice == '3':
        customer_name = input("Enter customer name: ")
        suggested_flavor = input("Enter suggested flavor: ")
        allergy_concern = input("Enter allergy concern (if any): ")
        add_customer_suggestion(customer_name, suggested_flavor, allergy_concern)

    elif choice == '4':
        print("Seasonal Flavors:")
        view_seasonal_flavors()

    elif choice == '5':
        print("Ingredient Inventory:")
        view_ingredient_inventory()

    elif choice == '6':
        print("Customer Suggestions:")
        view_customer_suggestions()

    elif choice == '7':
        print("Exiting... Goodbye!")
        break

    else:
        print("Invalid choice, please try again.")

# Close the database connection
conn.close()
