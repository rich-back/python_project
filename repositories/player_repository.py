import pdb

from db.run_sql import run_sql
from models.player import Player
from models.team import Team


def save(player):
    sql = "INSERT INTO players (f_name, l_name, age, team_id, position_id) VALUES (%s, %s, %s, %s, %s) RETURNING id"
    values = [player.f_name, player.l_name, player.age, player.team.id, player.position.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    player.id = id

def delete_all():
    sql = "DELETE FROM players"
    run_sql(sql)