import pdb

import repositories.player_repository as player_repository
import repositories.position_repository as position_repository
import repositories.team_repository as team_repository
import repositories.match_repository as match_repository
from models.player import Player
from models.position import Position
from models.team import Team
from models.match import Match

team_repository.delete_all()
player_repository.delete_all()
position_repository.delete_all()

team1 = Team("Edinburgh", "The DAM Health Stadium")
team_repository.save(team1)
team2 = Team("Glasgow Warriors", "Scotstoun Stadium")
team_repository.save(team2)
team3 = Team("Leinster", "The Aviva Stadium")
team_repository.save(team3)
team4 = Team("Munster", "Thomond Park")
team_repository.save(team4)
team5 = Team("Connacht", "Galway Sportsgrounds")
team_repository.save(team5)
team6 = Team("Ulster", "Ravenhill Stadium")
team_repository.save(team6)
team7 = Team("Dragons", "Rodney Parade")
team_repository.save(team7)
team8 = Team("Ospreys", "Swansea.com Stadium")
team_repository.save(team8)
team9 = Team("Scarlets", "Parc y Scarlets")
team_repository.save(team9)
team10 = Team("Cardiff", "Cardiff Arms Park")
team_repository.save(team10)
team11 = Team("Benetton", "Stadio Comunale di Monigo")
team_repository.save(team11)
team12 = Team("Zebre", "Stadio Sergio Lanfranchi")
team_repository.save(team12)


position1 = Position('Loosehead Prop', 1)
position_repository.save(position1 )
position2= Position('Hooker', 2)
position_repository.save(position2 )
position3 = Position('Tighthead Prop', 3)
position_repository.save(position3 )
position4 = Position('Second Row', 4)
position_repository.save(position4 )
position5 = Position('Second Row', 5)
position_repository.save(position5 )
position6 = Position('Blindside Flanker', 6)
position_repository.save(position6 )
position7 = Position('Openside Flanker', 7)
position_repository.save(position7 )
position8 = Position('Number 8', 8)
position_repository.save(position8 )
position9 = Position('Scrum-Half', 9)
position_repository.save(position9 )
position10 = Position('Fly-Half', 10)
position_repository.save(position10 )
position11 = Position('Left Wing', 11)
position_repository.save(position11 )
position12 = Position('Inside Centre', 12)
position_repository.save(position12 )
position13 = Position('Outside Center', 13)
position_repository.save(position13 )
position14 = Position('Right Wing', 14)
position_repository.save(position14 )
position15 = Position('Full Back', 15)
position_repository.save(position15 )

player1 = Player("Boan", "Venter", 25, team1, position1)
player_repository.save(player1)
player2 = Player("Adam", "McBurney", 27, team1, position2)
player_repository.save(player2)
player3 = Player("Luan", "De Bruin", 28, team1, position3)
player_repository.save(player3)
player4 = Player("Pierce", "Phillips", 24, team1, position4)
player_repository.save(player4)
player5 = Player("Jamie", "Hodgson", 30, team1, position5)
player_repository.save(player5)
player6 = Player("Ben", "Muncaster", 28, team1, position6)
player_repository.save(player6)
player7 = Player("Luke", "Crosbie", 25, team1, position7)
player_repository.save(player7)
player8 = Player("Viliame", "Mata", 27, team1, position8)
player_repository.save(player8)
player9 = Player("Charlie", "Shiel", 28, team1, position9)
player_repository.save(player9)
player10 = Player("Charlie", "Savala", 24, team1, position10)
player_repository.save(player10)
player11 = Player("Wes", "Goosen", 30, team1, position11)
player_repository.save(player11)
player12 = Player("Chris", "Dean", 28, team1, position12)
player_repository.save(player12)
player13 = Player("Matt", "Currie", 25, team1, position13)
player_repository.save(player13)
player14 = Player("Jack", "Blain", 27, team1, position14)
player_repository.save(player14)
player15 = Player("Emiliano", "Boffelli", 28, team1, position15)
player_repository.save(player15)



match1 = Match(team1.id, team1.id, team1.id, 27, 21)
match_repository.save(match1)
match2 = Match(team1.id, team3.id, team1.id, 12, 12)
match_repository.save(match2)
match3 = Match(team1.id, team3.id, team1.id, 34, 45)
match_repository.save(match3)
match4 = Match(team3.id, team1.id, team3.id, 12, 23)
match_repository.save(match4)

matches = [match1, match2, match3, match4]

match_repository.find_winner(matches, team3)


# match_repository.select_by_team(team1)

# pdb.set_trace()












