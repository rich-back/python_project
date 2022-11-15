from flask import Blueprint, Flask, redirect, render_template, request

from models.team import Team
from models.player import Player
import repositories.team_repository as team_repository
import repositories.player_repository as player_repository

players_blueprint = Blueprint("players", __name__)

@players_blueprint.route("/players")
def players():
    players = player_repository.select_all()
    return render_template("players/index.html", players=players)
