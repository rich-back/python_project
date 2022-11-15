from flask import Blueprint, Flask, redirect, render_template, request

from models.team import Team
from models.player import Player
from models.match import Match

import repositories.team_repository as team_repository
import repositories.player_repository as player_repository
import repositories.match_repository as match_repository

matches_blueprint = Blueprint("matches", __name__)

@matches_blueprint.route("/matches")
def matches():
    matches = match_repository.select_all()
    return render_template("matches/index.html", matches=matches)

    
