from bs4 import BeautifulSoup
import requests
import sqlite3
import json
import os

def setUpDatabase():
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/'+"NBA_SCORES")
    cur = conn.cursor()
    return cur, conn




def setUpTeamsTable(cur, conn):
    teams_names = []

    url = "https://www.nba.com/standings"

    r = requests.get(url)

    soup = BeautifulSoup(r.text, 'html.parser')

    

    
    print(table)
    
    '''
    '''

    '''
  
    cur.execute("DROP TABLE IF EXISTS Teams")
    cur.execute("CREATE TABLE Categories (id INTEGER PRIMARY KEY, name TEXT)")
    for i in range(len(team_list)):
        cur.execute("INSERT INTO Teams (id,name) VALUES (?,?)",(i,team_list[i]))
    conn.commit()
    '''






#def get_records(cur, conn):





cur, conn = setUpDatabase()

setUpTeamsTable(cur, conn)