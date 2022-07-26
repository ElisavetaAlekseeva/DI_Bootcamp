-- Exercise 1 : Items And Customers

-- Instructions

-- We will work on the public database that we created yesterday.

-- Use SQL to get the following from the database:
-- All items, ordered by price (lowest to highest).
-- Items with a price above 80 (80 included), ordered by price (highest to lowest).
-- The first 3 customers in alphabetical order of the first name (A-Z) – exclude the primary key column from the results.
-- All last names (no other columns!), in reverse alphabetical order (Z-A)--  item_id serial primary key,







-- create table items(
--  item_name varchar (10) not null,
--  price decimal not null
-- );

-- create table customers(
-- customer_id serial primary key,
-- customers_first_name varchar(10) not null,
-- customers_last_name varchar(10) not null);

-- insert into items(item_name, price)
-- values
-- ('Small Desk', 100),
-- ('Large desk', 300),
-- ('Fan', 80);

-- insert into customers(customers_first_name, customers_last_name)
-- values
-- ('Greg', 'Jones'),
-- ('Sandra', 'Jones'),
-- ('Scott', 'Scott'),
-- ('Trevor', 'Green'),
-- ('Melanie', 'Johnson');


-- 1
-- select * from items order by price asc
-- 2
-- select * from items where price >= 80 order by price desc
-- 3
-- alter table customers drop column customer_id
-- select * from customers order by customers_first_name asc limit 3
-- 4
-- select customers_last_name from customers order by customers_last_name desc



