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

#API data from https://www.basketball-reference.com/leagues/NBA_2021_games-{month}.html
#Necessary file imports for Plotly file creation
#Grouped Bar Chart for 2021 Home court PPG averages for all NBA teams
#Grouped Bar Chart Plotly creation and line by line bar development for each NBA team, pulling
#home court PPG averages from API gather

teams = ["NBA Team"]

fig = go.Figure(data=[
    go.Bar(name='Atlanta Hawks', x=teams, y=[113.9583404], marker_color = 'rgb(225,68,52)'),
    go.Bar(name='Boston Celtics', x=teams, y=[112.2483405], marker_color = 'rgb(0,122,51)' ),
    go.Bar(name='Brooklyn Nets', x=teams, y=[118.0], marker_color = 'rgb(0,0,0)'),
    go.Bar(name='Charlotte Hornets', x=teams, y=[108.84732344], marker_color = 'rgb(29,17,96)'),
    go.Bar(name='Chicago Bulls', x=teams, y=[109.6555556], marker_color = 'rgb(206,17,65)'),
    go.Bar(name='Clevland Cavaliers', x=teams, y=[108.64333231], marker_color = 'rgb(134,0,56)'),
    go.Bar(name='Dallas Mavericks', x=teams, y=[110.4582], marker_color = 'rgb(0,83,188)'),
    go.Bar(name='Denver Nuggets', x=teams, y=[117.19320232321], marker_color = 'rgb(13,34,64)'),
    go.Bar(name='Detroit Pistons', x=teams, y=[105.849287], marker_color = 'rgb(200,16,46)'),
    go.Bar(name='Golden State Warriors', x=teams, y=[115.76283108], marker_color = 'rgb(29,66,138)'),
    go.Bar(name='Houston Rockets', x=teams, y=[105.67372], marker_color = 'rgb(206,17,65)'),
    go.Bar(name='Indiana Pacers', x=teams, y=[111.74629283820000238], marker_color = 'rgb(0,45,98)'),
    go.Bar(name='Los Angeles Clippers', x=teams, y=[117.1], marker_color = 'rgb(200,16,46)'),
    go.Bar(name='Los Angeles Lakers', x=teams, y=[111.76666667], marker_color = 'rgb(85,37,130)'),
    go.Bar(name='Memphis Grizzlies', x=teams, y=[109.8773737], marker_color = 'rgb(93,118,169)'),
    go.Bar(name='Miami Heat', x=teams, y=[108.45757], marker_color = 'rgb(152,0,46)'),
    go.Bar(name='Milwaukee Bucks', x=teams, y=[119.8382829998], marker_color = 'rgb(0,71,27)'),
    go.Bar(name='Minnesota Timberwolves', x=teams, y=[107.43], marker_color = 'rgb(12,35,64)'),
    go.Bar(name='New Orleans Pelicans', x=teams, y=[116.12223888], marker_color = 'rgb(180,151,90)'),
    go.Bar(name='New York Knicks', x=teams, y=[109.55556], marker_color = 'rgb(0,107,182)'),
    go.Bar(name='Oklahoma City Thunder', x=teams, y=[106.544444], marker_color = 'rgb(239,59,36)'),
    go.Bar(name='Orlando Magic', x=teams, y=[105.87372], marker_color = 'rgb(0,125,197)'),
    go.Bar(name='Philadelphia 76ers', x=teams, y=[116.666767], marker_color = 'rgb(237,23,76)'),
    go.Bar(name='Phoenix Suns', x=teams, y=[116.2424555], marker_color = 'rgb(29,17,96)'),
    go.Bar(name='Portland Trail Blazers', x=teams, y=[114.0], marker_color = 'rgb(224,58,62)'),
    go.Bar(name='Sacramento Kings', x=teams, y=[115.666666667], marker_color = 'rgb(91,43,130)'),
    go.Bar(name='San Antonio Spurs', x=teams, y=[109.000053555], marker_color = 'rgb(196,206,211)'),
    go.Bar(name='Toronto Raptors', x=teams, y=[111.6555553], marker_color = 'rgb(206,17,65)'),
    go.Bar(name='Utah Jazz', x=teams, y=[117.933343435], marker_color = 'rgb(0,71,27)'),
    go.Bar(name='Washington Wizards', x=teams, y=[118.124522], marker_color = 'rgb(0,43,92)'),
])
# To alter bar presentation/add in external features and title text to clarify which year is depicted
fig.update_layout(barmode='group')
fig.update_layout(title_text='NBA 2021 Pre-COVID-19 Home Team PPG Averages')
fig.show()