## Novel Reader(backend)

### Steps
1. Clone the repo.
4. check python version and virtual env - `python --version`
5. Create virtual env `python -m venv <env-name>`
6. Activate virtualenv (command for bash shell) - `source <env_name>/Scripts/activate`
7. install python packages `pip install -r requirements.txt`
8. paste the `.env` in root directory
9. start the server `flask run`

### Env config
* `FLASK_DEBUG` - Set it to `1` to run in debug
* `MONGO_USERNAME` - mongoDB username of database
* `MONGO_PASSWORD` - mongoDB password of database 
* `MONGO_CLUSTER` - mongoDB cluster name of database

### Docs
Start the server. Docs at `/api/docs`

Find the frontend [here](https://github.com/con-artist/Novel-Reader)

Please let us know if there are any issues in above steps. Happy coding!
