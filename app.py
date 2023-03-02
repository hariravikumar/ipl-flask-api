from flask import Flask, jsonify, request
import ipl
import iplextra
import json

app = Flask(__name__)

@app.route('/')
def home():
    return "IPL"


@app.route('/api/teams')
def teams():
    teams = ipl.teamsAPI()
    return jsonify(teams)


@app.route('/api/teamvteam')
def teamvteam():
    team1 = request.args.get('team1')
    team2 = request.args.get('team2')

    response = ipl.teamVteamAPI(team1, team2)
    print(response)
    return jsonify(response)


@app.route('/api/team-record')
def team_record():
    team_name = request.args.get('team')
    response = jugaad.teamAPI(team_name)
    return response


@app.route('/api/batting-record')
def batting_record():
    batsman_name = request.args.get('batsman')
    response = iplextra.batsmanAPI(batsman_name)
    # convert string to  object
    #print(response)
    response = json.loads(response)
    return response


@app.route('/api/bowling-record')
def bowling_record():
    bowler_name = request.args.get('bowler')
    response = iplextra.bowlerAPI(bowler_name)
    # convert string to  object
    response = json.loads(response)

    return response

@app.route('/api/Team1vsTeam2')
def team1vsteam2():
    team1 = request.args.get('team1')
    team2 = request.args.get('team2')
    response = iplextra.team1vsteam2(team1,team2)
    #print(type(response.get_json()))
    return response

app.run(debug=True)
