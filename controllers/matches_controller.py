from flask import Blueprint, Flask, redirect, render_template, request
import pdb
import random
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

@matches_blueprint.route("/matches/new")
def new_match():
    teams = team_repository.select_all()
    return render_template("matches/new.html", teams=teams)

@matches_blueprint.route("/matches", methods=["POST"])
def add_match():
    home_team = request.form["home_team"]
    away_team = request.form["away_team"]
    home_stadium = request.form["home_stadium"]
    home_score = random.randint(0,50)
    away_score = random.randint(0,50)
    match_to_add = Match(home_team, away_team, home_stadium, home_score, away_score)
    match_repository.save(match_to_add)
    return redirect("/matches")

@matches_blueprint.route("/matches/<id>/delete", methods=["POST"])
def delete_match(id):
    match_repository.delete(id)
    return redirect("/matches")


