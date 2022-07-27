--  Exercise 1: DVD Rental
-- Instructions
-- Get a list of all film languages.
-- Get a list of all films joined with their languages – select the following details : film title, description, and language name. Try your query with different joins:
-- Get all films, even if they don’t have languages.
-- Get all languages, even if there are no films in those languages.
-- Create a new table called new_film with the following columns : id, name. Add some new films to the table.
-- Create a new table called customer_review, which will contain film reviews that customers will make.
-- Think about the DELETE constraint: if a film is deleted, it’s review should be automatically deleted.
-- It should have the following columns:
-- review_id – a primary key, non null, auto-increment.
-- film_id – references the new_film table. The film that is being reviewed.
-- language_id – references the language table. What language the review is in.
-- title – the title of the review.
-- score – the rating of the review (1-10).
-- review_text – the text of the review. No limit on the length.
-- last_update – when the review was last updated.
-- Add 2 movie reviews. Make sure you link them to valid objects in the other tables.
-- Delete a film that has a review from the new_film table, what happens to the customer_review table?







-- 1
-- select name from language

-- 2
-- select f.title, f.description, l.name 
-- from film as f
-- right join language as l
-- -- left join language as l
-- on l.language_id = f.language_id

-- 3
-- create table new_film(
-- 	id serial primary key,
-- 	name varchar (100) not null
-- )
-- insert into new_film
-- values
-- (default, 'new film 1'),
-- (default, 'new film 2'),
-- (default, 'new film 3')

-- -- 4
-- create table customer_review(
-- 	review_id serial primary key,
-- 	film_id int not null,
-- 	language_id int not null,
-- 	title varchar (200) not null,
-- 	score int not null,
-- 	review_text varchar (65535) not null,
-- 	last_update date not null,
-- 	FOREIGN KEY (film_id) REFERENCES new_film(id) ON DELETE CASCADE ON UPDATE CASCADE,
-- 	FOREIGN KEY (language_id) REFERENCES language(language_id) ON DELETE CASCADE ON UPDATE CASCADE
-- )

-- 5
-- insert into customer_review
-- values
-- (	default, 
-- 	(select id from new_film where name = 'new film 2'),
--  	(select language_id from language where name ='English'),
--  	'Not Bad',
-- 	4, 
-- 	'bla bla bla bla bla bla bla',
--  	'01.01.2001'
-- ),
-- (	default, 
-- 	(select id from new_film where name = 'new film 1'),
--  	(select language_id from language where name ='English'),
--  	'Bad',
-- 	1, 
-- 	'bla bla bla bla bla bla la bla bla bla bla bla la bla bla bla bla bla la bla bla bla bla bla la bla bla bla bla bla la bla bla bla bla bla bla',
--  	'04.04.2004'
-- )

-- 6
-- delete from new_film
-- where name = 'new film 1'



























