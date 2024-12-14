import streamlit as st
import sqlite3
from sqlite3 import Error
from faker import Faker
import pandas as pd
import random
from datetime import datetime, timedelta

# Database File
DATABASE_FILE = "food_delivery.db"

# Initialize Faker
fake = Faker()

# Function to initialize the database
def initialize_database(db_file):
    """Create database and necessary tables if they don't exist."""
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    # Customers Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Customers (
            customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            phone TEXT UNIQUE NOT NULL,
            location TEXT NOT NULL,
            signup_date TEXT NOT NULL,
            is_premium BOOLEAN NOT NULL,
            preferred_cuisine TEXT,
            total_orders INTEGER DEFAULT 0,
            average_rating REAL DEFAULT 0
        )
    ''')

    # Restaurants Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Restaurants (
            restaurant_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            cuisine_type TEXT NOT NULL,
            location TEXT NOT NULL,
            owner_name TEXT NOT NULL,
            average_delivery_time REAL,
            contact_number TEXT,
            rating REAL DEFAULT 0,
            total_orders INTEGER DEFAULT 0,
            is_active BOOLEAN NOT NULL
        )
    ''')

    # Orders Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Orders (
            order_id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_id INTEGER NOT NULL,
            restaurant_id INTEGER NOT NULL,
            order_date TEXT NOT NULL,
            delivery_time TEXT,
            status TEXT NOT NULL,
            total_amount REAL NOT NULL,
            payment_mode TEXT NOT NULL,
            discount_applied REAL,
            feedback_rating REAL,
            FOREIGN KEY (customer_id) REFERENCES Customers(customer_id),
            FOREIGN KEY (restaurant_id) REFERENCES Restaurants(restaurant_id)
        )
    ''')

    # Deliveries Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Deliveries (
            delivery_id INTEGER PRIMARY KEY AUTOINCREMENT,
            order_id INTEGER NOT NULL,
            delivery_status TEXT NOT NULL,
            distance REAL,
            delivery_time INTEGER,
            estimated_time INTEGER,
            delivery_fee REAL,
            vehicle_type TEXT,
            FOREIGN KEY (order_id) REFERENCES Orders(order_id)
        )
    ''')

    conn.commit()
    conn.close()

# Function to populate data using Faker
def populate_data():
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()

    # Populate Customers
    cursor.execute("SELECT COUNT(*) FROM Customers")
    if cursor.fetchone()[0] == 0:
        for _ in range(20):
            cursor.execute('''
                INSERT INTO Customers (name, email, phone, location, signup_date, is_premium, preferred_cuisine, total_orders, average_rating)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                fake.name(),
                fake.email(),
                fake.phone_number(),
                fake.address(),
                fake.date_between(start_date='-1y', end_date='today').strftime("%Y-%m-%d"),
                fake.boolean(),
                random.choice(['Indian', 'Chinese', 'Italian', 'Mexican']),
                random.randint(0, 50),
                round(random.uniform(3.0, 5.0), 2)
            ))

    # Populate Restaurants
    cursor.execute("SELECT COUNT(*) FROM Restaurants")
    if cursor.fetchone()[0] == 0:
        for _ in range(10):
            cursor.execute('''
                INSERT INTO Restaurants (name, cuisine_type, location, owner_name, average_delivery_time, contact_number, rating, total_orders, is_active)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                fake.company(),
                random.choice(['Indian', 'Chinese', 'Italian', 'Mexican']),
                fake.city(),
                fake.name(),
                random.randint(20, 50),
                fake.phone_number(),
                round(random.uniform(3.0, 5.0), 2),
                random.randint(0, 100),
                fake.boolean()
            ))

    # Populate Orders
    cursor.execute("SELECT COUNT(*) FROM Orders")
    if cursor.fetchone()[0] == 0:
        for _ in range(30):
            cursor.execute('''
                INSERT INTO Orders (customer_id, restaurant_id, order_date, delivery_time, status, total_amount, payment_mode, discount_applied, feedback_rating)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                random.randint(1, 20),
                random.randint(1, 10),
                fake.date_time_between(start_date='-6m', end_date='now').strftime("%Y-%m-%d %H:%M:%S"),
                fake.date_time_between(start_date='-6m', end_date='now').strftime("%Y-%m-%d %H:%M:%S"),
                random.choice(['Pending', 'Delivered', 'Cancelled']),
                round(random.uniform(100, 1000), 2),
                random.choice(['Credit Card', 'Cash', 'UPI']),
                round(random.uniform(10, 100), 2),
                round(random.uniform(3.0, 5.0), 2)
            ))

    # Populate Deliveries
    cursor.execute("SELECT COUNT(*) FROM Deliveries")
    if cursor.fetchone()[0] == 0:
        for _ in range(30):
            cursor.execute('''
                INSERT INTO Deliveries (order_id, delivery_status, distance, delivery_time, estimated_time, delivery_fee, vehicle_type)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (
                random.randint(1, 30),
                random.choice(['On the way', 'Delivered']),
                round(random.uniform(1, 20), 2),
                random.randint(15, 60),
                random.randint(10, 50),
                round(random.uniform(20, 100), 2),
                random.choice(['Bike', 'Car'])
            ))

    conn.commit()
    conn.close()

# Initialize database and populate data
initialize_database(DATABASE_FILE)
populate_data()

# Streamlit App
def main():
    st.title("Zomato - Food Delivery Data Management")

    # Database Connection
    conn = sqlite3.connect(DATABASE_FILE)

    menu = ["Customers", "Restaurants", "Orders", "Deliveries"]
    choice = st.sidebar.selectbox("Select Table", menu)

    if choice == "Customers":
        manage_customers(conn)
    elif choice == "Restaurants":
        manage_restaurants(conn)
    elif choice == "Orders":
        manage_orders(conn)
    elif choice == "Deliveries":
        manage_deliveries(conn)

    conn.close()

def manage_customers(conn):
    st.subheader("Customer Management")
    cursor = conn.cursor()

    # Add Customer
    with st.expander("Add Customer"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        phone = st.text_input("Phone")
        location = st.text_input("Location")
        signup_date = st.date_input("Signup Date")
        is_premium = st.checkbox("Premium Member")
        preferred_cuisine = st.selectbox("Preferred Cuisine", ['Indian', 'Chinese', 'Italian', 'Mexican'])

        if st.button("Add Customer"):
            cursor.execute('''
                INSERT INTO Customers (name, email, phone, location, signup_date, is_premium, preferred_cuisine)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (name, email, phone, location, signup_date, is_premium, preferred_cuisine))
            conn.commit()
            st.success("Customer added successfully!")

    # View Customers
    if st.checkbox("View All Customers"):
        customers = pd.read_sql_query("SELECT * FROM Customers", conn)
        st.dataframe(customers)

    # Update Customer
    with st.expander("Update Customer"):
        customer_id = st.number_input("Enter Customer ID to Update", min_value=1, step=1)
        field_to_update = st.selectbox("Field to Update", ['name', 'email', 'phone', 'location', 'preferred_cuisine'])
        new_value = st.text_input("Enter New Value")

        if st.button("Update Customer"):
            query = f"UPDATE Customers SET {field_to_update} = ? WHERE customer_id = ?"
            cursor.execute(query, (new_value, customer_id))
            conn.commit()
            st.success("Customer updated successfully!")

    # Delete Customer
    with st.expander("Delete Customer"):
        customer_id_to_delete = st.number_input("Enter Customer ID to Delete", min_value=1, step=1)

        if st.button("Delete Customer"):
            cursor.execute("DELETE FROM Customers WHERE customer_id = ?", (customer_id_to_delete,))
            conn.commit()
            st.success("Customer deleted successfully!")


def manage_restaurants(conn):
    st.subheader("Restaurant Management")
    cursor = conn.cursor()

    # Add Restaurant
    with st.expander("Add Restaurant"):
        name = st.text_input("Name")
        cuisine_type = st.selectbox("Cuisine Type", ['Indian', 'Chinese', 'Italian', 'Mexican'])
        location = st.text_input("Location")
        owner_name = st.text_input("Owner Name")
        average_delivery_time = st.number_input("Average Delivery Time (minutes)", min_value=1, max_value=120)
        contact_number = st.text_input("Contact Number")
        rating = st.slider("Rating", min_value=1, max_value=5)
        total_orders = st.number_input("Total Orders", min_value=0)
        is_active = st.checkbox("Is Active")

        if st.button("Add Restaurant"):
            cursor.execute('''
                INSERT INTO Restaurants (name, cuisine_type, location, owner_name, average_delivery_time, contact_number, rating, total_orders, is_active)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (name, cuisine_type, location, owner_name, average_delivery_time, contact_number, rating, total_orders, is_active))
            conn.commit()
            st.success("Restaurant added successfully!")

    # View Restaurants
    if st.checkbox("View All Restaurants"):
        restaurants = pd.read_sql_query("SELECT * FROM Restaurants", conn)
        st.dataframe(restaurants)

    # Update Restaurant
    with st.expander("Update Restaurant"):
        restaurant_id = st.number_input("Enter Restaurant ID to Update", min_value=1, step=1)
        field_to_update = st.selectbox("Field to Update", ['name', 'cuisine_type', 'location', 'owner_name', 'rating'])
        new_value = st.text_input("Enter New Value")

        if st.button("Update Restaurant"):
            query = f"UPDATE Restaurants SET {field_to_update} = ? WHERE restaurant_id = ?"
            cursor.execute(query, (new_value, restaurant_id))
            conn.commit()
            st.success("Restaurant updated successfully!")

    # Delete Restaurant
    with st.expander("Delete Restaurant"):
        restaurant_id_to_delete = st.number_input("Enter Restaurant ID to Delete", min_value=1, step=1)

        if st.button("Delete Restaurant"):
            cursor.execute("DELETE FROM Restaurants WHERE restaurant_id = ?", (restaurant_id_to_delete,))
            conn.commit()
            st.success("Restaurant deleted successfully!")


def manage_orders(conn):
    st.subheader("Order Management")
    cursor = conn.cursor()

    # Add Order
    with st.expander("Add Order"):
        customer_id = st.number_input("Customer ID", min_value=1)
        restaurant_id = st.number_input("Restaurant ID", min_value=1)
        order_date = st.date_input("Order Date")
        delivery_time = st.date_input("Delivery Time")
        status = st.selectbox("Order Status", ['Pending', 'Delivered', 'Cancelled'])
        total_amount = st.number_input("Total Amount", min_value=0.0)
        payment_mode = st.selectbox("Payment Mode", ['Credit Card', 'Cash', 'UPI'])
        discount_applied = st.number_input("Discount Applied", min_value=0.0)
        feedback_rating = st.slider("Feedback Rating", min_value=1, max_value=5)

        if st.button("Add Order"):
            cursor.execute('''
                INSERT INTO Orders (customer_id, restaurant_id, order_date, delivery_time, status, total_amount, payment_mode, discount_applied, feedback_rating)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (customer_id, restaurant_id, order_date, delivery_time, status, total_amount, payment_mode, discount_applied, feedback_rating))
            conn.commit()
            st.success("Order added successfully!")

    # View Orders
    if st.checkbox("View All Orders"):
        orders = pd.read_sql_query("SELECT * FROM Orders", conn)
        st.dataframe(orders)

    # Update Order
    with st.expander("Update Order"):
        order_id = st.number_input("Enter Order ID to Update", min_value=1, step=1)
        field_to_update = st.selectbox("Field to Update", ['status', 'total_amount', 'payment_mode', 'feedback_rating'])
        new_value = st.text_input("Enter New Value")

        if st.button("Update Order"):
            query = f"UPDATE Orders SET {field_to_update} = ? WHERE order_id = ?"
            cursor.execute(query, (new_value, order_id))
            conn.commit()
            st.success("Order updated successfully!")

    # Delete Order
    with st.expander("Delete Order"):
        order_id_to_delete = st.number_input("Enter Order ID to Delete", min_value=1, step=1)

        if st.button("Delete Order"):
            cursor.execute("DELETE FROM Orders WHERE order_id = ?", (order_id_to_delete,))
            conn.commit()
            st.success("Order deleted successfully!")


def manage_deliveries(conn):
    st.subheader("Delivery Management")
    cursor = conn.cursor()

    # Add Delivery
    with st.expander("Add Delivery"):
        order_id = st.number_input("Order ID", min_value=1)
        delivery_status = st.selectbox("Delivery Status", ['On the way', 'Delivered'])
        distance = st.number_input("Distance (km)", min_value=0.0)
        delivery_time = st.number_input("Delivery Time (min)", min_value=1)
        estimated_time = st.number_input("Estimated Time (min)", min_value=1)
        delivery_fee = st.number_input("Delivery Fee", min_value=0.0)
        vehicle_type = st.selectbox("Vehicle Type", ['Bike', 'Car'])

        if st.button("Add Delivery"):
            cursor.execute('''
                INSERT INTO Deliveries (order_id, delivery_status, distance, delivery_time, estimated_time, delivery_fee, vehicle_type)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (order_id, delivery_status, distance, delivery_time, estimated_time, delivery_fee, vehicle_type))
            conn.commit()
            st.success("Delivery added successfully!")

    # View Deliveries
    if st.checkbox("View All Deliveries"):
        deliveries = pd.read_sql_query("SELECT * FROM Deliveries", conn)
        st.dataframe(deliveries)

    # Update Delivery
    with st.expander("Update Delivery"):
        delivery_id = st.number_input("Enter Delivery ID to Update", min_value=1, step=1)
        field_to_update = st.selectbox("Field to Update", ['delivery_status', 'distance', 'delivery_fee', 'vehicle_type'])
        new_value = st.text_input("Enter New Value")

        if st.button("Update Delivery"):
            query = f"UPDATE Deliveries SET {field_to_update} = ? WHERE delivery_id = ?"
            cursor.execute(query, (new_value, delivery_id))
            conn.commit()
            st.success("Delivery updated successfully!")

    # Delete Delivery
    with st.expander("Delete Delivery"):
        delivery_id_to_delete = st.number_input("Enter Delivery ID to Delete", min_value=1, step=1)

        if st.button("Delete Delivery"):
            cursor.execute("DELETE FROM Deliveries WHERE delivery_id = ?", (delivery_id_to_delete,))
            conn.commit()
            st.success("Delivery deleted successfully!")

if __name__ == "__main__":
    main()
