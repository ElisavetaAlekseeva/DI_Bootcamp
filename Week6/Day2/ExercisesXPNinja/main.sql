-- 1
-- select * from (select * from customers order by customers_last_name desc limit 2)as c order by customers_last_name asc

-- 2
-- delete
-- from purchases as p
-- where p.customer_id = (
-- select c.customer_id
-- from purchases as p
-- left join customers as c
-- on c.customer_id = p.customer_id
-- where c.customers_first_name = 'Scott')
-- delete from customers
-- where customers_first_name = 'Scott'

-- 3
-- select * from customers 
-- where customers_first_name = 'Scott'

-- 4

-- 5
-- select p.*, c.*
-- from purchases as p
-- full outer join customers as c
-- on c.customer_id = p.customer_id












