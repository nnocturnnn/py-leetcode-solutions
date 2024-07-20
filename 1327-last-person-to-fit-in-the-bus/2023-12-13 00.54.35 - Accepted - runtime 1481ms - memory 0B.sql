# Write your MySQL query statement below
select person_name
from
(
    select person_name, 
    sum(weight) over(order by turn) as cum_weight
    from queue
) temp
where cum_weight<=1000
order by cum_weight desc
limit 1;