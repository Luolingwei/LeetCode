--Write a SQL query to find all numbers that appear at least three times consecutively.
--
--+----+-----+
--| Id | Num |
--+----+-----+
--| 1  |  1  |
--| 2  |  1  |
--| 3  |  1  |
--| 4  |  2  |
--| 5  |  1  |
--| 6  |  2  |
--| 7  |  2  |
--+----+-----+

select distinct l1.num as ConsecutiveNums from
Logs l1
inner join Logs l2 on l1.Id=l2.Id+1 and l1.Num=l2.Num
inner join Logs l3 on l1.Id=l3.Id+2 and l1.Num=L3.Num
