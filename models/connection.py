from mongoengine import connect

from settings import Database as Db


db_uri = (
            f"mongodb+srv://{Db.MONGO_USERNAME}:{Db.MONGO_PASSWORD}@"
            f"{Db.MONGO_CLUSTER}.net/?retryWrites=true&w=majority"
    )

db = connect(Db.DB_NAME, host=db_uri)