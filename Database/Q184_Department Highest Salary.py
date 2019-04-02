
select
    Department.Name as Department,
    Employee.Name as Employee,
    Employee.Salary as Salary
    from Employee left join Department on Employee.DepartmentId=Department.Id
    where (Employee.DepartmentId,Employee.Salary) in (select DepartmentId,max(Salary) as Salary from Employee group by DepartmentId)
    and Department.Name is not Null




