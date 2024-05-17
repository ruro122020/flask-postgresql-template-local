Backend flask application using sqlite.

After installing packages, to use flask session object for cookies, do the following:

1. Create a .env file in the root directory
2. Create an enviromental variable and set it equal to anything you want. You can also generate a key by running the following in the ubuntu terminal. Set the results to your variable. 

```
python -c 'import os; print(os.urandom(16))'
```
3. In the following line add the variable name like so:

```
app.secret_key= os.getenv('YOUR ENVIROMENT VARIABLE GOES HERE')
```

Assuming postgresql is installed and ready to use, to start working on project:

1. Start postgresql server in one ubuntu terminal

```
sudo service postgresql start
sudo -i -u postgres psql
```
Leave postgres terminal running

2. Start the flask application in another ubuntu terminal

```
pipenv shell
python app.py
```
