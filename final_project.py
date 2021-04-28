#By Chris Hudson and Ethan Perlmutter
from gathering_NBA_data import setUpDatabase
from gathering_NBA_data import setUp2020Table
from gathering_NBA_data import create_table_2020
import gathering_NBA_data
import NBA_homecourt
import NBA_visualizations_2020
import NBA_visualizations_2021
import os

#gathers first 40 pages of 2020 season (pre-COVID)

def repeat_gather():
    cur, conn = setUpDatabase()
    create_table_2020(cur, conn)
    for i in range(40):
        setUp2020Table(cur, conn)

os.system('python3 gathering_NBA_data.py')
repeat_gather()
os.system('python3 NBA_homecourt.py')
os.system('python3 NBA_visualizations_2020.py')
os.system('python3 NBA_visualizations_2021.py')

#


