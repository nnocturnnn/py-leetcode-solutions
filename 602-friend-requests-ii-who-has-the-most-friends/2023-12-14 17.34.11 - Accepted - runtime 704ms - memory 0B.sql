# Write your MySQL query statement below
select ra.id, sum(ra.id_sum) as num
from
(select r1.requester_id as id, count(distinct r1.accepter_id) as id_sum
from RequestAccepted r1
group by r1.requester_id
union all
select r2.accepter_id as id, count(r2.accepter_id) as id_sum
from RequestAccepted r2
group by r2.accepter_id) ra
group by ra.id
order by num desc
limit 1;
