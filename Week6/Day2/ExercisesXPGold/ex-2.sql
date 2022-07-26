-- Exercise 2: Students Table
-- Instructions
-- Continuation of the Day1 Exercise XPGold : students table
-- Update
-- ‘Lea Benichou’ and ‘Marc Benichou’ are twins, they should have the same birth_dates. Update both their birth_dates to 02/11/1998.
-- Change the last_name of David from ‘Grez’ to ‘Guez’.
-- Delete
-- Delete the student named ‘Lea Benichou’ from the table.
-- Count
-- Count how many students are in the table.
-- Count how many students were born after 1/01/2000.
-- Insert / Alter
-- Add a column to the student table called math_grade.
-- Add 80 to the student which id is 1.
-- Add 90 to the students which have ids of 2 or 4.
-- Add 40 to the student which id is 6.
-- Count how many students have a grade bigger than 83
-- Add another student named ‘Omer Simpson’ with the same birth_date as the one already in the table. Give him a grade of 70.
-- Now, in the table, ‘Omer Simpson’ should appear twice. It’s the same student, although he received 2 different grades because he retook the math exam. 
-- Bonus: Count how many grades each student has.
-- Tip: You should display the first_name, last_name and the number of grades of each student. If you followed the instructions above correctly, all the students should have 1 math grade, except Omer Simpson which has 2.
-- Tip : Use an alias called total_grade to fetch the grades.
-- Hint : Use GROUP BY.
-- SUM
-- Find the sum of all the students grades.



-- 1.1
-- update students
-- set birth_date = '1998/11/02'
-- where first_name = 'Lea' or first_name = 'Marc' and last_name = 'Benichou'
-- 1.2
-- update students
-- set last_name = 'Guez'
-- where last_name = 'Grez' and first_name = 'David'

-- 2
-- delete from students where first_name = 'Lea' and last_name = 'Benichou'

-- 3.1
-- select count(*) from students
-- 3.2
-- select count(*) from students where birth_date > '2000-01-01'


-- Insert / Alter
-- 1
-- alter table students
-- add math_grade int;
-- 2
-- update students
-- set math_grade = 80
-- where id = 1
-- 3
-- update students
-- set math_grade = 90
-- where id = 2 or id = 4
-- 4
-- update students
-- set math_grade = 40
-- where id = 6
-- 5
-- select count(*) from students
-- where math_grade > 83
-- 6
-- insert into students (last_name,first_name,math_grade,birth_date)
-- values
-- ('Simpson','Omer',70,'04/07/1996');
-- 7
-- select count(math_grade), first_name,last_name
-- from students 
-- group by first_name,last_name
-- SUM
-- 1
-- select sum(math_grade) from students

























