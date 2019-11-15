--Customers
--+----+-------+
--| Id | Name  |
--+----+-------+
--| 1  | Joe   |
--| 2  | Henry |
--| 3  | Sam   |
--| 4  | Max   |
--+----+-------+
--
--Orders
--+----+------------+
--| Id | CustomerId |
--+----+------------+
--| 1  | 3          |
--| 2  | 1          |
--+----+------------+

--Return
--+-----------+
--| Customers |
--+-----------+
--| Henry     |
--| Max       |
--+-----------+

select Name as Customers from Customers where Id not in (select CustomerId from Orders)