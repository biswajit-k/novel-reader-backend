## Novel Reader App(backend)
A novel reader app where you can find tons of books ranging from Manga, manhwa and comic. You can
read, bookmark, comment and engage with other community members. This is the backend part of it.

![image](https://github.com/biswajit-k/novel-reader-backend/assets/76483357/b5d1a2d3-aec1-493c-a636-8f4a4664a9db)


### Tech Stack
  - Flask
  - MongoDB
  - Swagger

### Installation Steps
1. Clone the repo.
4. check python version and virtual env - `python --version`
5. Create virtual env `python -m venv manga_env`
6. Activate virtualenv (command for bash shell) - `source manga_env/Scripts/activate`
7. install python packages `pip install -r requirements.txt`
8. paste the `.env` in root directory
9. start the server `flask run`

### Env config
* `FLASK_DEBUG` - Set it to `1` to run in debug
* `MONGO_USERNAME` - mongoDB username of database
* `MONGO_PASSWORD` - mongoDB password of database 
* `MONGO_CLUSTER` - mongoDB cluster name of database

### Swagger Docs
Docs are present at `/api/docs`

Find the frontend [here](https://github.com/con-artist/Novel-Reader)

Please let us know if there are any issues in above steps. Happy coding!
