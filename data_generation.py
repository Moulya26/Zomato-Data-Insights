from faker import Faker
import random
from database import create_connection, execute_query

fake = Faker()

# Insert sample data into the database
def populate_sample_data(db_file):
    conn = create_connection(db_file)

    if conn:
        # Populate Customers
        for _ in range(20):
            query = f"""
            INSERT INTO customers (name, email, phone, location, signup_date, is_premium, preferred_cuisine)
            VALUES (
                '{fake.name()}',
                '{fake.email()}',
                '{fake.phone_number()}',
                '{fake.address()}',
                '{fake.date()}',
                {random.choice([0, 1])},
                '{random.choice(["Indian", "Chinese", "Italian", "Mexican", "Thai"])}'
            );
            """
            execute_query(conn, query)

        # Populate Restaurants
        for _ in range(10):
            query = f"""
            INSERT INTO restaurants (name, cuisine_type, location, owner_name, average_delivery_time, contact_number, rating)
            VALUES (
                '{fake.company()}',
                '{random.choice(["Indian", "Chinese", "Italian", "Mexican", "Thai"])}',
                '{fake.address()}',
                '{fake.name()}',
                {random.randint(15, 45)},
                '{fake.phone_number()}',
                {round(random.uniform(3.0, 5.0), 1)}
            );
            """
            execute_query(conn, query)

        print("Sample data populated successfully.")
    else:
        print("Error: Unable to populate data.")
