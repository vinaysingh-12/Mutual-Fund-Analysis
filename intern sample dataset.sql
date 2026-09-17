CREATE TABLE sales (
    Order_ID INT PRIMARY KEY,
    Order_Date DATE,
    Customer_Name VARCHAR(50),
    Product VARCHAR(50),
    Category VARCHAR(50),
    Region VARCHAR(50),
    Quantity INT,
    Unit_Price DECIMAL(10, 2)
);

INSERT INTO sales (Order_ID, Order_Date, Customer_Name, Product, Category, Region, Quantity, Unit_Price) VALUES
(1001, '2023-10-01', 'Alice Smith', 'Laptop', 'Electronics', 'North', 1, 1200.00),
(1002, '2023-10-02', 'Bob Jones', 'Desk Chair', 'Furniture', 'South', 2, 150.00),
(1003, '2023-10-02', 'Charlie Brown', 'Mouse', 'Electronics', 'North', 3, 25.00),
(1004, '2023-10-03', 'Diana Prince', 'Coffee Maker', 'Appliances', 'East', 1, 85.00),
(1005, '2023-10-04', 'Evan Wright', 'Laptop', 'Electronics', 'West', 2, 1200.00),
(1006, '2023-10-05', 'Fiona Gallagher', 'Desk Chair', 'Furniture', 'North', 1, 150.00),
(1007, '2023-10-06', 'George Costanza', 'Blender', 'Appliances', 'South', 1, 60.00),
(1008, '2023-10-07', 'Hannah Abbott', 'Mouse', 'Electronics', 'West', 5, 25.00),
(1009, '2023-10-08', 'Ian Malcolm', 'Monitor', 'Electronics', 'East', 2, 300.00),
(1010, '2023-10-09', 'Jane Doe', 'Desk Chair', 'Furniture', 'West', 4, 150.00);