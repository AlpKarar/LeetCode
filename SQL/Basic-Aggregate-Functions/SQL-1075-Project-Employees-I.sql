# Write your MySQL query statement below
with project_total_employees as (
    select project_id, count(employee_id) as t_e
    from Project
    group by project_id
), project_total_experience_years as (
    select project_id, sum(e.experience_years) as exper
    from Project as p
    join Employee as e
    on p.employee_id = e.employee_id
    group by p.project_id
)
select t_emp.project_id, round(t_exp.exper / t_emp.t_e, 2) as average_years
from project_total_employees as t_emp
join project_total_experience_years as t_exp
on t_emp.project_id = t_exp.project_id;