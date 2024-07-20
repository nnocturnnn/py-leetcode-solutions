# Write your MySQL query statement below
select visited_on,
amount + amount1 + amount2 + amount3 + amount4 + amount5 + amount6 as amount,
round((amount + amount1 + amount2 + amount3 + amount4 + amount5 + amount6)/7,2) as average_amount
from 
  (select visited_on,
  amount,
  lag(amount, 1) over() as amount1,
  lag(amount, 2) over() as amount2,
  lag(amount, 3) over() as amount3,
  lag(amount, 4) over() as amount4,
  lag(amount, 5) over() as amount5,
  lag(amount, 6) over() as amount6
  from (select visited_on, sum(amount) as amount from Customer group by 1) as temp2
  group by 1) as temp
group by 1
having visited_on >= date_add((select visited_on from Customer limit 1), interval 6 day)
order by 1 