# Example SQL Queries for Data Insights

# Top customers by total orders
TOP_CUSTOMERS = """
SELECT name, total_orders, average_rating
FROM customers
ORDER BY total_orders DESC
LIMIT 10;
"""

# Most popular restaurants
MOST_POPULAR_RESTAURANTS = """
SELECT name, total_orders, rating
FROM restaurants
ORDER BY total_orders DESC
LIMIT 10;
"""

# Average delivery time for each restaurant
AVERAGE_DELIVERY_TIME = """
SELECT r.name, AVG(d.delivery_time) AS avg_delivery_time
FROM restaurants r
JOIN orders o ON r.restaurant_id = o.restaurant_id
JOIN deliveries d ON o.order_id = d.order_id
GROUP BY r.name
ORDER BY avg_delivery_time ASC;
"""

# Peak ordering times
PEAK_ORDER_TIMES = """
SELECT strftime('%H', order_date) AS hour, COUNT(*) AS order_count
FROM orders
GROUP BY hour
ORDER BY order_count DESC;
"""

# Orders with delayed deliveries
DELAYED_DELIVERIES = """
SELECT o.order_id, c.name AS customer_name, r.name AS restaurant_name, d.estimated_time, d.delivery_time
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
JOIN restaurants r ON o.restaurant_id = r.restaurant_id
JOIN deliveries d ON o.order_id = d.order_id
WHERE d.delivery_time > d.estimated_time;
"""

# Delivery personnel performance
DELIVERY_PERSONNEL_PERFORMANCE = """
SELECT dp.name, dp.total_deliveries, dp.average_rating
FROM delivery_persons dp
ORDER BY dp.average_rating DESC
LIMIT 10;
"""

# Insights: Feedback ratings by payment mode
FEEDBACK_BY_PAYMENT_MODE = """
SELECT payment_mode, AVG(feedback_rating) AS avg_rating
FROM orders
GROUP BY payment_mode
ORDER BY avg_rating DESC;
"""

# Function to fetch and execute specific queries
def get_query(query_name):
    queries = {
        "top_customers": TOP_CUSTOMERS,
        "popular_restaurants": MOST_POPULAR_RESTAURANTS,
        "avg_delivery_time": AVERAGE_DELIVERY_TIME,
        "peak_order_times": PEAK_ORDER_TIMES,
        "delayed_deliveries": DELAYED_DELIVERIES,
        "delivery_performance": DELIVERY_PERSONNEL_PERFORMANCE,
        "feedback_by_payment": FEEDBACK_BY_PAYMENT_MODE,
    }
    return queries.get(query_name, "")
