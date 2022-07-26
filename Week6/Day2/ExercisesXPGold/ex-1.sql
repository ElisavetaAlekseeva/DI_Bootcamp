-- Exercise 1: DVD Rental
-- Instructions
-- You were hired to babysit your cousin and you want to find a few movies that he can watch with you.
-- Find out how many films there are for each rating.
-- Get a list of all the movies that have a rating of G or PG-13.
-- Filter this list further: look for only movies that are under 2 hours long, and whose rental price (rental_rate) is under 3.00. Sort the list alphabetically.
-- Find a customer in the customer table, and change his/her details to your details, using SQL UPDATE.
-- Now find the customer’s address, and use UPDATE to change the address to your address (or make one up).







-- 1
-- select count(film_id),rating from film group by rating

-- 2
-- select title from film where rating = 'G' or rating = 'PG'

-- 2.1 
-- select title, length, rental_rate from film where rental_rate < 3.00  and length < 200 and (rating = 'G'or rating = 'PG') order by title asc


-- 3

-- update customer
-- set first_name = 'Lisa', last_name ='Alex', email = 'LisaAl@gamil.com'
-- where customer_id = 1

-- 4

-- update address
-- set address = 'Bezalel 4'
-- where address_id = (select address_id from customer where customer_id = 1)

