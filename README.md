# Python-Project
-->Creating a Simple Python Application for a fictional chocolate house that uses SQLite to manage,
●Seasonal flavor offerings 
●Ingredient inventory
●Customer flavor suggestions and allergy concerns.

This program gives a foundational structure to manage chocolate house data effectively.
I have created this application using visual studio codes and SQLite with python programming language.

VS Code is a free, lightweight, and powerful source code editor developed by Microsoft. It is one of the most popular development environments for Python and supports many other languages.

SQLite is a self-contained, serverless, and zero-configuration database engine. It’s one of the most popular databases for small to medium applications and is built directly into Python as part of its standard library.
Python’s sqlite3 module provides an easy way to work with SQLite databases, making it a good choice for small applications.

Setup:

Install Required Library:
Ensuring the sqlite3 library installed. we can install it using pip:
-->pip install sqlite3

Database Structure:

The database consists of three tables:

seasonal_flavors:

id: Unique identifier for each flavor
flavor_name: Name of the flavor
description: Description of the flavor
available_till: Date until which the flavor is available

ingredient_inventory:

id: Unique identifier for each ingredient
ingredient_name: Name of the ingredient
quantity: Quantity of the ingredient
unit: Unit of measurement for the quantity
customer_suggestions:

id: Unique identifier for each suggestion
customer_name: Name of the customer
suggested_flavor: Flavor suggested by the customer
allergy_concern: Any allergy concerns mentioned by the customer

