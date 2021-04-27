import sqlite3
import json
import csv
import os

#accepts nothing, returns nothing, outputs 2020_home_ppg file
def output_file():
    #set up database
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/'+"NBA_SCORES")
    cur = conn.cursor()

    #create file to write
    csvfile = '2020_home_ppg.csv'
    with open(csvfile, 'w') as of:
        of = csv.writer(of, delimiter = ",")
        #create headers
        of.writerow(["Team", "Home_PPG"])


        #joins team keys to hom results
        cur.execute("SELECT * FROM Team_keys JOIN Scores_2020 ON Team_keys.team_id = Scores_2020.Home_id")

        teams = cur.fetchall()
        
        #created dictionary of team abbrv with points ang games
        d = {}
        for tup in teams:
            sum_ = d.get(tup[1], (0,0))[0] + tup[6]
            n = d.get(tup[1], (0,0))[1] + 1

            d[tup[1]] = (sum_, n)
        #converts dictionary entries to file
        for i in d:
            of.writerow([i, (d[i][0]/d[i][1]) ]) 





output_file()

    

       
        

