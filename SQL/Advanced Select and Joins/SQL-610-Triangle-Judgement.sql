# Write your MySQL query statement below
select x,
       y,
       z, 
       case
           when 
                abs(y - z) < x and x < y + z and
                abs(y - x) < z and z < y + x and
                abs(x - z) < y and y < x + z then "Yes"
            else "No"       
       end as triangle
from Triangle;