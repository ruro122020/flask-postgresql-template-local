Backend flask application using postgresql.

This template will get you started with the backend of an application that will need a user account feature. 

The user model, marshmallow schema, and routes have been created to get you started. (adjust code to your projects needs)

For the account feature to work the following is needed:

1. Install packages 
``` 
pipenv install 
```
2. Create a .env file in the root directory
3. Create an enviromental variable and set it equal to anything you want. You can also generate a key by running the following in the ubuntu terminal. Set the results to your variable. 

```
python -c 'import os; print(os.urandom(16))'
```
4. In the config.py file add the variable name like so:

```
app.secret_key= os.getenv('YOUR ENVIROMENT VARIABLE GOES HERE')
```

Assuming postgresql is installed and ready to use, to use the user account feature:

1. Start postgresql server in one ubuntu terminal 

Note: postgresql database server is separate from the flask API server. When starting the database locally, you can start it from any root user in the ubuntu terminal. It doesn't need to be at the root of the projects directory but that is okay too.

```
sudo service postgresql start
psql -U {user} -d {dbname}
```
Leave postgres terminal running

2. Start the flask application in another ubuntu terminal in the project root directory

```
pipenv shell
python app.py
```
