import sqlite3
from sqlite3 import Error

# Function to create a database connection
def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(f"Error: {e}")
    return None

# Execute a general query
def execute_query(conn, query):
    try:
        c = conn.cursor()
        c.execute(query)
        conn.commit()
    except Error as e:
        print(f"Error: {e}")

# Execute a read query
def execute_read_query(conn, query):
    try:
        c = conn.cursor()
        c.execute(query)
        return c.fetchall()
    except Error as e:
        print(f"Error: {e}")
        return []

# SQL for creating tables
CREATE_CUSTOMERS_TABLE = """
CREATE TABLE IF NOT EXISTS customers (
    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE,
    phone TEXT,
    location TEXT,
    signup_date DATE,
    is_premium BOOLEAN,
    preferred_cuisine TEXT,
    total_orders INTEGER DEFAULT 0,
    average_rating REAL DEFAULT 0.0
);
"""

CREATE_RESTAURANTS_TABLE = """
CREATE TABLE IF NOT EXISTS restaurants (
    restaurant_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    cuisine_type TEXT,
    location TEXT,
    owner_name TEXT,
    average_delivery_time INTEGER,
    contact_number TEXT,
    rating REAL DEFAULT 0.0,
    total_orders INTEGER DEFAULT 0,
    is_active BOOLEAN DEFAULT 1
);
"""

CREATE_ORDERS_TABLE = """
CREATE TABLE IF NOT EXISTS orders (
    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER,
    restaurant_id INTEGER,
    order_date DATETIME,
    delivery_time DATETIME,
    status TEXT,
    total_amount REAL,
    payment_mode TEXT,
    discount_applied REAL,
    feedback_rating REAL,
    FOREIGN KEY (customer_id) REFERENCES customers (customer_id),
    FOREIGN KEY (restaurant_id) REFERENCES restaurants (restaurant_id)
);
"""

CREATE_DELIVERIES_TABLE = """
CREATE TABLE IF NOT EXISTS deliveries (
    delivery_id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER,
    delivery_person_id INTEGER,
    delivery_status TEXT,
    distance REAL,
    delivery_time INTEGER,
    estimated_time INTEGER,
    delivery_fee REAL,
    vehicle_type TEXT,
    FOREIGN KEY (order_id) REFERENCES orders (order_id)
);
"""

CREATE_DELIVERY_PERSONS_TABLE = """
CREATE TABLE IF NOT EXISTS delivery_persons (
    delivery_person_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    contact_number TEXT,
    vehicle_type TEXT,
    total_deliveries INTEGER DEFAULT 0,
    average_rating REAL DEFAULT 0.0,
    location TEXT
);
"""

# Initialize database with all tables
def initialize_database(db_file):
    conn = create_connection(db_file)
    if conn:
        execute_query(conn, CREATE_CUSTOMERS_TABLE)
        execute_query(conn, CREATE_RESTAURANTS_TABLE)
        execute_query(conn, CREATE_ORDERS_TABLE)
        execute_query(conn, CREATE_DELIVERIES_TABLE)
        execute_query(conn, CREATE_DELIVERY_PERSONS_TABLE)
    else:
        print("Error: Unable to connect to the database.")
