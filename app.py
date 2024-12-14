import streamlit as st
import sqlite3
from manager import DatabaseManager  # Import the class from manager.py

DATABASE_FILE = 'food_delivery.db'

def main():
    st.title("Zomato - Food Delivery Data Management")

    # Database Connection
    conn = sqlite3.connect(DATABASE_FILE)

    st.sidebar.title("Navigation")
    menu = st.sidebar.radio(
        "Menu",
        ["Home", "Manage Customers", "Manage Restaurants", "Manage Orders", "Manage Deliveries", "Column Management", "Query Section", "Table Management"]
    )

    # Create an instance of the DatabaseManager class
    manager = DatabaseManager(conn)

    if menu == "Manage Customers":
        manager.manage_customers()
    elif menu == "Manage Restaurants":
        manager.manage_restaurants()
    elif menu == "Manage Orders":
        manager.manage_orders()
    elif menu == "Manage Deliveries":
        manager.manage_deliveries()
    elif menu == "Column Management":
        manager.manage_columns()
    elif menu == "Query Section":
        manager.query_section()
    elif menu == "Table Management":
        manager.manage_tables()
    else:
        st.write("Welcome to the Food Delivery Management App!")
    
    conn.close()

if __name__ == "__main__":
    main()
