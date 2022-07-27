-- You are going to practice tables relationships
-- Part I
-- Create 2 tables : Customer and Customer profile. They have a One to One relationship.
-- A customer can have only one profile, and a profile belongs to only one customer
-- The Customer table should have the columns : id, first_name, last_name NOT NULL
-- The Customer profile table should have the columns : id, isLoggedIn DEFAULT false (a Boolean), customer_id (a reference to the Customer table)
-- Insert those customers
-- John, Doe
-- Jerome, Lalu
-- Lea, Rive
-- Insert those customer profiles, use subqueries
-- John is loggedIn
-- Jerome is not logged in
-- Use the relevant types of Joins to display:
-- The first_name of the LoggedIn customers
-- All the customers first_name and isLoggedIn columns - even the customers those who don’t have a profile.
-- The number of customers that are not LoggedIn
-- Part II
-- Create a table named Book, with the columns : book_id SERIAL PRIMARY KEY, title NOT NULL, author NOT NULL
-- Insert those books :
-- Alice In Wonderland, Lewis Carroll
-- Harry Potter, J.K Rowling
-- To kill a mockingbird, Harper Lee
-- Create a table named Student, with the columns : student_id SERIAL PRIMARY KEY, name NOT NULL UNIQUE, age. Make sure that the age is never bigger than 15 (Find an SQL method);
-- Insert those students:
-- John, 12
-- Lera, 11
-- Patrick, 10
-- Bob, 14
-- Create a table named Library, with the columns :
-- book_fk_id ON DELETE CASCADE ON UPDATE CASCADE
-- student_id ON DELETE CASCADE ON UPDATE CASCADE
-- borrowed_date
-- This table, is a junction table for a Many to Many relationship with the Book and Student tables : A student can borrow many books, and a book can be borrowed by many children
-- book_fk_id is a Foreign Key representing the column book_id from the Book table
-- student_fk_id is a Foreign Key representing the column student_id from the Student table
-- The pair of Foreign Keys is the Primary Key of the Junction Table
-- Add 4 records in the junction table, use subqueries.
-- the student named John, borrowed the book Alice In Wonderland on the 15/02/2022
-- the student named Bob, borrowed the book To kill a mockingbird on the 03/03/2021
-- the student named Lera, borrowed the book Alice In Wonderland on the 23/05/2021
-- the student named Bob, borrowed the book Harry Potter the on 12/08/2021
-- Display the data
-- Select all the columns from the junction table
-- Select the name of the student and the title of the borrowed books
-- Select the average age of the children, that borrowed the book Alice in Wonderland
-- Delete a student from the Student table, what happened in the junction table ?










-- create table customer(
-- 	id serial primary key,
-- 	first_name varchar (20) not null,
-- 	last_name varchar (20) not null
-- )

-- create table customer_profile(
-- 	id serial,
-- 	isLoggedIn bool default false,
-- 	customer_id int,
-- 	FOREIGN KEY (customer_id) REFERENCES customer(id) on delete restrict
-- )

-- insert into customer (first_name, last_name)
-- values
-- ('John', 'Doe'),
-- ('Jerome', 'Lalu'),
-- ('Lea', 'Rive')

-- insert into customer_profile (isLoggedIn,customer_id )
-- values
-- (true, (select id from customer where first_name ='John' and last_name = 'Doe')),
-- (default, (select id from customer where first_name ='Jerome' and last_name = 'Lalu'))
-- 1
-- select c.first_name, cp.isLoggedIn
-- from customer as c
-- inner join customer_profile as cp
-- on c.id = cp.customer_id
-- where cp.isLoggedIn is true

-- 2
-- select c.first_name, cp.isLoggedIn
-- from customer as c
-- left join customer_profile as cp
-- on c.id = cp.customer_id

-- 3
-- select count(c.first_name)
-- from customer as c
-- inner join customer_profile as cp
-- on c.id = cp.customer_id
-- where cp.isLoggedIn in (null, false)

-- PART 2
-- create table book(
-- 	book_id serial primary key,
-- 	title varchar (50) not null,
-- 	author varchar (50) not null
-- )

-- insert into book
-- values
-- (default,'Alice In Wonderland', 'Lewis Carroll'),
-- (default,'Harry Potter',' J.K Rowling'),
-- (default,'To kill a mockingbird','Harper Lee')


-- create table student(
-- 	student_id serial primary key,
-- 	name varchar (100) not null UNIQUE,
-- 	age int check 9age between 0 and 15)
-- )
-- insert into student
-- values
-- (default,'John', 12),
-- (default,'Lera', 11),
-- (default,'Patrick', 10),
-- (default,'Bob', 14)

-- create table library(
-- 	book_fk_id int not null,
-- 	student_id  int not null,
-- 	primary key(book_fk_id,student_id),
-- 	borrowed_date date, 
-- 	FOREIGN KEY (book_fk_id) REFERENCES book(book_id) ON DELETE CASCADE ON UPDATE CASCADE,
-- 	FOREIGN KEY (student_id) REFERENCES student(student_id) ON DELETE CASCADE ON UPDATE CASCADE
-- )

-- insert into library (student_id, book_fk_id, borrowed_date)
-- values
-- (
-- 	(select student_id from student where name = 'John'),
-- 	(select book_id from book where title = 'Alice In Wonderland'),
-- 	'02/15/2002'
-- ),
-- (
-- 	(select student_id from student where name = 'Bob'),
-- 	(select book_id from book where title = 'To kill a mockingbird'),
-- 	'03/03/2021'
-- ),
-- (
-- 	(select student_id from student where name = 'Lera'),
-- 	(select book_id from book where title = 'Alice In Wonderland'),
-- 	'05/23/2021'
-- ),
-- (
-- 	(select student_id from student where name = 'Bob'),
-- 	(select book_id from book where title = 'Harry Potter'),
-- 	'08/12/2021'
-- )

-- select * from library

-- select s.name, b.title
-- from library as l
-- inner join student as s
-- on s.student_id = l.student_id
-- inner join book as b
-- on b.book_id = l.book_fk_id


-- select avg(s.age)
-- from library as l
-- inner join student as s
-- on s.student_id = l.student_id
-- right join book as b
-- on b.book_id = l.book_fk_id
-- where b.title = 'Alice In Wonderland'

-- delete from student 
-- where student_id = 1
-- select * from library










