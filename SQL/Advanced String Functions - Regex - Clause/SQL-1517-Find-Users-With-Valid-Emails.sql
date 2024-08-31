# Write your MySQL query statement below
select *
from Users
where mail regexp '^[a-zA-Z]{1}[a-zA-Z0-9_.-]*@leetcode\\.com$';