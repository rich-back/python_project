import pdb

from db.run_sql import run_sql
from models.team import Team
from models.player import Player


def save(team):
    sql = "INSERT INTO teams (name, stadium) VALUES (%s, %s) RETURNING id"
    values = [team.name, team.stadium]
    results = run_sql(sql, values)
    id = results[0]['id']
    team.id = id

def select_all():
    teams = []
    sql = "SELECT * FROM teams"
    results = run_sql(sql)
    for result in results:
        team = Team(result["name"], result["stadium"], result["id"])
        teams.append(team)
    return teams

def delete_all():
    sql = "DELETE FROM teams"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM teams WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def select(id):
    sql = "SELECT * FROM teams WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        team = Team(result["name"], result["stadium"], result["id"])
    return team

def players_in_team(team):
    players = []

    sql = "SELECT players.*, positions.* FROM positions INNER JOIN players ON positions.id = players.position_id WHERE team_id = %s"
    values = [team.id]
    results = run_sql(sql, values)

    for row in results:
        player = Player(row['f_name'], row['l_name'], row['age'], row['position_id'], row['position'], row['id'])
        players.append(player)
    return players

