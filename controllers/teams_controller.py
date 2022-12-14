from flask import Blueprint, Flask, redirect, render_template, request

from models.team import Team
from models.player import Player
import repositories.team_repository as team_repository
import repositories.player_repository as player_repository

teams_blueprint = Blueprint("teams", __name__)

@teams_blueprint.route("/teams")
def teams():
    teams = team_repository.select_all()
    return render_template("teams/index.html", teams=teams)

@teams_blueprint.route("/teams/new")
def new_team():
    teams = team_repository.select_all()
    return render_template("teams/new.html", teams=teams)

@teams_blueprint.route("/teams/<id>/delete", methods=["POST"])
def delete_team(id):
    team_repository.delete(id)
    return redirect("/teams")

@teams_blueprint.route("/teams", methods=["POST"])
def add_team():
    team_name = request.form["team-name"]
    team_stadium = request.form["team-stadium"]
    team_to_add = Team(team_name, team_stadium)
    team_repository.save(team_to_add)
    return redirect("/teams")

@teams_blueprint.route("/teams/<id>")
def show_team(id):
    team = team_repository.select(id)
    players = team_repository.players_in_team(team)
    return render_template("teams/show.html", team = team, players = players)

# EDIT
@teams_blueprint.route("/teams/<id>/edit")
def edit_team(id):
    team = team_repository.select(id)
    return render_template('teams/edit.html', team=team)


# UPDATE
@teams_blueprint.route("/teams/<id>", methods=["POST"])
def update_team(id):
    name = request.form["name"]
    stadium = request.form["stadium"]
    team = Team(name, stadium, id)
    team_repository.update(team)
    return redirect("/teams")