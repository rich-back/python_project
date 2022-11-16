import pdb

from db.run_sql import run_sql
from models.player import Player
from models.team import Team
from repositories import team_repository, position_repository


def save(player):
    sql = "INSERT INTO players (f_name, l_name, age, team_id, position_id) VALUES (%s, %s, %s, %s, %s) RETURNING id"
    values = [player.f_name, player.l_name, player.age, player.team.id, player.position.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    player.id = id

def delete_all():
    sql = "DELETE FROM players"
    run_sql(sql)

def delete():
    sql = "DELETE FROM players WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def select_all():
    players = []
    sql = "SELECT * FROM players"
    results = run_sql(sql)

    for result in results:
        team_id = team_repository.select(result["team_id"])
        position_id = position_repository.select(result["position_id"])
        player = Player(result["f_name"], result["l_name"], result["age"], team_id, position_id, result["id"])
        players.append(player)
    return players




