import plotly
import plotly.graph_objects as go 
import plotly.express as px
from bs4 import BeautifulSoup
import requests
import re
import os
import csv
import sqlite3
import json

# data from https://www.balldontlie.io/api/v1/games?seasons[]=2019&page={page} and 
# https://www.basketball-reference.com/leagues/NBA_2021_games-{month}.html

#search for each team (JOIN team ID)
#Bar chart avg home team points per game (grouped bar chart)/attendance


import plotly.graph_objects as go
teams = ["Atlanta Hawks", "Boston Celtics", "Brooklyn Nets", "Charlotte Hornets", "Chicago Bulls", "Cleveland Cavaliers",
"Dallas Mavericks", "Denver Nuggets", "Detroit Pistions", "Golden State Warriors", "Houston Rockets", "Indiana Pacers", "Los Angeles Clippers",
"Los Angeles Lakers", "Memphis Grizzlies", "Miami Heat", "Milwaukee Bucks", "Minnesota Timberwolves", "New Orleans Pelicans", "New York Knicks",
"Oklahoma City Thunder", "Orlando Magic", "Philadelphia 76ers", "Phoenix Suns", "Portland Trail Blazers", "Sacramento Kings", "San Antonio Spurs",
"Toronto Raptors", "Utah Jazz", "Washington Wizards"]

fig = go.Figure(data=[
    go.Bar(name='Atlanta Hawks', x=teams, y=[20, 14, 23]),
    go.Bar(name='Boston Celtics', x=teams, y=[12, 18, 29])
])
# Change the bar mode
fig.update_layout(barmode='group')
fig.show()

#df = csv.read_csv("2020_home_ppg.csv")
#df = df[df['team_name'] == "Atlanta Hawks", "Boston Celtics", "Brooklyn Nets", "Charlotte Hornets", "Chicago Bulls", "Cleveland Cavaliers",
"Dallas Mavericks", "Denver Nuggets", "Detroit Pistions", "Golden State Warriors", "Houston Rockets", "Indiana Pacers", "Los Angeles Clippers",
"Los Angeles Lakers", "Memphis Grizzlies", "Miami Heat", "Milwaukee Bucks", "Minnesota Timberwolves", "New Orleans Pelicans", "New York Knicks",
"Oklahoma City Thunder", "Orlando Magic", "Philadelphia 76ers", "Phoenix Suns", "Portland Trail Blazers", "Sacramento Kings", "San Antonio Spurs",
"Toronto Raptors", "Utah Jazz", "Washington Wizards"]
#df = df.groupby(['month', 'team_name'], as_index=False)[['Home_PPG']].avg()
#print (df[:30])

#fig = go.Figure(data=go.Bar(y=[2, 3, 1]))
#fig.write_html('first_figure.html', auto_open=True) 

def main():
    """Returns nothing and takes no inputs. This function selects data from the database in order to create visualizations (two bar charts grouped through plotly) """
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/NBA_SCORES')
    cur = conn.cursor()
    nba_home_chart = px.bar(
        data_frame = df,
        x = "Team",
        y = "Home_PPG",
        color = ("red", "light blue"),
        opacity = 0.92,
        orientation = "v",
        barmode = "group"
    )


#if __name__ == "__main__":
    main()

