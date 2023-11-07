import os

# DB
class Database():
    DB_NAME = 'novel_reader'
    MONGO_USERNAME = os.environ.get('MONGO_USERNAME')
    MONGO_PASSWORD = os.environ.get('MONGO_PASSWORD')
    MONGO_CLUSTER = os.environ.get('MONGO_CLUSTER')

# Swagger
class Swagger():
    URL = '/api/docs'                               # route to get api docs
    YAML_URL = '/api/docs/api_spec.yaml'            # route for requesting yaml file
    YAML_PATH = './docs/api_spec.yaml'              # relative path from app to yaml
