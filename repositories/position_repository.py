import pdb

from db.run_sql import run_sql
from models.position import Position

def save(position):
    sql = "INSERT INTO positions (position, shirt_num) VALUES (%s, %s) RETURNING id"
    values = [position.position, position.shirt_num]
    results = run_sql(sql, values)
    id = results[0]['id']
    position.id = id

def delete_all():
    sql = "DELETE FROM positions"
    run_sql(sql)

def select(id):
    sql = "SELECT * FROM positions WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        position = Position(result["position"], result["shirt_num"], result["id"])
    return position