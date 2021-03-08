select * from players;
select * from matches;

select count(winner_name)
from matches
where winner_name = 'Serena Williams';

select hand, count(hand)
from players
group by hand;

select ma.loser_age,
	ma.loser_id,
	ma.loser_name,
	ma.loser_rank,
	ma.winner_age,
	ma.winner_id,
	ma.winner_name,
	pl.hand,
	ma.winner_rank
from matches as ma
inner join players as pl
on ma.winner_id = pl.player_id;
group by hand

select count(pl.hand), pl.hand

from matches as ma
inner join players as pl
on ma.winner_id = pl.player_id
group by pl.hand;

rollback;