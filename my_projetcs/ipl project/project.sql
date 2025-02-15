-- find no.of matches played
use iplindia;
select count(*) as total_matches
from matches;
-- find no.of winning matches by each 
-- team
SELECT winner,count(winner)
FROM matches
group by winner;
-- find total  matches by venue wise
select venue,count(venue) as total
from matches
group by venue
order by total desc;
-- find total no. of matches by season wise
select season,count(season) as total
from matches
group by season
order by season;
-- find total matches won by 
-- " mumbai indians " season wise
select season,count(*) as  winning_matches
from matches
where winner="Royal Challengers Bangalore"
group by season;
 



