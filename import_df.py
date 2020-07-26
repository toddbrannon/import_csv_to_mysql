# This script reads all csv's in a directory, 
# passes the data into a dataframe, 
# inserts them into a db table
# and then moves the files to an archive folder

import pandas as pd 
from glob import glob
import sqlalchemy as sq
import databaseconfig as cfg
import shutil
import os

# Source and destination paths for csv files
source = '/Users/toddbrannon/Documents/CSV/' # Adapt this to your own source path where your data files will be
dest  =  '/Users/toddbrannon/Documents/CSV/Archive/' # Adapt this to your own needs -  destination file path to move data files

# location of all the csv files with data to be assigned to dataframe
acct_files = sorted(glob(source + '*.CSV')) # Adapt this to your own needs (file extension)

# iterate over all files in 'acct_files' directory and create dataframe
# if not csv files, make sure you use the appropriate pandas Input/Output method
# https://pandas.pydata.org/pandas-docs/stable/reference/io.html

filecount = len(acct_files)

if filecount < 1:
        # Print an error message to the terminal
        print(" ")
        print("*** SCRIPT ERROR MESSAGE ***")
        print("No files found in the filepath: ")
        print(source)
        print("Please check the filepath and try again!")
        print("*** END ERROR MESSAGE ***")
        print(" ")
else:        
        # Create dataframe df from csv data
        df = pd.concat((pd.read_csv(file).assign(filename = file) 
        for file in acct_files), ignore_index = True)

        # move the csv files to the archive folder
        for file in acct_files:
            shutil.move(os.path.join(source,file),dest)

        # Print the df to the terminal
        print(df)

        # Using sqlalchemy to make the db connection
        # User, pw, and db are being imported from databaseconfig file to mask credentials
        con = sq.create_engine("mysql+pymysql://{user}:{pw}@localhost/{db}"
                                .format(user=cfg.mysql["user"],
                                        pw=cfg.mysql["passwd"],
                                        db=cfg.mysql["db"]))

        # Insert the dataframe into the MySQL database table 'acct_activity'
        # use if_exists argument to 'replace' if you want to drop the table and replace
        # use if_exists argument to 'append' if you want to append new data to existing data
        df.to_sql("acct_activity", con, if_exists='append')

        rowcount = format(len(df.index))
        filecount = format(filecount)
        db = format(cfg.mysql["db"])

        print("SUCCESS: " + rowcount + " rows of data from " + filecount + " files imported to the " + db + " database.")


        
                
                

                






