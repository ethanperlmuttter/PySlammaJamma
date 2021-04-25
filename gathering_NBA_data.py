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



def create_table_2021(cur, conn):
    cur.execute("DROP TABLE IF EXISTS Scores_2021")
    cur.execute("CREATE TABLE Scores_2021 (game_id INTEGER PRIMARY KEY, Visitor_Team TEXT, Vistor_Score INTEGER, Home_Team TEXT, Home_Score INTEGER, Attendance INTEGER)")
    conn.commit()




def get_scores(year, cur, conn):
    url = f"https://www.basketball-reference.com/leagues/NBA_{year}_games.html"

    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    table = soup.find('table')
    rows = table.find_all('tr')
    print(rows)
    count = 0
    for row in rows:
        vis_team = row.find_all('td', class_ = "left")#[0].find('a').text
        print(vis_team)
        home_team = row.find_all('td', class_ = "left")#[1].find('a').text
        print(home_team)
        vis_score = (row.find_all('td', class_ = "right"))#[1].text)
        home_score = (row.find_all('td', class_ = "right"))#[2].text)
        attendance = (row.find('td', class_ = "right iz").text)
        cur.commit(f"INSERT INTO Scores_2021 (game_id, Visitor_team, Visitor_score, Home_team, Home_score, Attendance) VALUES (?,?,?,?,?,?)", (count, vis_team, vis_score, home_team, home_score, attendance))
        count+=1
    conn.commit






cur, conn = setUpDatabase()
create_table_2021(cur, conn)
get_scores(2021, cur, conn)