-- Exercise 1 : Items And Customers

-- Create a database called public.
-- Add two tables:
-- items
-- customers.


-- Follow the instructions below to determine which columns and data types to add to the two tables:

-- Add the following items to the items table:
-- 1 - Small Desk – 100 (ie. price)
-- 2 - Large desk – 300
-- 3 - Fan – 80

-- Add 5 new customers to the customers table:
-- 1 - Greg - Jones
-- 2 - Sandra - Jones
-- 3 - Scott - Scott
-- 4 - Trevor - Green
-- 5 - Melanie - Johnson

-- Use SQL to fetch the following data from the database:
-- All the items.
-- All the items with a price above 80 (80 not included).
-- All the items with a price below 300. (300 included)
-- All customers whose last name is ‘Smith’ (What will be your outcome?).
-- All customers whose last name is ‘Jones’.
-- All customers whose firstname is not ‘Scott’.




create table items(
 item_id serial primary key,
 item_name varchar (10) not null,
 price decimal not null
);

create table customers(
customer_id serial primary key,
customers_first_name varchar(10) not null,
customers_last_name varchar(10) not null);

insert into items(item_name, price)
values
('Small Desk', 100),
('Large desk', 300),
('Fan', 80);

insert into customers(first_name, last_name)
values
('Greg', 'Jones'),
('Sandra', 'Jones'),
('Scott', 'Scott'),
('Trevor', 'Green'),
('Melanie', 'Johnson');

select * from items;
select * from items where price > 80;
select * from items where price <= 300;
select * from customers where customers_last_name = 'Smith';
select * from customers where customers_last_name = 'Jones';
select * from customers where customers_first_name != 'Scott';
