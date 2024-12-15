This file is structured to provide a clear overview, installation steps, and detailed descriptions of the project components.

---

# Zomato Data Insights

## **Overview**

This project is an interactive tool for managing and analyzing food delivery data inspired by Zomato's operational requirements. Built with **Python**, **SQLite**, and **Streamlit**, this tool enables seamless database management and insight generation to improve operational efficiency and customer satisfaction. Key features include CRUD operations, dynamic table creation and modification, data visualization, and SQL query execution.

---

## **Features**

### **1. Database Management**
- Perform **CRUD (Create, Read, Update, Delete)** operations on `Customers`, `Orders`, `Restaurants`, and `Deliveries` tables.
- Dynamically create, populate, edit, and delete new tables.
- Add, update, or delete columns from existing tables.

### **2. Query Execution**
- Execute 20 predefined SQL queries for business insights, such as:
  - Identifying peak ordering times.
  - Analyzing customer preferences and top restaurants.
  - Tracking delivery performance.

### **3. Data Insights Visualization**
- Generate actionable insights into food delivery data using **SQL queries**.
- View results in a user-friendly interface powered by **Streamlit**.

### **4. Modular and Extensible Design**
- Follows a modular structure to ensure code reusability and scalability.
- Encapsulates functionality in Python classes, enabling clean integration and easier maintenance.

---

### Technologies Used

- **Python** 3.9+
- **SQLite** for database management
- **Streamlit** for interactive web UI
- **Faker** for generating synthetic data
- **Pandas** for data manipulation

---

## **Installation and Setup**

### **1. Clone the Repository**
```bash
git clone https://github.com/Moulya26/Zomato-Data-Insights.git
cd Zomato-Data-Insights
```

### **2. Install Dependencies**
Ensure you have Python 3.8+ installed. Install the required packages using `pip`:

```bash
pip install -r requirements.txt
```

### **3. Run the Application**
Launch the Streamlit application:
```bash
streamlit run app.py
```

---

## **Project Structure**

```
Zomato-Data-Insights/
├── app.py                # Main entry point for the Streamlit application.
├── data_generation.py    # Generates synthetic data using the Faker library.
├── database.py           # Contains functions for database initialization and connection.
├── food_delivery.db      # SQLite database file storing all data.
├── manager.py            # Contains the DatabaseManager class for CRUD operations and table management.
├── queries.py            # Houses predefined SQL queries for analysis.
├── requirements.txt      # Lists Python dependencies for the project.
```

### **File Descriptions**

#### **1. `app.py`**
The main application file that serves as the entry point for the Streamlit app. It integrates all features:
- Navigation through sections: `CRUD Operations`, `Query Execution`, and `Manage Tables`.
- Invokes `DatabaseManager` methods to interact with the database.
- Displays query results and table contents.

#### **2. `data_generation.py`**
Generates synthetic data for tables like `Customers`, `Restaurants`, `Orders`, and `Deliveries` using the **Faker** library. It ensures:
- Randomized but realistic data.
- Easy population of the database.

#### **3. `database.py`**
Handles database connection and initialization:
- Creates necessary tables (`Customers`, `Orders`, `Restaurants`, `Deliveries`) if they do not exist.
- Provides a helper function to connect to the SQLite database.

#### **4. `food_delivery.db`**
The SQLite database file that stores all project data, including:
- Customers: Information about users of the platform.
- Restaurants: Restaurant details and metrics.
- Orders: Tracks order details, amounts, and statuses.
- Deliveries: Tracks delivery information and performance metrics.

#### **5. `manager.py`**
Contains the **`DatabaseManager` class**, which encapsulates database interactions:
- CRUD operations for existing tables.
- Dynamic creation and management of new tables.
- Column-level operations like adding, editing, and deleting columns.

#### **6. `queries.py`**
Houses predefined SQL queries for business insights. These queries cover:
- Customer analytics (preferences, order patterns).
- Restaurant performance (most popular cuisines, ratings).
- Delivery optimization (delays, personnel performance).

#### **7. `requirements.txt`**
Lists all required Python libraries, including:
- `streamlit`: For building the user interface.
- `sqlite3`: For database management.
- `faker`: For synthetic data generation.

---

## **How to Use**

### **1. CRUD Operations**
- Navigate to the `CRUD Operations` section in the app.
- Select a table (e.g., Customers, Restaurants, Orders, or Deliveries).
- Add, update, view, or delete records directly using the form-based interface.

### **2. Query Execution**
- Go to the `Query Execution` section.
- Select from 20 predefined SQL queries to generate insights.
- View results in a tabular format within the Streamlit app.

### **3. Manage Tables**
- Navigate to the `Manage Tables` section.
- Create new tables by specifying table names and column definitions.
- View, edit, or delete newly created tables directly within the app.

---

## **Predefined SQL Queries**

Here are some example queries from `queries.py`:

1. **Top Customers by Total Orders**:
   ```sql
   SELECT name, total_orders, average_rating FROM customers ORDER BY total_orders DESC LIMIT 10;
   ```
2. **Most Popular Restaurants**:
   ```sql
   SELECT name, total_orders, rating FROM restaurants ORDER BY total_orders DESC LIMIT 10;
   ```
3. **Peak Ordering Time**:
   ```sql
   SELECT strftime('%H', order_date) AS hour, COUNT(*) AS order_count
   FROM orders GROUP BY hour ORDER BY order_count DESC;
   ```
4. **Average Delivery Time by Restaurant**:
   ```sql
   SELECT r.name, AVG(d.delivery_time) AS avg_delivery_time
   FROM restaurants r
   JOIN orders o ON r.restaurant_id = o.restaurant_id
   JOIN deliveries d ON o.order_id = d.order_id
   GROUP BY r.name
   ORDER BY avg_delivery_time ASC;
   ```

---

## **Key Features of the Code**

### **1. Modular Design**
Encapsulates functionality into reusable Python classes and methods, enabling:
- Easy addition of new features.
- Clean and maintainable code.

### **2. Dynamic Table Management**
- Create tables dynamically based on user input.
- Populate tables with synthetic or manually entered data.
- Modify or delete tables as needed.

### **3. SQL Query Flexibility**
- Use built-in queries for insights.
- Easily add custom SQL queries for additional analysis.

---

## **Future Enhancements**

- **Visualization**: Add charts for visualizing query results.
- **Authentication**: Add a login system for secure access.
- **API Integration**: Enable integration with external data sources.

---

## **Acknowledgments**

- **Streamlit** for providing an intuitive platform for building interactive web apps.
- **Faker** for generating realistic synthetic datasets.
- **SQLite** for lightweight and efficient database management.

---

## Contributors

Moulya26 (Repository Owner)

Feel free to contribute or report issues on [GitHub](https://github.com/Moulya26/Zomato-Data-Insights.git).

--- 

Let me know if you need further refinements!
