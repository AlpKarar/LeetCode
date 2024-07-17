# Write your MySQL query statement below
select p.product_id, coalesce(round(sum(price * units) / sum(units), 2), 0) as average_price
from Prices as p
left join UnitsSold as u
on u.product_id = p.product_id
and purchase_date between start_date and end_date
group by p.product_id;