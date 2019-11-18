--In social network like Facebook or Twitter, people send friend requests and accept others' requests as well.
--
--
--
--Table request_accepted
--
--+--------------+-------------+------------+
--| requester_id | accepter_id | accept_date|
--|--------------|-------------|------------|
--| 1            | 2           | 2016_06-03 |
--| 1            | 3           | 2016-06-08 |
--| 2            | 3           | 2016-06-08 |
--| 3            | 4           | 2016-06-09 |
--+--------------+-------------+------------+
--This table holds the data of friend acceptance, while requester_id and accepter_id both are the id of a person.


# Write your MySQL query statement below
select id, count(*) as num
from
(
    select requester_id as id from request_accepted
    union all
    select accepter_id as id from request_accepted
) a
group by id
order by num DESC
limit 1