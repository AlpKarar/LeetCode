# Write your MySQL query statement below
with c as (
    select user_id, count(user_id) as confirmed
    from Confirmations
    group by user_id, action
    having action = 'confirmed'
), t as (
    select user_id, count(*) as total
    from Confirmations
    group by user_id
)
select s.user_id, coalesce(round(c.confirmed / t.total, 2), 0) as confirmation_rate
from c
join t
on c.user_id = t.user_id
right join Signups as s
on s.user_id = c.user_id;