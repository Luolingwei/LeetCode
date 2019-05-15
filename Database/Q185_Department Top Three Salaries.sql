--Employee
--+----+-------+--------+--------------+
--| Id | Name  | Salary | DepartmentId |
--+----+-------+--------+--------------+
--| 1  | Joe   | 85000  | 1            |
--| 2  | Henry | 80000  | 2            |
--| 3  | Sam   | 60000  | 2            |
--| 4  | Max   | 90000  | 1            |
--| 5  | Janet | 69000  | 1            |
--| 6  | Randy | 85000  | 1            |
--| 7  | Will  | 70000  | 1            |
--+----+-------+--------+--------------+
--
--Department
--+----+----------+
--| Id | Name     |
--+----+----------+
--| 1  | IT       |
--| 2  | Sales    |
--+----+----------+
--
--Return
--+------------+----------+--------+
--| Department | Employee | Salary |
--+------------+----------+--------+
--| IT         | Max      | 90000  |
--| IT         | Randy    | 85000  |
--| IT         | Joe      | 85000  |
--| IT         | Will     | 70000  |
--| Sales      | Henry    | 80000  |
--| Sales      | Sam      | 60000  |
--+------------+----------+--------+

select Department.Name as Department, Employee.Name as Employee, Employee.Salary as Salary
from Employee inner join Department on Employee.DepartmentId=Department.Id
where (DepartmentId,Salary) in
--取每个部门的top3 Salary
(
select a.DepartmentID,a.Salary from Employee a
inner join Employee b
 on a.DepartmentId=b.DepartmentId and a.Salary<=b.Salary
 group by a.DepartmentId,a.Salary
 having (count(distinct b.Salary))<=3
 )