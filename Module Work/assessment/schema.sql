CREATE TABLE players (
	player_id INT NOT NULL,
	first_name varchar(40) NOT NULL,
	last_name varchar(40) NOT NULL,
	hand VARCHAR(1) NOT NULL,
	country_code VARCHAR(3) NOT NULL,
	primary key (player_id)
);

CREATE TABLE matches (
	loser_age DEC NOT NULL,
	loser_id INT NOT NULL,
	loser_name varchar(80) NOT NULL,
	loser_rank INT NOT NULL,
	winner_age DEC NOT NULL,
	winner_id INT NOT NULL,
	winner_name VARCHAR(80) NOT NULL,
	winner_rank INT NOT NULL
);

drop table matches, players;

commit;