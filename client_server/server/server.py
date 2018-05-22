# from flask import Flask, jsonify
from flask import Flask, render_template, jsonify
from arcgis.gis import GIS 
from config import agol_unpw
from api.distribute import create_distribute_bp

app = Flask(__name__, static_url_path='/', static_folder='client/build')

gis = GIS(profile="client_server")
app.register_blueprint(create_distribute_bp(gis), url_prefix="/api/distribute")

# @app.route("/organization")
# def hello_world():
#     return jsonify({'res': agol_unpw['un']})