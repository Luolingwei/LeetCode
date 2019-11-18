--Table: friend_request
--| sender_id | send_to_id |request_date|
--|-----------|------------|------------|
--| 1         | 2          | 2016_06-01 |
--| 1         | 3          | 2016_06-01 |
--| 1         | 4          | 2016_06-01 |
--| 2         | 3          | 2016_06-02 |
--| 3         | 4          | 2016-06-09 |
--
--
--Table: request_accepted
--| requester_id | accepter_id |accept_date |
--|--------------|-------------|------------|
--| 1            | 2           | 2016_06-03 |
--| 1            | 3           | 2016-06-08 |
--| 2            | 3           | 2016-06-08 |
--| 3            | 4           | 2016-06-09 |
--| 3            | 4           | 2016-06-10 |


-- Write your MySQL query statement below

select round(ifnull(b.acceptnum/a.sendnum,0),2) as accept_rate
from
(
select count(distinct sender_id,send_to_id) as sendnum
from friend_request
) a
,
(
select count(distinct requester_id,accepter_id) as acceptnum
from request_accepted
) b