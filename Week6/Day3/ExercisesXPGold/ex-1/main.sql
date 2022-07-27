
-- Exercise 1 : DVD Rentals
-- Instructions
-- Get a list of all rentals which are out (have not been returned). How do we identify these films in the database?
-- Get a list of all customers who have not returned their rentals. Make sure to group your results.
-- Get a list of all the Action films with Joe Swank.
-- Before you start, could there be a shortcut to getting this information? Maybe a view?



-- 1
-- select f.title, r.return_date
-- from film as f
-- inner join inventory as i
-- on f.film_id = i.film_id
-- inner join rental as r
-- on i.inventory_id = r.inventory_id
-- where return_date is null

-- 2
-- select c.first_name, c.last_name
-- from film as f
-- inner join inventory as i
-- on f.film_id = i.film_id
-- inner join rental as r
-- on i.inventory_id = r.inventory_id
-- inner join customer as c
-- on r.customer_id = c.customer_id
-- where return_date is null
-- group by c.first_name, c.last_name

-- 3
-- select f.title, f.description, a.first_name, a.last_name
-- from film as f
-- inner join film_actor as fa
-- on f.film_id = fa.film_id
-- inner join actor as a
-- on fa.actor_id = a.actor_id
-- where (a.first_name = 'Joe' and a.last_name = 'Swank')




