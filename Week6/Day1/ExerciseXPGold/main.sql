create table students (
	id SERIAL PRIMARY KEY,
	last_name varchar (10) NOT NULL,
	first_name varchar (10) NOT NULL,
	birth_date DATE NOT NULL
);

insert into students (first_name,last_name,birth_date)
values
('Marc', 'Benichou', '11/02/1998'),
('Yoan', 'Cohen', '12/03/2010'),
('Lea', 'Benichou', '07/27/1987'),
('Amelia', 'Dux', '04/07/1996'),
('David', 'Grez', '06/14/2003'),
('Omer', 'Simpson', '10/03/1980');


-- 1
select first_name, last_name, birth_date from students ORDER BY last_name ASC
limit 4;
-- 2
select first_name, last_name, max(birth_date) from students;
-- 3
select first_name, last_name, birth_date from students limit 3 offset 2;






