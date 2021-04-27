from bs4 import BeautifulSoup
import requests
import sqlite3
import json
import os
from nba_api.stats.static import teams 

#creates the database, returns cur and conn paramters
def setUpDatabase():
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/'+"NBA_SCORES")
    cur = conn.cursor()
    return cur, conn

#takes in cur and conn, produces empty table for 2021 scores, returns nothing
def create_table_2021(cur, conn):
    cur.execute("DROP TABLE IF EXISTS Scores_2021")
    cur.execute("CREATE TABLE Scores_2021 (game_id INTEGER PRIMARY KEY, Vistor_Score INTEGER, Home_Score INTEGER, Attendance INTEGER)")
    conn.commit()
#takes in cur and conn, produces empty table for 2020 scores, returns nothing
def create_table_2020(cur,conn):

    cur.execute("CREATE TABLE IF NOT EXISTS Scores_2020 (game_id INTEGER PRIMARY KEY, Visitor_id INTEGER, Vistor_Score INTEGER, Home_id INTEGER, Home_Score INTEGER, Page INTEGER)")
    conn.commit()

def create_team_keys_table(cur, conn):
    cur.execute("DROP TABLE IF EXISTS Team_keys")
    cur.execute("CREATE TABLE Team_keys (team_id INTEGER PRIMARY KEY, team_abrv TEXT)")
    conn.commit()







#accepts cur and conn, populates table from beautiful soup/basketball reference, returns nothing
def setUp2021Table(cur, conn):
    months = ['december', 'january', 'february', 'march']
    i = 0
    for month in months:
        url = f"https://www.basketball-reference.com/leagues/NBA_2021_games-{month}.html"

        r = requests.get(url)

        soup = BeautifulSoup(r.text, 'html.parser')

        
        table = soup.find('table')

        trs = table.find_all('tr')[2:]
        for tr in trs:
            hs = tr.find('td',{'data-stat':'visitor_pts'}).text
            vs = tr.find('td',{'data-stat':'home_pts'}).text
            atten  = tr.find('td', {'data-stat':'attendance'}).text
            if atten=='':
                atten = '0'
            cur.execute("INSERT INTO Scores_2021 (game_id, Vistor_Score, Home_Score, Attendance) VALUES (?,?,?,?)", (i, int(vs), int(hs), int(atten.replace(',', '')) ) )
            i+=1
    conn.commit()


#accepts cur and conn, populates table from balldontlie, returns nothing
def setUp2020Table(cur, conn):
    cur.execute("SELECT MAX(Page) FROM Scores_2020")
    
    n = cur.fetchone()[0]
    if(not n):
        n = 0
    page = n+1


    #each page contains exactly 25 game results
    r = requests.get(f"https://www.balldontlie.io/api/v1/games?seasons[]=2019&page={page}")
    games = json.loads(r.text)


    for game in games['data']:


        id_ = game.get('id', 0)
        hs = game.get('home_team_score', 0)
        vs = game.get('visitor_team_score', 0)
        hid = game.get('home_team',None).get('id',0)
        vid = game.get('visitor_team',None).get('id',0)
        cur.execute("INSERT INTO Scores_2020 (game_id , Visitor_id, Vistor_Score, Home_id, Home_Score, Page) VALUES (?,?,?,?,?,?)", (id_, vid, vs, hid, hs, page))

    conn.commit()

#accepts cur and conn, populates table from balldontlie to match team keys to names, returns nothing
def setUpTeamsTable(cur, conn):
    r = requests.get("https://www.balldontlie.io/api/v1/teams")
    teams = json.loads(r.text)


    for team in teams['data']:


        id_ = team.get('id', 0)
        abrv = team.get('abbreviation', None)
        cur.execute("INSERT INTO Team_keys (team_id, team_abrv) VALUES (?,?)", (id_, abrv))

    conn.commit()


    
 


   






#def get_records(cur, conn):




def main():
    cur, conn = setUpDatabase()
    create_team_keys_table(cur,conn)
    create_table_2020(cur, conn)
    setUp2020Table(cur, conn)
    create_table_2021(cur, conn)
    setUp2021Table(cur, conn)
    setUpTeamsTable(cur, conn)

if __name__ == "__main__":
    main()
