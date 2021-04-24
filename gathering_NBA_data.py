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
cur, conn = setUpDatabase()
create_table_2021(cur, conn)