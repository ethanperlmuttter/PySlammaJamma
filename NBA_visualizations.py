import plotly.graph_objects as go 
import plotly.express as px
import numpy as np
from bs4 import BeautifulSoup
import requests
import re
import os
import csv
import sqlite3
import json 

def main():
     """Returns nothing and takes no inputs. This function selects data from the database in order to create visualizations (a dot plot and two bar charts.) """
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path + '/NBA.db')
    cur = conn.cursor()



if __name__ = "__main__":
    main()

