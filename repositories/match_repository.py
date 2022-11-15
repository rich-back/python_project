import pdb

from db.run_sql import run_sql
from models.team import Team
from models.player import Player
from models.match import Match

import repositories.team_repository as team_repository

def save(match):
    sql = "INSERT INTO matches (home_team, away_team, home_stadium, home_score, away_score) VALUES (%s, %s, %s, %s, %s) RETURNING id"
    values = [match.home_team.id, match.away_team.id, match.home_stadium.id, match.home_score, match.away_score]
    results = run_sql(sql, values)
    id = results[0]['id']
    match.id = id

def select_all():
    matches = []
    sql = "SELECT * FROM matches"
    results = run_sql(sql)

    for result in results:
        home_team = team_repository.select(result["home_team"])
        away_team = team_repository.select(result["away_team"])
        home_stadium = team_repository.select(result["home_stadium"])
        match = Match(home_team, away_team, home_stadium, result["home_score"], result["away_score"], result["id"])
        matches.append(match)
    return matches

