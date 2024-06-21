# Write your MySQL query statement below
select machine_id,
    round((r.end_total - r.start_total) / (select count(distinct process_id) from Activity), 3) as processing_time
from (
    select machine_id,
        sum(if(activity_type = 'start', timestamp, 0)) as start_total,
        sum(if(activity_type = 'end', timestamp, 0)) as end_total
    from Activity
    group by machine_id
) as r;