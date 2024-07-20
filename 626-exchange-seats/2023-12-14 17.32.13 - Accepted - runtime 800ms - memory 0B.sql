# Write your MySQL query statement below
select s.id, s.student
from (
    select s.id+1 as id, s.student from seat s where s.id % 2 = 1 and s.id != (select count(*) from seat)
    union
    select s.id-1 as id, s.student from seat s where s.id % 2 = 0
    union
    select s.id as id, s.student from seat s where s.id = (select count(*) from seat) and s.id % 2 = 1
) s
order by s.id