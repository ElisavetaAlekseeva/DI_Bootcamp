-- 1
select count(actor_id) from actors;
-- 2
insert into actors (first_name, last_name, age, number_oscars)
values
('', '', null, null)
-- outcome will be an error