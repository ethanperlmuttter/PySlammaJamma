#By Chris Hudson and Ethan Perlmutter
from gathering_NBA_data import setUpDatabase
from gathering_NBA_data import setUp2020Table
from gathering_NBA_data import create_table_2020

#gathers first 40 pages of 2020 season (pre-COVID)
def repeat_gather():
    cur, conn = setUpDatabase()
    create_table_2020(cur, conn)
    for i in range(40):
        setUp2020Table(cur, conn)

repeat_gather()

#


