--Employee
--+----+--------+
--| Id | Salary |
--+----+--------+
--| 1  | 100    |
--| 2  | 200    |
--| 3  | 300    |
--+----+--------+
--
--+---------------------+
--| SecondHighestSalary |
--+---------------------+
--| 200                 |
--+---------------------+

select
    ifnull(
            (
                select
                    distinct Salary from Employee order by Salary desc
                    limit 1 offset 1
            ),
            NULL
          ) as SecondHighestSalary