import os
from flask import Flask, render_template, request, redirect
# from flask_cors import CORS
from flask_migrate import Migrate
# from flask_wtf.csrf import CSRFProtect, generate_csrf
# from flask_login import LoginManager
from .models import db, Player, Roster, Franchise, PlayerScore
from .api.player_routes import player_routes
from .api.player_scores_routes import pscore_routes
from .api.franchise_routes import franchise_routes
from .api.roster_routes import roster_routes
from .seeds import seed_commands
from .config import Config

app = Flask(__name__)

# Setup login manager



# Tell flask about our seed commands
app.cli.add_command(seed_commands)

app.config.from_object(Config)
app.register_blueprint(player_routes, url_prefix='/api/players')
app.register_blueprint(pscore_routes, url_prefix='/api/pscores')
app.register_blueprint(roster_routes, url_prefix='/api/rosters')
app.register_blueprint(franchise_routes, url_prefix='/api/franchises')
db.init_app(app)
Migrate(app, db)

# Application Security
# CORS(app)


# Since we are deploying with Docker and Flask,
# we won't be using a buildpack when we deploy to Heroku.
# Therefore, we need to make sure that in production any
# request made over http is redirected to https.
# Well.........
@app.before_request
def https_redirect():
    if os.environ.get('FLASK_ENV') == 'production':
        if request.headers.get('X-Forwarded-Proto') == 'http':
            url = request.url.replace('http://', 'https://', 1)
            code = 301
            return redirect(url, code=code)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def react_root(path):
    if path == 'favicon.ico':
        return app.send_static_file('favicon.ico')
    return app.send_static_file('index.html')
