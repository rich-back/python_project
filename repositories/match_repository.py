import pdb

from db.run_sql import run_sql
from models.team import Team
from models.player import Player
from models.match import Match

import repositories.team_repository as team_repository

def save(match):
  
    sql = "INSERT INTO matches (home_team, away_team, home_stadium, home_score, away_score) VALUES (%s, %s, %s, %s, %s) RETURNING id"
    values = [match.home_team, match.away_team, match.home_stadium, match.home_score, match.away_score]
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

def delete(id):
    sql = "DELETE FROM matches WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def select(id):
    sql = "SELECT * FROM matches WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        match = Match(result["home_team"], result["away_team"], result["home_stadium"], result["home_score"], result["away_score"], result["id"])
    return match

def find_winner(matches, team):
    winners = []
    sql = "SELECT * FROM matches"
    values = [matches, team]    
    results = run_sql(sql, values)

    for match in results:

        if match['home_score'] > match['away_score'] and match['home_team'] == team.id:
            winners.append(team_repository.select(match['home_team']))
        
        elif match['away_score'] > match['home_score'] and match['away_team'] == team.id:
            winners.append(team_repository.select(match['away_team']))

    count = 0
    for winner in winners:
        if isinstance(winner, Team):
            count += 1
    print(count)










# def find_winner(matches, team):
#     winners = []
#     drawers = []
#     sql = "SELECT * FROM matches"
#     values = [matches, team]    
#     results = run_sql(sql, values)
#     # pdb.set_trace()

#     for match in results:

#         if match['home_score'] > match['away_score'] and match['home_team'] == team.id:
#             winners.append(team_repository.select(match['home_team']))
        
#         elif match['away_score'] > match['home_score'] and match['away_team'] == team.id:
#             winners.append(team_repository.select(match['away_team']))
     
#         # else:
#         #     drawers.append(team_repository.select(match['home_team']))
#         #     drawers.append(team_repository.select(match['away_team']))
#     # return winners, drawers
#     count = 0
#     for winner in winners:
#         if isinstance(winner, Team):
#             count += 1
#     print(count)
    
    # count2 = 0

    # for drawer in drawers:
    #     if isinstance(drawer, Team):
    #         count2 += 1
    # print(count2)



# def select_by_team(team):
#     matches=[]
#     sql = "SELECT * FROM matches WHERE matches.home_team = %s OR matches.away_team = %s"
#     values = [team.id]
#     results = run_sql(sql,values)
#     if results:
#         result = results[0]
#     for result in results:
#         match = Match(result["home_team"], result["away_team"], result["home_stadium"], result["home_score"], result["away_score"], result["id"])
#         matches.append(match)
#     pdb.set_trace()
#     return matches        






