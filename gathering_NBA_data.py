from bs4 import BeautifulSoup
import requests
import sqlite3
import json
import os
from nba_api.stats.static import teams 


def setUpDatabase():
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/'+"NBA_SCORES")
    cur = conn.cursor()
    return cur, conn


def create_table_2021(cur, conn):
    cur.execute("DROP TABLE IF EXISTS Scores_2021")
    cur.execute("CREATE TABLE Scores_2021 (game_id INTEGER PRIMARY KEY, Vistor_Score INTEGER, Home_Score INTEGER, Attendance INTEGER)")
    conn.commit()






def setUpTeamsTable(cur, conn):
    teams_names = []

    url = "https://www.basketball-reference.com/leagues/NBA_2021_games.html"

    r = requests.get(url)

    soup = BeautifulSoup(r.text, 'html.parser')

    
    table = soup.find('table')

    trs = table.find_all('tr')[2:]
    i = 0
    for tr in trs:
        hs = tr.find('td',{'data-stat':'visitor_pts'}).text
        vs = tr.find('td',{'data-stat':'home_pts'}).text
        atten  = tr.find('td', {'data-stat':'attendance'}).text
        cur.execute("INSERT INTO Scores_2021 (game_id, Vistor_Score, Home_Score, Attendance) VALUES (?,?,?,?)", (i, int(vs), int(hs), int(atten.replace(',', ''))))
        i+=1
    conn.commit()

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