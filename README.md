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