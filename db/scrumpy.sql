DROP TABLE IF EXISTS matches;
DROP TABLE IF EXISTS players;
DROP TABLE IF EXISTS positions;
DROP TABLE IF EXISTS teams;



CREATE TABLE teams (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    stadium VARCHAR(255)
);

CREATE TABLE positions (
    id SERIAL PRIMARY KEY,
    position VARCHAR(255),
    shirt_num INT
);

CREATE TABLE players (
    id SERIAL PRIMARY KEY,
    f_name VARCHAR(255),
    l_name VARCHAR(255),
    age INT,
    team_id INT NOT NULL REFERENCES teams(id) ON DELETE CASCADE,
    position_id INT NOT NULL REFERENCES positions(id) ON DELETE CASCADE

);

CREATE TABLE matches (
    id SERIAL PRIMARY KEY,
    home_team INT NOT NULL REFERENCES teams(id) ON DELETE CASCADE,
    away_team INT NOT NULL REFERENCES teams(id) ON DELETE CASCADE,
    home_stadium INT NOT NULL REFERENCES teams(id) ON DELETE CASCADE,
    home_score INT,
    away_score INT

);

