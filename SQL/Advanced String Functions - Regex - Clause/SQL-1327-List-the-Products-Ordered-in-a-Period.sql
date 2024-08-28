# Write your MySQL query statement below
with orders_cte as (
    select product_id, sum(unit) as unit
    from Orders
    where year(order_date) = 2020 and month(order_date) = 2
    group by product_id
    having sum(unit) >= 100
)
select p.product_name as product_name, o.unit as unit
from Products as p
join orders_cte as o
on p.product_id = o.product_id;