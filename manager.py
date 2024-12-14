import streamlit as st
import pandas as pd

class DatabaseManager:
    def __init__(self, conn):
        self.conn = conn
        self.cursor = conn.cursor()

    def manage_customers(self):
        st.subheader("Customer Management")

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
                self.cursor.execute('''
                    INSERT INTO Customers (name, email, phone, location, signup_date, is_premium, preferred_cuisine)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                ''', (name, email, phone, location, signup_date, is_premium, preferred_cuisine))
                self.conn.commit()
                st.success("Customer added successfully!")

        # View Customers
        if st.checkbox("View All Customers"):
            customers = pd.read_sql_query("SELECT * FROM Customers", self.conn)
            st.dataframe(customers)

        # Update Customer
        with st.expander("Update Customer"):
            customer_id = st.number_input("Enter Customer ID to Update", min_value=1, step=1)
            field_to_update = st.selectbox("Field to Update", ['name', 'email', 'phone', 'location', 'preferred_cuisine'])
            new_value = st.text_input("Enter New Value")

            if st.button("Update Customer"):
                query = f"UPDATE Customers SET {field_to_update} = ? WHERE customer_id = ?"
                self.cursor.execute(query, (new_value, customer_id))
                self.conn.commit()
                st.success("Customer updated successfully!")

        # Delete Customer
        with st.expander("Delete Customer"):
            customer_id_to_delete = st.number_input("Enter Customer ID to Delete", min_value=1, step=1)

            if st.button("Delete Customer"):
                self.cursor.execute("DELETE FROM Customers WHERE customer_id = ?", (customer_id_to_delete,))
                self.conn.commit()
                st.success("Customer deleted successfully!")

    def manage_restaurants(self):
        st.subheader("Restaurant Management")

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
                self.cursor.execute('''
                    INSERT INTO Restaurants (name, cuisine_type, location, owner_name, average_delivery_time, contact_number, rating, total_orders, is_active)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                ''', (name, cuisine_type, location, owner_name, average_delivery_time, contact_number, rating, total_orders, is_active))
                self.conn.commit()
                st.success("Restaurant added successfully!")

        # View Restaurants
        if st.checkbox("View All Restaurants"):
            restaurants = pd.read_sql_query("SELECT * FROM Restaurants", self.conn)
            st.dataframe(restaurants)

        # Update Restaurant
        with st.expander("Update Restaurant"):
            restaurant_id = st.number_input("Enter Restaurant ID to Update", min_value=1, step=1)
            field_to_update = st.selectbox("Field to Update", ['name', 'cuisine_type', 'location', 'owner_name', 'rating'])
            new_value = st.text_input("Enter New Value")

            if st.button("Update Restaurant"):
                query = f"UPDATE Restaurants SET {field_to_update} = ? WHERE restaurant_id = ?"
                self.cursor.execute(query, (new_value, restaurant_id))
                self.conn.commit()
                st.success("Restaurant updated successfully!")

        # Delete Restaurant
        with st.expander("Delete Restaurant"):
            restaurant_id_to_delete = st.number_input("Enter Restaurant ID to Delete", min_value=1, step=1)

            if st.button("Delete Restaurant"):
                self.cursor.execute("DELETE FROM Restaurants WHERE restaurant_id = ?", (restaurant_id_to_delete,))
                self.conn.commit()
                st.success("Restaurant deleted successfully!")

    def manage_orders(self):
        st.subheader("Order Management")

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
                self.cursor.execute('''
                    INSERT INTO Orders (customer_id, restaurant_id, order_date, delivery_time, status, total_amount, payment_mode, discount_applied, feedback_rating)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                ''', (customer_id, restaurant_id, order_date, delivery_time, status, total_amount, payment_mode, discount_applied, feedback_rating))
                self.conn.commit()
                st.success("Order added successfully!")

        # View Orders
        if st.checkbox("View All Orders"):
            orders = pd.read_sql_query("SELECT * FROM Orders", self.conn)
            st.dataframe(orders)

        # Update Order
        with st.expander("Update Order"):
            order_id = st.number_input("Enter Order ID to Update", min_value=1, step=1)
            field_to_update = st.selectbox("Field to Update", ['status', 'total_amount', 'payment_mode', 'feedback_rating'])
            new_value = st.text_input("Enter New Value")

            if st.button("Update Order"):
                query = f"UPDATE Orders SET {field_to_update} = ? WHERE order_id = ?"
                self.cursor.execute(query, (new_value, order_id))
                self.conn.commit()
                st.success("Order updated successfully!")

        # Delete Order
        with st.expander("Delete Order"):
            order_id_to_delete = st.number_input("Enter Order ID to Delete", min_value=1, step=1)

            if st.button("Delete Order"):
                self.cursor.execute("DELETE FROM Orders WHERE order_id = ?", (order_id_to_delete,))
                self.conn.commit()
                st.success("Order deleted successfully!")

    def manage_deliveries(self):
        st.subheader("Delivery Management")

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
                self.cursor.execute('''
                    INSERT INTO Deliveries (order_id, delivery_status, distance, delivery_time, estimated_time, delivery_fee, vehicle_type)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                ''', (order_id, delivery_status, distance, delivery_time, estimated_time, delivery_fee, vehicle_type))
                self.conn.commit()
                st.success("Delivery added successfully!")

        # View Deliveries
        if st.checkbox("View All Deliveries"):
            deliveries = pd.read_sql_query("SELECT * FROM Deliveries", self.conn)
            st.dataframe(deliveries)

        # Update Delivery
        with st.expander("Update Delivery"):
            delivery_id = st.number_input("Enter Delivery ID to Update", min_value=1, step=1)
            field_to_update = st.selectbox("Field to Update", ['delivery_status', 'distance', 'delivery_fee', 'vehicle_type'])
            new_value = st.text_input("Enter New Value")

            if st.button("Update Delivery"):
                query = f"UPDATE Deliveries SET {field_to_update} = ? WHERE delivery_id = ?"
                self.cursor.execute(query, (new_value, delivery_id))
                self.conn.commit()
                st.success("Delivery updated successfully!")

        # Delete Delivery
        with st.expander("Delete Delivery"):
            delivery_id_to_delete = st.number_input("Enter Delivery ID to Delete", min_value=1, step=1)

            if st.button("Delete Delivery"):
                self.cursor.execute("DELETE FROM Deliveries WHERE delivery_id = ?", (delivery_id_to_delete,))
                self.conn.commit()
                st.success("Delivery deleted successfully!")

    def manage_columns(self):
        """
        Manage Columns in Customers, Restaurants, Orders, and Deliveries tables.
        """
        st.subheader("Column Management")

        table_name = st.selectbox("Select Table", ["Customers", "Restaurants", "Orders", "Deliveries"])
        operation = st.selectbox("Operation", ["Add Column", "Delete Column", "Update Column Name"])

        if operation == "Add Column":
            column_name = st.text_input("New Column Name")
            column_type = st.selectbox("Column Type", ["TEXT", "INTEGER", "REAL", "BOOLEAN", "DATE"])
            if st.button(f"Add Column to {table_name}"):
                query = f"ALTER TABLE {table_name} ADD COLUMN {column_name} {column_type}"
                try:
                    self.cursor.execute(query)
                    self.conn.commit()
                    st.success(f"Column {column_name} added to {table_name}!")
                except Exception as e:
                    st.error(f"Error: {e}")

        elif operation == "Delete Column":
            st.warning("Deleting a column is not natively supported in SQLite. It requires recreating the table.")
            st.info("Please consult a database administrator for this operation.")
            # Optional implementation: Table recreation logic

        elif operation == "Update Column Name":
            old_column_name = st.text_input("Old Column Name")
            new_column_name = st.text_input("New Column Name")
            if st.button(f"Update Column Name in {table_name}"):
                st.warning("Renaming a column is not natively supported in SQLite. Consider using table recreation logic.")

        st.info("SQLite has limited support for modifying table structures. Use carefully.")

    def query_section(self):
        """
        Allows the user to select from a list of predefined SQL queries to analyze the data.
        Displays the results in a readable format.
        """
        st.subheader("Query Section")

        # List of predefined SQL queries with updated queries
        queries = [
            ("1. Get the total number of customers", "SELECT COUNT(*) FROM customers"),
            ("2. Get the details of top 5 customers by total orders", "SELECT * FROM customers ORDER BY total_orders DESC LIMIT 5"),
            ("3. Get the average order value for all customers", "SELECT AVG(total_amount) FROM orders"),
            ("4. Get the total number of orders for each restaurant", "SELECT restaurant_id, COUNT(*) AS total_orders FROM orders GROUP BY restaurant_id"),
            ("5. Get the total revenue for each restaurant", "SELECT restaurant_id, SUM(total_amount) AS total_revenue FROM orders GROUP BY restaurant_id"),
            ("6. Get the number of orders placed each month in the last year", 
             "SELECT strftime('%Y-%m', order_date) AS month, COUNT(*) AS total_orders FROM orders WHERE order_date >= DATE('now', '-1 year') GROUP BY month ORDER BY month DESC"),
            ("7. Get the most popular restaurant by total orders", "SELECT restaurant_id, COUNT(*) AS total_orders FROM orders GROUP BY restaurant_id ORDER BY total_orders DESC LIMIT 1"),
            ("8. Get the total number of canceled orders per restaurant", 
             "SELECT restaurant_id, COUNT(*) AS canceled_orders FROM orders WHERE status = 'Cancelled' GROUP BY restaurant_id"),
            ("9. Get the total revenue generated for each month", 
             "SELECT strftime('%Y-%m', order_date) AS month, SUM(total_amount) AS total_revenue FROM orders GROUP BY month ORDER BY month DESC"),
            ("10. Get the top 3 restaurants by rating", "SELECT restaurant_id, AVG(rating) AS avg_rating FROM restaurants GROUP BY restaurant_id ORDER BY avg_rating DESC LIMIT 3"),
            ("11. Get the average discount applied for all orders", "SELECT AVG(discount_applied) FROM orders"),
            ("12. Get the average order amount for premium customers", "SELECT AVG(total_amount) FROM orders WHERE customer_id IN (SELECT customer_id FROM customers WHERE is_premium = 1)"),
            ("13. Get the total number of canceled orders", "SELECT COUNT(*) FROM orders WHERE status = 'Cancelled'"),
            ("14. Get the average rating given to restaurants for each restaurant", 
             "SELECT restaurant_id, AVG(rating) AS avg_rating FROM restaurants GROUP BY restaurant_id"),
            ("15. Get the most common cuisine types ordered by customers", "SELECT preferred_cuisine, COUNT(*) AS frequency FROM customers GROUP BY preferred_cuisine ORDER BY frequency DESC LIMIT 5"),
            ("16. Get the orders placed in the last 7 days", "SELECT * FROM orders WHERE order_date >= DATE('now', '-7 days')"),
            ("17. Get the average delivery fee for orders", "SELECT AVG(delivery_fee) FROM deliveries"),
            ("18. Get the number of active restaurants", "SELECT COUNT(*) FROM restaurants WHERE is_active = 1"),
            ("19. Get the total number of orders placed per day", "SELECT DATE(order_date) AS order_day, COUNT(*) AS total_orders FROM orders GROUP BY order_day ORDER BY order_day DESC"),
            ("20. Get the total revenue for the last 30 days", "SELECT SUM(total_amount) FROM orders WHERE order_date >= DATE('now', '-30 days')")
        ]

        # Let the user select a query
        selected_query = st.selectbox("Choose a query to execute", [query[0] for query in queries])

        # Find the query that matches the selected one
        query_to_run = None
        for query in queries:
            if query[0] == selected_query:
                query_to_run = query[1]
                break

        # Execute the selected query and display the result
        if query_to_run:
            try:
                self.cursor.execute(query_to_run)
                result = self.cursor.fetchall()
                columns = [description[0] for description in self.cursor.description]  # Get column names from cursor description
                
                # Convert result to DataFrame
                df = pd.DataFrame(result, columns=columns)
                
                if not df.empty:
                    st.write("Query Results:")
                    st.dataframe(df)  # Display the DataFrame directly without passing 'columns'
                else:
                    st.info("No results found for the selected query.")
            except Exception as e:
                st.error(f"Error executing query: {e}")

    def manage_tables(self):
        """
        Manage Tables - Create, Read, Delete, Update Tables, Populate Tables with Data, and View Contents.
        """
        st.subheader("Table Management with Content Visibility")

        # Select Operation
        operation = st.selectbox(
            "Select Operation",
            ["Create Table", "View Tables", "View Table Content", "Delete Table", "Update Table Name", "Populate Table"]
        )

        if operation == "Create Table":
            table_name = st.text_input("Enter New Table Name")
            columns = st.text_area(
                "Define Columns (e.g., column1 TYPE, column2 TYPE, ...)", 
                placeholder="Example: id INTEGER PRIMARY KEY, name TEXT, age INTEGER"
            )
            if st.button("Create Table"):
                if table_name and columns:
                    try:
                        query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns})"
                        self.cursor.execute(query)
                        self.conn.commit()
                        st.success(f"Table '{table_name}' created successfully!")
                    except Exception as e:
                        st.error(f"Error: {e}")
                else:
                    st.warning("Please provide both table name and column definitions.")

        elif operation == "Populate Table":
            query = "SELECT name FROM sqlite_master WHERE type='table';"
            self.cursor.execute(query)
            tables = [table[0] for table in self.cursor.fetchall()]
            selected_table = st.selectbox("Select Table to Populate", tables)
            if selected_table:
                st.write(f"Populating table '{selected_table}'")
                self.cursor.execute(f"PRAGMA table_info({selected_table})")
                columns = self.cursor.fetchall()
                column_names = [col[1] for col in columns]

                # Input form for populating the table
                input_data = {}
                for col in column_names:
                    input_data[col] = st.text_input(f"Enter value for {col}")
                
                if st.button(f"Populate {selected_table}"):
                    try:
                        # Prepare the data for insertion
                        placeholders = ", ".join(["?" for _ in column_names])
                        values = tuple(input_data[col] for col in column_names)
                        query = f"INSERT INTO {selected_table} ({', '.join(column_names)}) VALUES ({placeholders})"
                        self.cursor.execute(query, values)
                        self.conn.commit()
                        st.success(f"Data inserted into '{selected_table}' successfully!")
                    except Exception as e:
                        st.error(f"Error: {e}")

        elif operation == "View Tables":
            query = "SELECT name FROM sqlite_master WHERE type='table';"
            self.cursor.execute(query)
            tables = self.cursor.fetchall()
            if tables:
                st.write("Existing Tables:")
                for table in tables:
                    st.write(f"- {table[0]}")
            else:
                st.info("No tables found.")

        elif operation == "View Table Content":
            query = "SELECT name FROM sqlite_master WHERE type='table';"
            self.cursor.execute(query)
            tables = [table[0] for table in self.cursor.fetchall()]
            selected_table = st.selectbox("Select Table to View Content", tables)
            if st.button("View Content"):
                try:
                    self.cursor.execute(f"SELECT * FROM {selected_table}")
                    rows = self.cursor.fetchall()
                    if rows:
                        st.write(f"Contents of {selected_table}:")
                        st.dataframe(rows)
                    else:
                        st.info(f"No data found in table '{selected_table}'.")
                except Exception as e:
                    st.error(f"Error: {e}")

        elif operation == "Delete Table":
            query = "SELECT name FROM sqlite_master WHERE type='table';"
            self.cursor.execute(query)
            tables = [table[0] for table in self.cursor.fetchall()]
            table_to_delete = st.selectbox("Select Table to Delete", tables)
            if st.button(f"Delete {table_to_delete}"):
                try:
                    self.cursor.execute(f"DROP TABLE IF EXISTS {table_to_delete}")
                    self.conn.commit()
                    st.success(f"Table '{table_to_delete}' deleted successfully!")
                except Exception as e:
                    st.error(f"Error: {e}")

        elif operation == "Update Table Name":
            query = "SELECT name FROM sqlite_master WHERE type='table';"
            self.cursor.execute(query)
            tables = [table[0] for table in self.cursor.fetchall()]
            table_to_update = st.selectbox("Select Table to Rename", tables)
            new_table_name = st.text_input("Enter New Table Name")
            if st.button(f"Rename '{table_to_update}' to '{new_table_name}'"):
                try:
                    self.cursor.execute(f"ALTER TABLE {table_to_update} RENAME TO {new_table_name}")
                    self.conn.commit()
                    st.success(f"Table renamed from '{table_to_update}' to '{new_table_name}'!")
                except Exception as e:
                    st.error(f"Error: {e}")