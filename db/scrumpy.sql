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
    team_id INT NOT NULL REFERENCES teams(id),
    position_id INT NOT NULL REFERENCES positions(id) 

)

