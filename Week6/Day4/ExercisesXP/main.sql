-- 1
-- select first_name as "First Name" , last_name as "Last Name" from employees

-- 2
-- select DISTINCT employee_id from employees

-- 3
-- select * from employees order by first_name desc

-- 4
-- select first_name, last_name, salary, (salary / 0.15) as PF from employees

-- 5
-- select employee_id, first_name, last_name, salary from employees order by salary asc

-- 6
-- select sum(salary) from employees

-- 7
-- select max(salary), min(salary) from employees

-- 8
-- select avg(salary) from employees

-- 9
-- select count(employee_id) from employees

-- 10
-- select upper(first_name) from employees

-- 11
-- select substr(first_name, 1,3) from employees

-- 12
-- select (first_name||' '||last_name) as full_name from employees

-- 13
-- select (first_name||' '||last_name) as full_name, length((first_name||' '||last_name)) from employees

-- 14
-- select first_name from employees where first_name like '%[0-9]%'

-- 15
-- select * from employees limit 10

-- 🌟 Restricting And Sorting

-- 1
-- select first_name, last_name, salary from employees where salary between 10000 and 15000

-- 2
-- select first_name, last_name, hire_date from employees  where hire_date between '1987-01-01' and '1987-12-31'

-- 3
-- select * from employees where first_name ilike '%c%' and first_name ilike '%e%'

-- -- 4
-- select e.last_name, j.job_title, e.salary 
-- from employees as e
-- inner join jobs as j
-- on e.job_id = j.job_id
-- where (j.job_title != 'Programmer' and j.job_title != 'Shipping Clerks')
-- and e.salary not in (4500, 10000, 15000)

-- 5
-- select last_name from employees where length(last_name) = 6

-- 6
-- select last_name from employees where last_name ilike '__e%%'

-- 7
-- select e.* , j.job_title
-- from employees as e
-- inner join jobs as j
-- on e.job_id = j.job_id

-- 8
-- select * from employees where last_name = 'JONES' or last_name = 'BLAKE' or last_name = 'SCOTT' or last_name = 'KING' or last_name = 'FORD'






















