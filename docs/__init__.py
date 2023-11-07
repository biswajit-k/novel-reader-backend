from flask_swagger_ui import get_swaggerui_blueprint

from settings import Swagger

"""
    flask-swagger-ui can be thought as a different server that just servers swagger UI
    think of this blueprint and app as completely separate

    tell the blueprint where to serve docs(URL) and on which route it will get yaml file
    (YAML_URL). Rest it will do.
"""
swaggerui_blueprint = get_swaggerui_blueprint(
    Swagger.URL,
    Swagger.YAML_URL,
    config={
        'app_name': "Novel Reader Docs"
    },
)

