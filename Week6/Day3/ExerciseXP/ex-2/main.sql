-- 🌟 Exercise 2 : DVD Rental
-- Instructions
-- Use UPDATE to change the language of some films. Make sure that you use valid languages.
-- Which foreign keys (references) are defined for the customer table? How does this affect the way in which we INSERT into the customer table?
-- We created a new table called customer_review. Drop this table. Is this an easy step, or does it need extra checking?
-- Find out how many rentals are still outstanding (ie. have not been returned to the store yet).
-- Find the 30 most expensive movies which are outstanding (ie. have not been returned to the store yet)
-- Your friend is at the store, and decides to rent a movie. He knows he wants to see 4 movies, but he can’t remember their names. Can you help him find which movies he wants to rent?
-- The 1st film : The film is about a sumo wrestler, and one of the actors is Penelope Monroe.
-- The 2nd film : A short documentary (less than 1 hour long), rated “R”.
-- The 3rd film : A film that his friend Matthew Mahan rented. He paid over $4.00 for the rental, and he returned it between the 28th of July and the 1st of August, 2005.
-- The 4th film : His friend Matthew Mahan watched this film, as well. It had the word “boat” in the title or description, and it looked like it was a very expensive DVD to replace.








-- 1
-- update language
-- set language.name = 'French'
-- from language
-- inner join film as f
-- on language.language_id = f.language_id
-- where f.title = 'Alone Trip'

-- 2

-- 3
-- drop table customer_review

-- 4 
-- select sum(case when return_date is null then 1 else 0 end) count_nulls
-- from rental;

-- 5
-- select f.title, f.rental_rate
-- from film as f
-- inner join inventory as i
-- on f.film_id = i.film_id
-- inner join rental as r
-- on i.inventory_id = r.inventory_id
-- where return_date is null
--  order by f.rental_rate desc limit 30

-- -- 6.1
-- select f.title, f.description, a.first_name, a.last_name
-- from film as f
-- inner join film_actor as fa
-- on f.film_id = fa.film_id
-- inner join actor as a
-- on fa.actor_id = a.actor_id
-- where (a.first_name = 'Penelope' and a.last_name = 'Monroe')
-- and f.description like '%Sumo%' and f.description like  '%Wrestler%'

-- 6.2
-- select f.title, c.name, f.rating, f.length
-- from film as f
-- inner join film_category as fc
-- on f.film_id = fc.film_id
-- inner join category as c
-- on fc.category_id = c.category_id
-- where f.length < 60 and f.rating = 'R' and c.name = 'Documentary'

-- 6.3
-- select f.title, f.rental_rate, r.return_date, c.first_name, c.last_name
-- from film as f
-- inner join inventory as i
-- on f.film_id = i.film_id
-- inner join rental as r
-- on i.inventory_id = r.inventory_id
-- inner join customer as c
-- on c.customer_id = r.customer_id
-- where c.first_name = 'Matthew' and c.last_name = 'Mahan'
-- and f.rental_rate > 4
-- and r.return_date between '2005-07-28' and '2005-08-01'

-- 6.4
-- select f.title, f.rental_rate, r.return_date, c.first_name, c.last_name
-- from film as f
-- inner join inventory as i
-- on f.film_id = i.film_id
-- inner join rental as r
-- on i.inventory_id = r.inventory_id
-- inner join customer as c
-- on c.customer_id = r.customer_id
-- where c.first_name = 'Matthew' and c.last_name = 'Mahan'
-- and f.description like '%Boat%' or f.title like '%Boat%'
-- order by rental_rate desc limit 1




