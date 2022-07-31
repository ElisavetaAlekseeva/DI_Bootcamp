-- create table product_orders(
-- id serial primary key
-- );
-- create table items(
-- id serial primary key,
-- name varchar (200),
-- price float not null,
-- order_id int,
-- foreign key (order_id) references product_orders(id)
-- )
-- insert into product_orders
-- values
-- (default),
-- (default),
-- (default),
-- (default),
-- (default)
-- insert into items values
-- (default, 'ball1', 100,(select id from product_orders where id = 1)),
-- (default, 'ball2', 100,(select id from product_orders where id = 2)),
-- (default, 'ball3', 100,(select id from product_orders where id = 3)),
-- (default, 'ball4', 100,(select id from product_orders where id = 4)),
-- (default, 'ball5', 100,(select id from product_orders where id = 5))




CREATE or REPLACE FUNCTION total_price(oi int) 
RETURNS float AS $$
declare
    total_sum float;
BEGIN
   total_sum := (select sum(price) from (select i.name, i.price, po.id 
		from items as i
		inner join 
		(select * from product_orders where id = oi) as po 
		on i.order_id = po.id) as t
		order by sum(price))
		;
   RETURN total_sum;
   
END;
$$ LANGUAGE plpgsql;
select * from total_price(1);




