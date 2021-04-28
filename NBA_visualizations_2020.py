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

#Grouped Bar Chart for 2020 Home court PPG averages for all NBA teams

teams = ["NBA Team"]

fig = go.Figure(data=[
    go.Bar(name='Atlanta Hawks', x=teams, y=[114.58823529411765], marker_color = 'rgb(225,68,52)'),
    go.Bar(name='Boston Celtics', x=teams, y=[117.05714285714286], marker_color = 'rgb(0,122,51)' ),
    go.Bar(name='Brooklyn Nets', x=teams, y=[112.38888888888889], marker_color = 'rgb(0,0,0)'),
    go.Bar(name='Charlotte Hornets', x=teams, y=[104.2258064516129], marker_color = 'rgb(29,17,96)'),
    go.Bar(name='Chicago Bulls', x=teams, y=[106.11764705882354], marker_color = 'rgb(206,17,65)'),
    go.Bar(name='Clevland Cavaliers', x=teams, y=[108.55555555555556], marker_color = 'rgb(134,0,56)'),
    go.Bar(name='Dallas Mavericks', x=teams, y=[117.71052631578948], marker_color = 'rgb(0,83,188)'),
    go.Bar(name='Denver Nuggets', x=teams, y=[111.86111111111111], marker_color = 'rgb(13,34,64)'),
    go.Bar(name='Detroit Pistons', x=teams, y=[109.3030303030303], marker_color = 'rgb(200,16,46)'),
    go.Bar(name='Golden State Warriors', x=teams, y=[106.97058823529412], marker_color = 'rgb(29,66,138)'),
    go.Bar(name='Houston Rockets', x=teams, y=[119.0], marker_color = 'rgb(206,17,65)'),
    go.Bar(name='Indiana Pacers', x=teams, y=[110.75], marker_color = 'rgb(0,45,98)'),
    go.Bar(name='Los Angeles Clippers', x=teams, y=[117.76470588235294], marker_color = 'rgb(200,16,46)'),
    go.Bar(name='Los Angeles Lakers', x=teams, y=[113.58823529411765], marker_color = 'rgb(85,37,130)'),
    go.Bar(name='Memphis Grizzlies', x=teams, y=[113.19444444444444], marker_color = 'rgb(93,118,169)'),
    go.Bar(name='Miami Heat', x=teams, y=[115.75], marker_color = 'rgb(152,0,46)'),
    go.Bar(name='Milwaukee Bucks', x=teams, y=[120.97222222222223], marker_color = 'rgb(0,71,27)'),
    go.Bar(name='Minnesota Timberwolves', x=teams, y=[110.125], marker_color = 'rgb(12,35,64)'),
    go.Bar(name='New Orleans Pelicans', x=teams, y=[117.58333333333333], marker_color = 'rgb(0,22,65)'),
    go.Bar(name='New York Knicks', x=teams, y=[105.39393939393939], marker_color = 'rgb(0,107,182)'),
    go.Bar(name='Oklahoma City Thunder', x=teams, y=[113.16666666666667], marker_color = 'rgb(239,59,36)'),
    go.Bar(name='Orlando Magic', x=teams, y=[106.05714285714286], marker_color = 'rgb(0,125,197)'),
    go.Bar(name='Philadelphia 76ers', x=teams, y=[113.44117647058823], marker_color = 'rgb(237,23,76)'),
    go.Bar(name='Phoenix Suns', x=teams, y=[114.48717948717949], marker_color = 'rgb(29,17,96)'),
    go.Bar(name='Portland Trail Blazers', x=teams, y=[117.33333333333333], marker_color = 'rgb(224,58,62)'),
    go.Bar(name='Sacramento Kings', x=teams, y=[110.37142857142857], marker_color = 'rgb(91,43,130)'),
    go.Bar(name='San Antonio Spurs', x=teams, y=[114.73529411764706], marker_color = 'rgb(196,206,211)'),
    go.Bar(name='Toronto Raptors', x=teams, y=[114.97142857142858], marker_color = 'rgb(206,17,65)'),
    go.Bar(name='Utah Jazz', x=teams, y=[111.48571428571428], marker_color = 'rgb(0,71,27)'),
    go.Bar(name='Washington Wizards', x=teams, y=[114.0], marker_color = 'rgb(0,43,92)'),
])
# To alter bar presentation
fig.update_layout(barmode='group')
fig.update_layout(title_text='NBA 2020 Pre-COVID-19 Home Team PPG Averages')
fig.show()

#df = csv.read_csv("2020_home_ppg.csv")
#df = df[df['team_name'] == "Atlanta Hawks", "Boston Celtics", "Brooklyn Nets", "Charlotte Hornets", "Chicago Bulls", "Cleveland Cavaliers",
#"Dallas Mavericks", "Denver Nuggets", "Detroit Pistions", "Golden State Warriors", "Houston Rockets", "Indiana Pacers", "Los Angeles Clippers",
#"Los Angeles Lakers", "Memphis Grizzlies", "Miami Heat", "Milwaukee Bucks", "Minnesota Timberwolves", "New Orleans Pelicans", "New York Knicks",
#"Oklahoma City Thunder", "Orlando Magic", "Philadelphia 76ers", "Phoenix Suns", "Portland Trail Blazers", "Sacramento Kings", "San Antonio Spurs",
#"Toronto Raptors", "Utah Jazz", "Washington Wizards"]
#df = df.groupby(['month', 'team_name'], as_index=False)[['Home_PPG']].avg()
#print (df[:30])

#fig = go.Figure(data=go.Bar(y=[2, 3, 1]))
#fig.write_html('first_figure.html', auto_open=True) 

#def main():
    #"""Returns nothing and takes no inputs. This function selects data from the database in order to create visualizations (two bar charts grouped through plotly) """
   # path = os.path.dirname(os.path.abspath(__file__))
    #conn = sqlite3.connect(path+'/NBA_SCORES')
    #cur = conn.cursor()
    #nba_home_chart = px.bar(
        #data_frame = df,
        #x = "Team",
       # y = "Home_PPG",
        #color = ("red", "light blue"),
        #opacity = 0.92,
       # orientation = "v",
       # barmode = "group"
    #)


#if __name__ == "__main__":
    #main()

