import pdb

import repositories.player_repository as player_repository
import repositories.position_repository as position_repository
import repositories.team_repository as team_repository
from models.player import Player
from models.position import Position
from models.team import Team

team_repository.delete_all()
player_repository.delete_all()
position_repository.delete_all()

team1 = Team("Edinburgh", "The DAM Health Stadium")
team_repository.save(team1)

team2 = Team("Glasgow Warriors", "Scotstoun Stadium")
team_repository.save(team2)

team3 = Team("Leinster", "The Aviva Stadium")
team_repository.save(team3)


position1 = Position('Loosedhead Prop', 1)
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

player1 = Player("Blair", "Kinghorn", 25, team1, position10)
player_repository.save(player1)

player2 = Player("Duhan", "Van Der Merwe", 27, team1, position11)
player_repository.save(player2)

player3 = Player("Pierre", "Schoeman", 28, team1, position1)
player_repository.save(player3)

player4 = Player("Zander", "Fagerson", 24, team2, position3)
player_repository.save(player4)

player5 = Player("George", "Turner", 30, team2, position2)
player_repository.save(player5)

player6 = Player("Kyle", "Steyn", 28, team2, position13)
player_repository.save(player6)

print(team_repository.players_in_team(team1))











pdb.set_trace()
