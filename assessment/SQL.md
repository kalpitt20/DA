 # Section A  —  Concept Application

 # SCENARIO-1

<br>You are a data analyst at a food delivery platform. The operations team needs a report showing which restaurant partners earned more than Rs 1,00,000 in total revenue last month — but only for restaurants that received at least 50 orders.

<br>

<b>Query</b>

SELECT 
    restaurant_id,SUM(order_amount) AS total_revenue,COUNT(order_id) AS total_orders
FROM orders
WHERE order_date >= DATE_TRUNC('month', CURRENT_DATE - INTERVAL '1 month')
  AND order_date <  DATE_TRUNC('month', CURRENT_DATE)
  AND order_status = 'completed'
GROUP BY restaurant_id
HAVING SUM(order_amount) > 100000
   AND COUNT(order_id) >= 50
ORDER BY total_revenue DESC;

<br><b>Question:</b> Explain how you would use GROUP BY and HAVING together to produce this report.Why is HAVING more appropriate than WHERE for filtering on aggregated values? What would break in your query if you replaced HAVING with WHERE?

<br><b>Ans:</b>
WHERE filters raw rows first, GROUP BY restaurant_id then collapses those rows into one group per restaurant and computes SUM(order_amount) and COUNT(order_id) for each, and HAVING filters those grouped results down to restaurants meeting both thresholds.

<br>
WHERE only sees one order at a time, before any grouping happens. It has no idea what a restaurant's total revenue is yet, because that total hasn't been added up. SUM() and COUNT() only make sense after grouping, so only HAVING can check them.

<br>
What happens if you use WHERE instead of HAVING? — The query simply won't run. SQL will give you an error like "aggregate functions not allowed in WHERE," because you're asking it to check a total that doesn't exist yet at that stage.

<br>

# SCENARIO-2

<br>You are building a customer insights report for a food delivery app. The marketing team needs a list of every registered customer and their most recent order details — even for customers who have never placed an order.

<br><b>Query</b>
SELECT 
    c.customer_id,c.customer_name,o.order_id,o.order_date,o.order_amount
FROM customers c
LEFT JOIN orders o 
    ON c.customer_id = o.customer_id
    AND o.order_date = (
        SELECT MAX(o2.order_date) 
        FROM orders o2 
        WHERE o2.customer_id = c.customer_id
    );

<br><b>Question</b>
Which type of JOIN would you use to ensure all customers appear in the result,including those with no orders? Justify your choice by comparing it with INNER JOIN, and explain specifically what data would be lost if INNER JOIN were used instead.

<br><b>Ans.</b>

Use LEFT JOIN:it keeps every customer row even when there's no matching row in orders, filling order columns with NULL; INNER JOIN only returns rows that match in both tables, so it wouldn't fit the "even customers with no orders" requirement.

<br>
every customer who has never placed an order would vanish from the result entirely.which is exactly the segment marketing usually wants to target.

<br>

# SCENARIO-3

<br>
You are designing a delivery performance dashboard. The business wants to identify delivery agents whose average delivery time is faster than the overall platform average, without using a temporary table or creating a newview.                                                                                               

<br><b>Query</b>
SELECT 
    delivery_agent_id,
    AVG(delivery_time) AS avg_delivery_time
FROM deliveries
GROUP BY delivery_agent_id
HAVING AVG(delivery_time) < (
    SELECT AVG(delivery_time) FROM deliveries
);

<br><b>Question</b>
Describe how you would write a subquery to find these agents. What type of subquery is most appropriate here — scalar, row, or table — and why? What would happen if you tried to place this subquery in the SELECT clause instead of the WHERE clause?

<br><b>Ans</b>
Scalar subquery is the right type. because it returns exactly one value, so it can be compared directly against each agent's average in HAVING with a simple < operator; a row or table subquery would return multiple values, which doesn't fit a single scalar comparison like this.
<br>

It would just add the overall average as an extra column on every row, not filter anything — you'd get all agents back with the platform average repeated alongside each, and you'd still need a separate HAVING/WHERE comparison to actually exclude the slower agents.

# SCENARIO-4
You are analysing order data for a food delivery company. The product team wants to rank the top 3 highest-revenue restaurants within each city. Two restaurants in Surat have the exact same revenue figure and you must decide how to number them. 

<br>

<br><b>Query</b>
SELECT city, restaurant_name, total_revenue, ranking
FROM (
    SELECT 
        city,restaurant_name,
        SUM(order_amount) AS total_revenue,
        DENSE_RANK() OVER (PARTITION BY city ORDER BY SUM(order_amount) DESC) AS ranking
    FROM orders o
    JOIN restaurants r ON r.restaurant_id = o.restaurant_id
    GROUP BY city, restaurant_name
) ranked
WHERE ranking <= 3
ORDER BY city, ranking;

<br><b>Question</b>
Question: Compare RANK() and DENSE_RANK() window functions for this use case. Which would you choose and why? Provide a brief example showing how each function would number three restaurants where two share the same revenue, and explain the practical impact of that difference on the product team's report

<br><b>Ans</b>

Choose DENSE_RANK() — RANK() skips the next number after a tie (1,1,3), while DENSE_RANK() keeps positions consecutive (1,1,2); for a "top 3" report, RANK() can silently push a genuinely-3rd-place restaurant out past the cutoff just because two others tied above it, which isn't what the product team wants.

<br>
With RANK(), restaurant 3 above would be excluded from a "top 3" filter (rank <= 3 still includes it here, but a 3-way tie at #1 would push 3 to rank 4 and drop it); with DENSE_RANK(), C is correctly shown as the 2nd-highest distinct revenue tier, though it means a tie right at the boundary can return more than 3 rows for a city — worth flagging to the product team as expected behavior, not a bug.
<br>

# SCENARIO-5

You are writing a CRM query for a food delivery startup. The customer success team wants each customer labelled as 'Platinum', 'Gold', or 'Standard' based on total lifetime spend — above Rs 5,000, between Rs 2,000 and Rs 5,000, and below Rs 2,000 respectively — directly in the query output without creating a new table.

<br>

<br><b>Query</b>
SELECT 
    customer_id,total_spend,
    CASE 
        WHEN total_spend > 5000 THEN 'Platinum'
        WHEN total_spend >= 2000 THEN 'Gold'
        ELSE 'Standard'
    END AS customer_tier
FROM (
    SELECT customer_id, SUM(order_amount) AS total_spend
    FROM orders
    GROUP BY customer_id
);

<br><b>Question</b>

 Question: Explain how you would use CASE WHEN to generate this classification column. If a customer's total spend is exactly Rs 5,000, which tier will they fall into, and how does the order of your WHEN conditions control that outcome?

<br><b>Ans</b>
How CASE WHEN works here: it checks conditions top-to-bottom and stops at the first one that's TRUE, assigning that label; so total_spend > 5000 is checked first (Platinum), then >= 2000 catches everything left that's Gold-range, and ELSE catches the rest as Standard — you don't need an upper bound on the Gold condition since anything above 5000 was already claimed by the first WHEN.

<br>
Exactly Rs 5,000 → Gold: because the first condition uses strict > (not >=), 5000 fails the Platinum check and falls through to total_spend >= 2000, which is TRUE. If you'd written the first condition as >= 5000 instead, the same customer would land in Platinum 
so the boundary tier entirely depends on which operator and which order you pick, not just the numbers themselves.
<br>

# SCENARIO-6
You are optimising a slow-running analytics query for a food delivery platform. The query joins four large tables and applies a GROUP BY across 10 million rows, taking over 30 seconds. A colleague suggests adding an index on the JOIN column used most frequently.
<br>

<br><b>Query</b>
-- Example: index on the most-used JOIN column
CREATE INDEX idx_orders_restaurant_id ON orders(restaurant_id);

<br><b>Question</b>

Question: Explain what a database index does at the engine level and why it would speed up this specific query. Are there scenarios where adding an index could actually hurt performance? What trade-off must you evaluate before indexing every column in a large table

<br><b>Ans</b>

What an index does & why it helps here — an index builds a sorted structure (usually a B-tree) on the column, so the engine can seek matching rows in roughly O(log n) instead of scanning all 10M rows (O(n)) for every JOIN/GROUP BY lookup — this is exactly why indexing the join column speeds up a 4-table join with heavy aggregation.
<br>

Every index adds overhead on INSERT/UPDATE/DELETE and consumes extra disk space, so on write-heavy tables or low-cardinality columns an index can slow things down without meaningfully speeding up reads.so the real trade-off is read speed vs. write speed + storage, and you index selectively not every column.


<br>


# Section B  —  Practical Coding Tasks

# Task 1: Menu & Order Explorer

1.Create a table named food_orders with columns: order_id, customer_name, restaurant_name, item_ordered, quantity, price_per_item, order_date, and city.Insert at least 8 rows spanning at least 3 cities. 
2.Write a query to retrieve all orders placed in the city of 'Mumbai', sorted by price_per_item in descending order. 
3.Write a query to return all distinct restaurant names that have received at least one order. 
4.Write a query to list the top 5 most expensive individual orders using ORDER BY and LIMIT
<br>
<b>Ans:</b>

<br>

CREATE TABLE food_orders (
    order_id INT PRIMARY KEY,
    customer_name VARCHAR(50),
    restaurant_name VARCHAR(50),
    item_ordered VARCHAR(50),
    quantity INT,
    price_per_item DECIMAL(10,2),
    order_date DATE,
    city VARCHAR(30)
);

INSERT INTO food_orders VALUES
(1, 'Rahul Shah',   'Spice Villa',     'Butter Paneer', 2, 250.00, '2026-08-02', 'Ahmedabad'),
(2, 'Priya Mehta',  'Pizza Point',     'Margherita Pizza', 1, 350.00, '2026-08-03', 'Surat'),
(3, 'Amit Verma',   'Spice Villa',     'Paneer Tikka',   3, 180.00, '2026-08-04', 'Rajkot'),
(4, 'Sneha Patel',  'Burger Barn',     'Cheese Burger',  2, 150.00, '2026-08-05', 'Ahmedabad'),
(5, 'Kalpit Thanki',  'Pizza Point',    'Pepperoni Pizza',1, 400.00, '2026-08-06', 'Rajkot'),
(6, 'Neha Sharma',  'Dosa Corner',     'Masala Dosa',    2, 120.00, '2026-08-07', 'Surat'),
(7, 'Vikram Rao',   'Burger Barn',     'Veg Burger',     4, 100.00, '2026-08-08', 'Ahmedabad'),
(8, 'Riya Desai',   'Spice Villa',     'Veg Biryani',1, 300.00, '2026-08-09', 'Rajkot');

<br>
2.

SELECT * FROM food_orders
WHERE city = 'Mumbai'
ORDER BY price_per_item DESC;

<br>

3.

SELECT DISTINCT restaurant_name
FROM food_orders;

<br>

4.

SELECT order_id, customer_name, restaurant_name, item_ordered, price_per_item
FROM food_orders
ORDER BY price_per_item DESC
LIMIT 5;


<br>

# Task 2: Restaurant Revenue Summary

<br>
<b>Questions</b>
<br>

1.Create a table named delivery_orders with columns: order_id, restaurant_name, city,
total_amount, order_status, and order_date. Insert at least 10 rows covering at least 4
different restaurants.

2.Write a query using SUM, COUNT, and AVG to calculate total revenue, total orders, and average
order value per restaurant.

3.Add a HAVING clause to return only restaurants whose total revenue exceeds Rs 5,000.

4.Extend the SELECT list with a CASE WHEN expression that labels each qualifying restaurant as
'High Revenue' if total revenue is above Rs 10,000, or 'Moderate Revenue' otherwise.

<br><b>Ans:</b>

<br>

1
CREATE TABLE delivery_orders (
    order_id INT PRIMARY KEY,
    restaurant_name VARCHAR(50),
    city VARCHAR(30),
    total_amount DECIMAL(10,2),
    order_status VARCHAR(20),
    order_date DATE
);

INSERT INTO delivery_orders VALUES
(1,  'Spice Villa',  'Mumbai',     3000.00, 'completed', '2026-08-01'),
(2,  'Spice Villa',  'Mumbai',     4000.00, 'completed', '2026-08-03'),
(3,  'Spice Villa',  'Delhi',      5000.00, 'completed', '2026-08-05'),
(4,  'Pizza Point',  'Mumbai',     2000.00, 'completed', '2026-08-02'),
(5,  'Pizza Point',  'Delhi',      2500.00, 'completed', '2026-08-04'),
(6,  'Pizza Point',  'Delhi',      1800.00, 'completed', '2026-08-06'),
(7,  'Burger Barn',  'Ahmedabad',  1000.00, 'completed', '2026-08-02'),
(8,  'Burger Barn',  'Ahmedabad',  1500.00, 'completed', '2026-08-07'),
(9,  'Dosa Corner',  'Delhi',      3000.00, 'completed', '2026-08-03'),
(10, 'Dosa Corner',  'Mumbai',     2800.00, 'completed', '2026-08-08');

<br>

2

SELECT 
    restaurant_name,
    SUM(total_amount) AS total_revenue,
    COUNT(order_id)   AS total_orders,
    AVG(total_amount) AS avg_order_value
FROM delivery_orders
GROUP BY restaurant_name
ORDER BY total_revenue DESC;

<br>

3.

SELECT 
    restaurant_name,
    SUM(total_amount) AS total_revenue,
    COUNT(order_id)   AS total_orders,
    AVG(total_amount) AS avg_order_value
FROM delivery_orders
GROUP BY restaurant_name
HAVING SUM(total_amount) > 5000
ORDER BY total_revenue DESC;

<br>

4.

SELECT 
    restaurant_name,
    SUM(total_amount) AS total_revenue,
    COUNT(order_id)   AS total_orders,
    AVG(total_amount) AS avg_order_value,
    CASE 
        WHEN SUM(total_amount) > 10000 THEN 'High Revenue'
        ELSE 'Moderate Revenue'
    END AS revenue_label
FROM delivery_orders
GROUP BY restaurant_name
HAVING SUM(total_amount) > 5000
ORDER BY total_revenue DESC;

# Task 3: Customer–Order–Restaurant Joined Report

<br>

<b>Questions</b>

<br>

1.Create three tables: customers (customer_id, name, city, phone), restaurants (restaurant_id,name, cuisine_type, city), and orders (order_id, customer_id, restaurant_id, amount,order_date). Insert at least 6 rows per table and intentionally include at least 2 customers who have placed no orders.

2.Write an INNER JOIN query to list each order alongside the placing customer's name and the fulfilling restaurant's name.

3.Write a LEFT JOIN query to list all customers — including those with no orders — with NULL appearing in order columns where no order exists.

4.Add a WHERE condition to the joined result to show only orders where both the customer and the restaurant belong to the same city.

<br>

<b>Ans:</b>
-- Table 1: customers 
CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    name VARCHAR(50),
    city VARCHAR(30),
    phone VARCHAR(15)
);

INSERT INTO customers VALUES
(1, 'Rahul Shah',  'Ahmedabad', '9800000001'),
(2, 'Priya Mehta', 'Surat',     '9800000002'),
(3, 'Amit Verma',  'Rajkot',    '9800000003'),
(4, 'Sneha Patel', 'Ahmedabad', '9800000004'),
(5, 'Neha Sharma', 'Surat',     '9800000005'),  
(6, 'Vikram Rao',  'Rajkot',    '9800000006');  

-- Table 2: restaurants
CREATE TABLE restaurants (
    restaurant_id INT PRIMARY KEY,
    name VARCHAR(50),
    cuisine_type VARCHAR(30),
    city VARCHAR(30)
);

INSERT INTO restaurants VALUES
(101, 'Spice Villa',   'North Indian', 'Ahmedabad'),
(102, 'Pizza Point',   'Italian',      'Surat'),
(103, 'Burger Barn',   'Fast Food',    'Rajkot'),
(104, 'Dosa Corner',   'South Indian', 'Surat'),
(105, 'Sushi Zen',     'Japanese',     'Ahmedabad'),
(106, 'Curry House',   'North Indian', 'Rajkot');

-- Table 3: orders
CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    restaurant_id INT,
    amount DECIMAL(10,2),
    order_date DATE
);

INSERT INTO orders VALUES
(1, 1, 101, 500.00, '2026-08-01'),  
(2, 2, 102, 350.00, '2026-08-02'),  
(3, 3, 103, 200.00, '2026-08-03'),
(4, 4, 105, 600.00, '2026-08-04'),
(5, 1, 102, 300.00, '2026-08-05'),  
(6, 2, 106, 450.00, '2026-08-06');  

2.

SELECT o.order_id, c.name AS customer_name, r.name AS restaurant_name, o.amount, o.order_date
FROM orders o
INNER JOIN customers c ON o.customer_id = c.customer_id
INNER JOIN restaurants r ON o.restaurant_id = r.restaurant_id;

3.

SELECT c.customer_id, c.name AS customer_name, o.order_id, r.name AS restaurant_name, o.amount
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id
LEFT JOIN restaurants r ON o.restaurant_id = r.restaurant_id;

4.

SELECT o.order_id, c.name AS customer_name, c.city AS customer_city, r.name AS restaurant_name, r.city AS restaurant_city, o.amount
FROM orders o
INNER JOIN customers c ON o.customer_id = c.customer_id
INNER JOIN restaurants r ON o.restaurant_id = r.restaurant_id
WHERE c.city = r.city;

<br>

# Task 4: Delivery Agent Performance Ranking

<br>

<b>Question</b>

1.Create a table named deliveries with columns: delivery_id, agent_name, restaurant_name, delivery_time_mins, and order_date. Insert at least 10 rows across at least 4 delivery agents, with varied delivery times.

2.Write a CTE named agent_stats that calculates each agent's average delivery time across all their deliveries.

3.Using the CTE result, apply RANK() OVER (ORDER BY avg_delivery_time ASC) to rank agents from fastest to slowest.

4.Add a scalar subquery to compute the overall platform average delivery time, then use CASE WHEN in the final SELECT to label each agent 'On Track' if their average is at or below the platform average, or 'Needs Improvement' if it is above.

<br>

<b>Ans:</b>


1.
CREATE TABLE deliveries (
    delivery_id INT PRIMARY KEY,
    agent_name VARCHAR(50),
    restaurant_name VARCHAR(50),
    delivery_time_mins INT,
    order_date DATE
);

INSERT INTO deliveries VALUES
(1,  'Ravi Kumar',   'Spice Villa',  28, '2026-08-01'),
(2,  'Ravi Kumar',   'Pizza Point',  35, '2026-08-02'),
(3,  'Ravi Kumar',   'Burger Barn',  22, '2026-08-03'),
(4,  'Mihir Joshi',  'Spice Villa',  40, '2026-08-01'),
(5,  'Mihir Joshi',  'Dosa Corner',  30, '2026-08-04'),
(6,  'Mihir Joshi',  'Pizza Point',  45, '2026-08-05'),
(7,  'Suresh Nair',  'Burger Barn',  18, '2026-08-02'),
(8,  'Suresh Nair',  'Dosa Corner',  25, '2026-08-06'),
(9,  'Anil Rathod','Spice Villa',  50, '2026-08-03'),
(10, 'Anil Rathod','Pizza Point',  33, '2026-08-07');

2.

WITH agent_stats AS (
    SELECT 
        agent_name,
        AVG(delivery_time_mins) AS avg_delivery_time
    FROM deliveries
    GROUP BY agent_name
)
SELECT * FROM agent_stats;

3.

WITH agent_stats AS (
    SELECT 
        agent_name,
        AVG(delivery_time_mins) AS avg_delivery_time
    FROM deliveries
    GROUP BY agent_name
)
SELECT 
    agent_name,
    avg_delivery_time,
    RANK() OVER (ORDER BY avg_delivery_time ASC) AS speed_rank
FROM agent_stats;

4.

WITH agent_stats AS (
    SELECT 
        agent_name,
        AVG(delivery_time_mins) AS avg_delivery_time
    FROM deliveries
    GROUP BY agent_name
)
SELECT 
    agent_name,
    avg_delivery_time,
    RANK() OVER (ORDER BY avg_delivery_time ASC) AS speed_rank,
    CASE 
        WHEN avg_delivery_time <= (SELECT AVG(delivery_time_mins) FROM deliveries) THEN 'On Track'
        ELSE 'Needs Improvement'
    END AS performance_label
FROM agent_stats;

<br>

# <b> Section C  —  Mini Capstone Project </b>

<br>

<b>Mini Project:  Food Delivery Analytics — SQL Backend</b>

1.Design a schema with at least four related tables: customers, restaurants, orders, and delivery_agents. Define appropriate PRIMARY KEY and FOREIGN KEY constraints and insert at least 10 rows per table with realistic food delivery data across at least 3 cities.

2.Write a revenue report query using GROUP BY, HAVING, and aggregate functions (SUM, COUNT, AVG) that returns total orders and total revenue per restaurant, filtered to include only restaurants with more than 3 orders.

3.Write a customer segmentation query using CASE WHEN to classify each customer as 'Platinum' (spend above Rs 5,000), 'Gold' (Rs 2,000–Rs 5,000), or 'Standard' (below Rs 2,000) based on their total spend, ordered from highest to lowest spender.

4.Write a window function query using DENSE_RANK() OVER (PARTITION BY city ORDER BY total_revenue DESC) to identify the top 3 performing restaurants in each city, and a separate query using ROW_NUMBER() to find each customer's single most recent order.

5.Create a SQL VIEW named vw_daily_order_summary that JOINs all four tables and returns:order_date, customer_name, restaurant_name, agent_name, order_amount, and delivery_time_mins. Query the view to display only orders placed in the last 7 days.


<br>

<b>Ans</b>

-- Table 1: customers
CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    name VARCHAR(50),
    city VARCHAR(30),
    phone VARCHAR(15)
);

INSERT INTO customers VALUES
(1,  'Rahul Shah',    'Ahmedabad', '9800000001'),
(2,  'Priya Mehta',   'Surat',     '9800000002'),
(3,  'Amit Verma',    'Rajkot',    '9800000003'),
(4,  'Sneha Patel',   'Ahmedabad', '9800000004'),
(5,  'Neha Sharma',   'Surat',     '9800000005'),
(6,  'Vikram Rao',    'Rajkot',    '9800000006'),
(7,  'Kalpit Thanki',  'Ahmedabad', '9800000007'),
(8,  'Riya Desai',    'Surat',     '9800000008'),
(9,  'Manish Joshi',  'Rajkot',    '9800000009'),
(10, 'Pooja Bhatt',   'Ahmedabad', '9800000010');

-- Table 2: restaurants
CREATE TABLE restaurants (
    restaurant_id INT PRIMARY KEY,
    name VARCHAR(50),
    cuisine_type VARCHAR(30),
    city VARCHAR(30)
);

INSERT INTO restaurants VALUES
(101, 'Spice Villa',  'North Indian', 'Ahmedabad'),
(102, 'Pizza Point',  'Italian',      'Surat'),
(103, 'Burger Barn',  'Fast Food',    'Rajkot'),
(104, 'Dosa Corner',  'South Indian', 'Surat'),
(105, 'Sushi Zen',    'Japanese',     'Ahmedabad'),
(106, 'Curry House',  'North Indian', 'Rajkot'),
(107, 'Taco Town',    'Mexican',      'Ahmedabad'),
(108, 'Noodle Bar',   'Chinese',      'Surat'),
(109, 'Grill Master', 'BBQ',          'Rajkot'),
(110, 'Sweet Treats', 'Desserts',     'Ahmedabad');

-- Table 3: delivery_agents
CREATE TABLE delivery_agents (
    agent_id INT PRIMARY KEY,
    agent_name VARCHAR(50),
    city VARCHAR(30),
    phone VARCHAR(15)
);

INSERT INTO delivery_agents VALUES
(201, 'Ravi Kumar',    'Ahmedabad', '9700000001'),
(202, 'Meera Joshi',   'Surat',     '9700000002'),
(203, 'Suresh Nair',   'Rajkot',    '9700000003'),
(204, 'Anjali Rathod', 'Ahmedabad', '9700000004'),
(205, 'Dev Patel',     'Surat',     '9700000005'),
(206, 'Kiran Solanki', 'Rajkot',    '9700000006'),
(207, 'Farhan Sheikh', 'Ahmedabad', '9700000007'),
(208, 'Nisha Trivedi', 'Surat',     '9700000008'),
(209, 'Om Prajapati',  'Rajkot',    '9700000009'),
(210, 'Zara Khan',     'Ahmedabad', '9700000010');

-- Table 4: orders 
CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    restaurant_id INT,
    agent_id INT,
    amount DECIMAL(10,2),
    delivery_time_mins INT,
    order_date DATE,
    order_status VARCHAR(20),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (restaurant_id) REFERENCES restaurants(restaurant_id),
    FOREIGN KEY (agent_id) REFERENCES delivery_agents(agent_id)
);

INSERT INTO orders VALUES
(1,  1, 101, 201, 500.00, 28, '2026-08-01', 'completed'),
(2,  2, 102, 202, 350.00, 35, '2026-08-02', 'completed'),
(3,  3, 103, 203, 200.00, 22, '2026-08-03', 'completed'),
(4,  4, 105, 204, 600.00, 40, '2026-08-04', 'completed'),
(5,  1, 102, 205, 300.00, 30, '2026-08-05', 'completed'),
(6,  2, 106, 206, 450.00, 33, '2026-08-06', 'completed'),
(7,  7, 107, 207, 700.00, 25, '2026-08-07', 'completed'),
(8,  8, 108, 208, 280.00, 45, '2026-08-08', 'completed'),
(9,  9, 109, 209, 550.00, 18, '2026-08-09', 'completed'),
(10, 10,110, 210, 150.00, 20, '2026-08-10', 'completed'),
(11, 3, 101, 201, 320.00, 27, '2026-08-11', 'cancelled'),
(12, 4, 104, 202, 260.00, 38, '2026-08-12', 'completed');

2.

SELECT 
    r.restaurant_id,
    r.name AS restaurant_name,
    COUNT(o.order_id) AS total_orders,
    SUM(o.amount)      AS total_revenue,
    AVG(o.amount)      AS avg_order_value
FROM orders o
JOIN restaurants r ON r.restaurant_id = o.restaurant_id
GROUP BY r.restaurant_id, r.name
HAVING COUNT(o.order_id) > 3
ORDER BY total_revenue DESC;

3.

SELECT 
    c.customer_id,
    c.name AS customer_name,
    COALESCE(SUM(o.amount), 0) AS total_spend,
    CASE 
        WHEN COALESCE(SUM(o.amount), 0) > 5000 THEN 'Platinum'
        WHEN COALESCE(SUM(o.amount), 0) >= 2000 THEN 'Gold'
        ELSE 'Standard'
    END AS customer_tier
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id AND o.order_status = 'completed'
GROUP BY c.customer_id, c.name
ORDER BY total_spend DESC;


4.

-- Top 3 restaurants per city by revenue
WITH restaurant_revenue AS (
    SELECT 
        r.restaurant_id,
        r.name AS restaurant_name,
        r.city,
        SUM(o.amount) AS total_revenue
    FROM orders o
    JOIN restaurants r ON r.restaurant_id = o.restaurant_id
    GROUP BY r.restaurant_id, r.name, r.city
),
ranked AS (
    SELECT *,
        DENSE_RANK() OVER (PARTITION BY city ORDER BY total_revenue DESC) AS city_rank
    FROM restaurant_revenue
)
SELECT * FROM ranked WHERE city_rank <= 3
ORDER BY city, city_rank;

-- Each customer's most recent order
WITH ranked_orders AS (
    SELECT 
        o.*,
        ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY order_date DESC) AS rn
    FROM orders o
)
SELECT customer_id, order_id, order_date, amount
FROM ranked_orders
WHERE rn = 1
ORDER BY customer_id;

5.

CREATE VIEW vw_daily_order_summary AS
SELECT 
    o.order_date,
    c.name AS customer_name,
    r.name AS restaurant_name,
    a.agent_name,
    o.amount AS order_amount,
    o.delivery_time_mins
FROM orders o
JOIN customers c ON c.customer_id = o.customer_id
JOIN restaurants r ON r.restaurant_id = o.restaurant_id
JOIN delivery_agents a ON a.agent_id = o.agent_id;

-- Query the view for last 7 days
SELECT *
FROM vw_daily_order_summary
WHERE order_date >= CURRENT_DATE - INTERVAL '7 days'
ORDER BY order_date DESC;

<br>

# <b> Section D  —  AI-Augmented Learning </b>

<br>

<b>Question</b>

1.Finds the top 3 delivery agents per city for a food delivery platform, ranked by number of completed orders, using window functions.

2.Includes a column showing each agent's average delivery time alongside their rank.

3.Filters the result to include only agents who have completed more than 5 orders in that city.

4.Returns the final output sorted by city name alphabetically, then by rank ascending.

<br>
<b>Ans</b>

# 1
1. Prompt given to the AI tool

Write a SQL query that finds the top 3 delivery agents per city for a food delivery platform, ranked by number of completed orders, using window functions. My tables are orders (order_id, customer_id, restaurant_id, agent_id, amount, delivery_time_mins, order_date, order_status) and delivery_agents (agent_id, agent_name, city, phone).

2. AI query

SELECT 
    a.agent_name,
    a.city,
    COUNT(o.order_id) AS completed_orders,
    RANK() OVER (ORDER BY COUNT(o.order_id) DESC) AS city_rank
FROM orders o
JOIN delivery_agents a ON a.agent_id = o.agent_id
GROUP BY a.agent_name, a.city
HAVING city_rank <= 3;

3. My Query

WITH agent_city_stats AS (
    SELECT 
        a.agent_id,
        a.agent_name,
        a.city,
        COUNT(o.order_id) AS completed_orders
    FROM orders o
    JOIN delivery_agents a ON a.agent_id = o.agent_id
    WHERE o.order_status = 'completed'
    GROUP BY a.agent_id, a.agent_name, a.city
),
ranked_agents AS (
    SELECT *,
        RANK() OVER (PARTITION BY city ORDER BY completed_orders DESC) AS city_rank
    FROM agent_city_stats
)
SELECT city, agent_name, completed_orders, city_rank
FROM ranked_agents
WHERE city_rank <= 3
ORDER BY city ASC, city_rank ASC;

4. Ans

The AI's query had two bugs: it missed PARTITION BY city in the RANK() window function, so it ranked agents globally instead of per city; and it tried filtering on city_rank in HAVING, which errors since window functions aren't allowed there. I fixed both by moving the ranking into a CTE with PARTITION BY city, filtering WHERE city_rank <= 3 in the outer query, and added WHERE o.order_status = 'completed' so only completed orders count.

<br>

# 2

1. Prompt given to the AI tool 

Includes a column showing each agent's average delivery time alongside their rank.
Same with this query.


2. AI query

WITH agent_city_stats AS (
    SELECT 
        a.agent_name,
        a.city,
        COUNT(o.order_id) AS completed_orders,
        AVG(o.delivery_time_mins) AS avg_delivery_time
    FROM orders o
    JOIN delivery_agents a ON a.agent_id = o.agent_id
    GROUP BY a.agent_name, a.city
),
ranked_agents AS (
    SELECT *,
        RANK() OVER (PARTITION BY city ORDER BY completed_orders DESC) AS city_rank
    FROM agent_city_stats
)
SELECT city, agent_name, completed_orders, avg_delivery_time, city_rank
FROM ranked_agents
WHERE city_rank <= 3;

3. My query

WITH agent_city_stats AS (
    SELECT 
        a.agent_id,
        a.agent_name,
        a.city,
        COUNT(o.order_id) AS completed_orders,
        AVG(o.delivery_time_mins) AS avg_delivery_time
    FROM orders o
    JOIN delivery_agents a ON a.agent_id = o.agent_id
    WHERE o.order_status = 'completed'
      AND o.delivery_time_mins IS NOT NULL
    GROUP BY a.agent_id, a.agent_name, a.city
),
ranked_agents AS (
    SELECT *,
        RANK() OVER (PARTITION BY city ORDER BY completed_orders DESC) AS city_rank
    FROM agent_city_stats
)
SELECT city, agent_name, completed_orders, avg_delivery_time, city_rank
FROM ranked_agents
WHERE city_rank <= 3
ORDER BY city ASC, city_rank ASC;

4. Ans.

The AI's version didn't filter by order_status = 'completed', so cancelled orders with possibly NULL delivery times could pollute both the order count and the AVG() calculation. It also grouped by agent_name alone instead of agent_id, risking merged rows if two agents share a name. I added the status/NULL filter before aggregation and grouped by agent_id for accuracy, plus an explicit ORDER BY for consistent output.

<br>

# 3


1. Prompt given to the AI tool

same with this query 
3.Filters the result to include only agents who have completed more than 5 orders in that city.

2. AI query

WITH agent_city_stats AS (
    SELECT 
        a.agent_id,
        a.agent_name,
        a.city,
        COUNT(o.order_id) AS completed_orders,
        AVG(o.delivery_time_mins) AS avg_delivery_time
    FROM orders o
    JOIN delivery_agents a ON a.agent_id = o.agent_id
    WHERE o.order_status = 'completed'
    GROUP BY a.agent_id, a.agent_name, a.city
),
ranked_agents AS (
    SELECT *,
        RANK() OVER (PARTITION BY city ORDER BY completed_orders DESC) AS city_rank
    FROM agent_city_stats
)
SELECT city, agent_name, completed_orders, avg_delivery_time, city_rank
FROM ranked_agents
WHERE city_rank <= 3 AND completed_orders > 5;

3. My Query

WITH agent_city_stats AS (
    SELECT 
        a.agent_id,
        a.agent_name,
        a.city,
        COUNT(o.order_id) AS completed_orders,
        AVG(o.delivery_time_mins) AS avg_delivery_time
    FROM orders o
    JOIN delivery_agents a ON a.agent_id = o.agent_id
    WHERE o.order_status = 'completed'
      AND o.delivery_time_mins IS NOT NULL
    GROUP BY a.agent_id, a.agent_name, a.city
    HAVING COUNT(o.order_id) > 5
),
ranked_agents AS (
    SELECT *,
        RANK() OVER (PARTITION BY city ORDER BY completed_orders DESC) AS city_rank
    FROM agent_city_stats
)
SELECT city, agent_name, completed_orders, avg_delivery_time, city_rank
FROM ranked_agents
WHERE city_rank <= 3
ORDER BY city ASC, city_rank ASC;

4. Ans.

The AI applied completed_orders > 5 after ranking, in the same WHERE as city_rank <= 3 — this ranks agents first, then filters, so an agent with only 3 orders could still occupy rank 1 in a small city and get counted before being dropped, distorting who "rank 2" or "rank 3" really is. I moved the > 5 condition into HAVING inside the CTE, so only already-qualified agents (5+ completed orders) enter the ranking step at all — filter-before-rank, not rank-then-filter.

<br>

# 4

1. Prompt given to the AI tool
Returns the final output sorted by city name alphabetically, then by rank ascending. same with this query.

2. AI query

WITH agent_city_stats AS (
    SELECT 
        a.agent_id,
        a.agent_name,
        a.city,
        COUNT(o.order_id) AS completed_orders,
        AVG(o.delivery_time_mins) AS avg_delivery_time
    FROM orders o
    JOIN delivery_agents a ON a.agent_id = o.agent_id
    WHERE o.order_status = 'completed'
    GROUP BY a.agent_id, a.agent_name, a.city
    HAVING COUNT(o.order_id) > 5
),
ranked_agents AS (
    SELECT *,
        RANK() OVER (PARTITION BY city ORDER BY completed_orders DESC) AS city_rank
    FROM agent_city_stats
)
SELECT city, agent_name, completed_orders, avg_delivery_time, city_rank
FROM ranked_agents
WHERE city_rank <= 3
ORDER BY completed_orders DESC;

3. My query

WITH agent_city_stats AS (
    SELECT 
        a.agent_id,
        a.agent_name,
        a.city,
        COUNT(o.order_id) AS completed_orders,
        AVG(o.delivery_time_mins) AS avg_delivery_time
    FROM orders o
    JOIN delivery_agents a ON a.agent_id = o.agent_id
    WHERE o.order_status = 'completed'
      AND o.delivery_time_mins IS NOT NULL
    GROUP BY a.agent_id, a.agent_name, a.city
    HAVING COUNT(o.order_id) > 5
),
ranked_agents AS (
    SELECT *,
        RANK() OVER (PARTITION BY city ORDER BY completed_orders DESC) AS city_rank
    FROM agent_city_stats
)
SELECT city, agent_name, completed_orders, avg_delivery_time, city_rank
FROM ranked_agents
WHERE city_rank <= 3
ORDER BY city ASC, city_rank ASC;

4. Ans.

The AI sorted by completed_orders DESC instead of the requested city, then rank order, so results from different cities got interleaved by order count rather than grouped together alphabetically by city. I fixed the ORDER BY clause to city ASC, city_rank ASC so all of one city's top-3 agents appear together, in rank order, before moving to the next city alphabetically.