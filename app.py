from flask import Flask, send_file

from routes import router
from docs import swaggerui_blueprint
from settings import Swagger


app = Flask("novel_reader")


# api spec yaml route
@app.route(Swagger.YAML_URL)
def swagger_api_spec():
    return send_file(Swagger.YAML_PATH)


# blueprints
app.register_blueprint(swaggerui_blueprint)
app.register_blueprint(router)


# main routes
@app.route("/")
def home():
    return "<p> This is a novel reader app</p>"
