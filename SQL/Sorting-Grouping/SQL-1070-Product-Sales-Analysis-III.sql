# Write your MySQL query statement below
with min_year_in_group as (
    select product_id, min(year) as min_year
    from Sales
    group by product_id
)
select s.product_id, year as first_year, quantity, price
from Sales as s
join min_year_in_group as m
on s.product_id = m.product_id and s.year = m.min_year;