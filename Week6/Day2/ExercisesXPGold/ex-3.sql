-- Exercise 3 : Items And Customers
-- Instructions
-- We will work on the public database that we created yesterday.
-- Part I
-- Create a table named purchases. It should have 3 columns :
-- id : the primary key of the table
-- customer_id : this column references the table customers
-- item_id : this column references the table items
-- quantity_purchased : this column is the quantity of items purchased by a certain customer
-- Insert purchases for the customers, use subqueries:
-- Scott Scott bought one fan
-- Melanie Johnson bought ten large desks
-- Greg Jones bougth two small desks
-- The table purchases should look like this:
-- id	customer_id	item_id	quantity_purchased
-- 1	3	3	1
-- 2	5	2	10
-- 3	1	1	2
-- Here is the explanation of the first row:
-- id = 1, this is the auto-incrementing primary key
-- customer_id = 3, because the id of Scott Scott in the customers table is 3
-- item_id = 3, because the id of a fan in the items table is 3
-- quantity_purchased = 1, because Scott Scott bought one fan
-- Part II
-- Use SQL to get the following from the database:
-- All purchases. Is this information useful to us?
-- All purchases, joining with the customers table.
-- Purchases of the customer with the ID equal to 5.
-- Purchases for a large desk AND a small desk
-- Use SQL to show all the customers who have made a purchase. Show the following fields/columns:
-- Customer first name
-- Customer last name
-- Item name









-- create table purchases(
-- id serial primary key,
-- customer_id int, foreign key (customer_id) references customers(customer_id),
-- item_id int, foreign key (item_id) references items(item_id),
-- quantity_purchased int
-- )

-- INSERT INTO purchases (customer_id, item_id) 
-- SELECT customers.customer_id, items.item_id 
-- FROM customers, items 
-- WHERE customers.customers_first_name='Scott' and customers.customers_last_name='Scott'
-- AND items.item_name='Fan';

-- INSERT INTO purchases (customer_id, item_id) 
-- SELECT customers.customer_id, items.item_id 
-- FROM customers, items 
-- WHERE customers.customers_first_name='Melanie' and customers.customers_last_name='Johnson'
-- AND items.item_name='Large desk';

-- INSERT INTO purchases (customer_id, item_id) 
-- SELECT customers.customer_id, items.item_id 
-- FROM customers, items 
-- WHERE customers.customers_first_name='Greg' and customers.customers_last_name='Jones'
-- AND items.item_name='Small Desk';

-- update purchases set quantity_purchased = 1
-- where id = 1;

-- update purchases set quantity_purchased = 10
-- where id = 2;

-- update purchases set quantity_purchased = 2
-- where id = 3;



-- 1.1
-- select items.item_name , quantity_purchased
-- from items, purchases
-- where items.item_id = purchases.item_id 

-- 1.2
-- select * from purchases

-- 1.3
-- select items.item_name, customer_id, quantity_purchased
-- from purchases
-- inner join items
-- on items.item_id = purchases.item_id 
-- where customer_id = 5

-- 1.4
-- select items.item_name, quantity_purchased
-- from purchases
-- inner join items
-- on items.item_id = purchases.item_id 
-- where items.item_name in ('Small Desk', 'Large desk')

-- 2
-- select items.item_name, quantity_purchased, customers.customers_first_name, customers.customers_last_name
-- from purchases
-- inner join customers
-- on customers.customer_id = purchases.customer_id 
-- inner join items
-- on items.item_id = purchases.item_id 




