# FLASK API with PostgreSQL

This template will get you started with a flask application using PostgreSQL and Marshmallow. It comes with a user account feature setup as well.

The user model, marshmallow schema, and login/signup/checksession routes have been created to get you started. (Adjust code to your projects needs)

### POSTGESQL SETUP

Postgresql is a database server seperate from the flask application server. When starting the database locally, you can start it from any root in the terminal. It doesn't need to be at the root of your project but that is okay too.

Start postgesql database:

```
sudo service postgresql start
psql -U username -d database_name
```

Leave postgres terminal running...

### VIRTUAL ENVIRONMENT SETUP

Open another terminal.
Check if you already have virtualenv installed:

```
virtualenv --version
#Output should be: 20.31.2 or higher
```

If a version number was not displayed install virtualenv:

```
pip3 install virtualenv
```

Note: installation may very depending on the OS you're using.

To create the virtual environment:

```
virtualenv -p python3 venv
```

To start and activate environment:

```
source venv/bin/activate
```

Once the Environment has been set up you want to install the packages in requirement.txt file. Run:

```
pip3 install -r requirements.txt
```

To run the flask application

```
python app.py
```

### FLASK DB SETUP

```
flask db init
flask db migrate -m 'initial migration'
flask db upgrade
```

### COOKIES SESSION SETUP

To cookies, do the following:

1. Create a .env file in the root directory
2. Create an enviromental variable and set it equal to anything you want. You can also generate a key by running the following in the ubuntu terminal. Set the results to your variable.

```
python -c 'import os; print(os.urandom(16))'
```

3. In the following line add the variable name like so:

```
app.secret_key= os.getenv('YOUR ENVIROMENT VARIABLE NAME GOES HERE')
```

Follow these instructions if you want to use pyenv [here](https://ruthr.hashnode.dev/api-template-with-flask-sqlalchemy-postgresql)

Feel free to raise an issue if you run into any problems!

Happy coding! 😊
