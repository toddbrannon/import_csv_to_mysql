### command to start the virtual environment: python3 - m venv env:  ###
pipenv shell

### pandas API reference:  ### 
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_sql.html

# import_csv_to_mysql
Python script sweeps folder for csv files to create df and then imports to mysql db

### Masking Database Credentials in the import_df.py Code ###
Note the MySQL connection code refers to masked credentials in the create_engine call. Replace the values for the 'user', 'pw', and 'db' with your own values directly into the import_df.py file, or create a databaseconfig.py file with your MySQL credentials and import the config file into the import_df.py file to mask your credentials (the import_df.py file already contains ``` import databaseconfig as cfg ``` to accomplish this).

### Database Connection ###
a
```
con = sq.create_engine("mysql+pymysql://{user}:{pw}@localhost/{db}"
                        .format(user=cfg.mysql["user"],
                                pw=cfg.mysql["passwd"],
                                db=cfg.mysql["db"]))
```

If you plan to create a git repo for your project, be sure to add databaseconfig.py to your .gitignore file in order not to expose your db connection credentials.

### Config File ###

Create a databaseconfig.py in the same directory as import_df.py.

Insert the following code into databaseconfig.py, change the values according to your needs and save:

```
mysql = {
    "host": "localhost",
    "user": "root",
    "passwd": "yourpassword",
    "db": "yourdatabase"
}
```
