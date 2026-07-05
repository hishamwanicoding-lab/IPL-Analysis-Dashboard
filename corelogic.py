#CREATING IPL PLAYER ANALYSIS DASHBOARD 
"""
=========================================
         MAIN DASHBOARD
=========================================
"""
def maindashboard():
   while True:
      try:
       print("1 Tournament statisics")
       print("2 Team statistics")
       print("3 Player statistics")
       print("4 search")
       print("5 Exit ")
       #taking choice input 
       choice=int(input("Enter your choice "))
       if choice==1:
         tournamentdashboard()
       elif choice==2:
         teamdashboard()
       elif choice==3:
         playersdashboard()
       elif choice==4:
         searchdashboard()
       elif choice==5:
         break
       else: 
         print("invalid choice")
      except ValueError:
         print("enter numbers only ")
      except FileNotFoundError:
         print("csv file is missing ")
"""
==========================================
         PLAYER STATISTICS
=========================================1. Player Statistics
2. Most Runs
3. Most Wickets
4. Most Sixes
5. Most Fours
6. Highest Strike Rate
7. Highest Batting Average
8. Lowest Economy
9. Top 5 Run Scorers
10. Top 5 Wicket Takers
11. Back
==================================
     Players dashboard
==================================

"""

def playersdashboard():
   while True:
    try:
     print("2 Top Run Scorer")
     print("3 Top Wicket Taker")
     print("4 Highest Batting Average")
     print("5 Highest Strike Rate")
     print("6 Most Catches ")
     print("7 Back")
    #taking choice input 
     choice=int(input("enter your choice"))
     if choice==2:
          toprunscorer()
     elif choice==3:
         topwickettaker()
     elif choice==4:
       highestbattingaverage()
     elif choice==5:
       higheststrikerate()
     elif choice==6:
       mostcatches()
     elif choice==7:
       break
     else:
       print("Enter Valid Choice")
    except ValueError:
       print("enter numbers only")
       """
       ====================================

       CREATING PLAYER FUNCTIONS 
       ====================================
       
        
       
       """

#defining highest batting average function
def highestbattingaverage():
   highest=float("-inf")
   with open("players.csv") as file:
      import csv
      dictreader=csv.DictReader(file )
      for rows in dictreader:
         if float(rows["average"])>highest:
            highest=float(rows["average"])
   return(highest)
#creating a function for top run scorrers 
def toprunscorer():
   maxruns=0
   topplayer=""
   #importing csv
   import csv
   with open("players.csv") as file:
      dictplayer=csv.DictReader(file)
      for rows in dictplayer:
         if int(rows["runs"])>maxruns:
            maxruns=int(rows["runs"])
            topplayer=rows["player_name"]
      return(topplayer)
#defining a function for top witcket taker 
def topwickettaker():
   wickets=0
   topplayer=""
   import csv
   with open("players.csv") as file:
     dictreader=csv.DictReader(file)
     for rows in dictreader:
        if int(rows["wickets"])>wickets:
           wickets=int(rows["wickets"])
           topplayer=rows["player_name"]
     return(topplayer)

#defining a function for highest  batting average 
def bestbattingaverage():
   bestaverage=float("-inf")
   bestplayer=""
   with open("players.csv") as file:
      import csv
      dictreader=csv.DictReader(file )
      for rows in dictreader:
         if float(rows["average"])>bestaverage:
            bestaverage=float(rows["average"])
      return(bestaverage)

#definging a function for highest strike rate 
def higheststrikerate():
   highest=float("-inf")
   with open("players.csv")as file :
      import csv
      dictreader=csv.DictReader(file)
      for rows in dictreader:
         if float(rows["strike_rate"])>highest:
            highest=float(rows["strike_rate"])
      return(highest)
#definging a function for most catches 
def mostcatches():
   mostcatches=float("-inf")
   player=""
   import csv
   with open("players.csv")as file :
    dictreader=csv.DictReader(file)
    for rows in dictreader:
       if float(rows["catches"])>mostcatches:
          mostcatches=float(rows["catches"])
          player=rows["player_name"]
   return(player)

#defining a function for team statistics
"""
------ TEAM Dashboard------
1. Total Runs
2. Total Wickets
3. Average Strike Rate
4. Average Batting Average
5. Average Economy
6. Highest Run Scorer
7. Highest Wicket Taker
8. Team Squad
9. Back
"""
"""
==============================================

CREATING TEAM DASHBOARD
==============================================
"""
def teamdashboard():
   while True:
      try:
       print("1  Total Runs ")
       print("2  Total Wickets ")
       print("3. Average Strike Rate")
       print("4. Average Batting Average")
       print("5. Average Economy")
       print("6. Highest Run Scorer")
       print("7. Highest Wicket Taker")
       print("8. Team Squad")
       print("9. Back")
       choice=int(input("enter your choice "))
       if choice==1:
         teamruns()
       elif choice==2:
         teamwickets()
       elif choice==3:
         averageteamstrikerate()
       elif choice==4:
         averagebattingaverage()
       elif choice==5:
         averagebattingeconomy()
       elif choice==6:
         highestrunscrorer()
       elif choice==7:
         highestwickettaker()
       elif choice==8:
         teamplayers()
       elif choice==9:
         break
       else:
         print("enter valid choice")
      except ValueError:
         print("enter numbers only ")
#defining function to show team runs 
def teamruns():
   team=input(" enter team name to see runs scored" )
   separateruns=[]
   import csv
   with open("players.csv") as file :
      dictreader=csv.DictReader(file)
      for rows in dictreader:
         if rows["team"].replace(" ","").lower()==team.replace(" ","").lower():
            separateruns.append(int(rows["runs"]))
         else:
            continue
   import numpy as np
   separateruns=np.array(separateruns)
   totalruns=np.sum(separateruns)
   return(totalruns)            
#defining a fucntion to show team witckets 
def teamwickets():
   team=input( "Enter team  for wickets taken" )
   playerwickets=[]
   found=False
   with open("players.csv")as file:
      import csv
      import numpy as np
      dictreader=csv.DictReader(file)
      for dicts in dictreader:
         if team.replace(" ","").lower()==dicts["team"].replace(" ","").lower():
            found=True 
            playerwickets.append(int(dicts["wickets"]))
         if not found:
            return("Enter a valid team")
            #creating an array
   playerwickets=np.array(playerwickets)
   totalwickets=np.sum(playerwickets) 
   return(totalwickets)
#creating a function to calculate average strike rate of team
def averageteamstrikerate():
   team=input("Enter Team Name ")
   playerstrikerate=[]
   found=False
   #reading csv file
   with open ("players.csv") as file :
      import csv
      dictreader =csv.DictReader(file)
      for dicts in dictreader:
       if team.replace(" ","").lower()==dicts["team"].replace(" ","").lower():
         found=True
         playerstrikerate.append(float(dicts["strike_rate"]))
   if not found:
         return("Enter a valid Team")
      #now   averaging strikerates using numpy mean
   import numpy as np 
   arrplayerstrikerate=np.array(playerstrikerate)
      #now taking averages 
   averageteamstrikerate=np.mean(arrplayerstrikerate)
   return(averageteamstrikerate)
#defining an function for defining average team players batting average 
def averagebattingaverage():
   team=input("Enter team ")
   found=False
   playerbattingaverge=[]
   #opening a file 
   with open("players.csv") as file:
      import csv
      #reading 
      dictreader=csv.DictReader(file)
      for dicts in dictreader:
         if team.replace(" ","").lower()==dicts["team"].replace(" ","").lower():
            found=True
            playerbattingaverge.append(float(dicts["average"]))
   if not found:
            return("Enter valid team")
      #now averageing playerbattingaverges 
   import numpy as np
   arrayplayerbattingaverge=np.array(playerbattingaverge)
   averagebattingaverage=np.mean(playerbattingaverge)
   return(averagebattingaverage)
#creating a function for average batting economy 
def averagebattingeconomy():
   team=input("Enter team name ")
   found=False
   averageplayereconomy=[]
   #now reading csv files in dicts rows
   with open("players.csv") as file:
      import csv
      dictreader=csv.DictReader(file)
      for dicts in dictreader:
         if team.replace(" ","").lower()==dicts["team"].replace(" ","").lower():
            found=True
            averageplayereconomy.append(float(dicts["economy"]))
   if not found:
         return("Enter valid team")
      #now using numpy for averaging players economy
   import numpy as np
   arraverageplayereconomy=np.array(averageplayereconomy)
   averagebattingeconomy=np.mean(arraverageplayereconomy)
   return(averagebattingeconomy)
#creating a function for highest run scorer of team 
def highestrunscrorer():
   team=input("Enter team name ")
   found=False
   runs=[]
   highestrunscrorer=""
   #reading csv file 
   with open("players.csv") as file :
      import csv
      dictreader=csv.DictReader(file)
      for dicts in dictreader:
         if team.replace(" ","").lower()==dicts["team"].replace(" ","").lower():
            found=True
            runs.append(int(dicts["runs"]))
      if not found:
            return("Enter a valid team")
         #now using numpy
      import numpy as np
      arrruns=np.array(runs)
      highestruns=np.max(arrruns)
      #opening file again 
      with open("players.csv")as file :
       import csv 
       dictreader=csv.DictReader(file)
       for dicts in dictreader:
        if team.replace(" ","").lower()==dicts["team"].replace(" ","").lower():
           if int(dicts["runs"])==highestruns:
            highestrunscrorer=dicts["player_name"]
      return(highestrunscrorer)
#defining a function for highest witcket taker 
def highestwickettaker():
   team=input("Enter team name ")
   found=False
   highestwickets=0
   highestwitckettaker=""
   #reading csv file 
   with open("players.csv")as file :
      import csv 
      dictreader=csv.DictReader(file)
      for dicts in dictreader:
         if team.replace(" ","").lower()==dicts["team"].replace(" ","").lower():
            found=True
            if int(dicts["wickets"])>int(highestwickets):
               highestwickets=int(dicts["wickets"])
               highestwitckettaker=dicts["player_name"]
      if not found:
               return("Enter a valid team")
   return(highestwitckettaker)
#defing function to show team players
def teamplayers():
    teamname=input("Enter team name") 
    playersname=[]
    import csv
    with open("players.csv") as file:
      dictplayer=csv.DictReader(file)
      #now 
      for rows in dictplayer:
         if rows["team"].replace(" ","").lower()==teamname.replace(" ","").lower():
            playersname.append(rows["player_name"])
             
         else:
            continue
      return(playersname)

"""
==========================================
      TOURNAMENT STATISTICS
==========================================
Total players 
Total Teams 
Team with lowest economy
Team with most sixes
Team with best batting average
Team with most wickets
Top 5 run scorers
Top 5 wicket takers
======================
team dashboard 
==========================
"""
def tournamentdashboard():
   while True:
      try:
       print("1 Total Players")
       print("2 Total Teams ")
       print("4 Team with lowest economy")
       print("6 Team with best batting average ")
       print("7 Team with most wickets ")
       print("8 Top five run scrorer ")
       print("9 Top five wicket takers ")
       print("10 Back")
       #taking choice input 
       choice=int(input("enter choice "))
       if choice==1:
        totalplayers()
       elif choice==2:
        totalteams()
       elif choice ==4:
        teamlowesteconomy()
       elif choice==6:
         teammostsbattingaverage()
       elif choice==7:
         teamwithmostwickets()
       elif choice==8:
         topfiverunscrorers()
       elif choice==9:
         topfivewickettakers()
       elif choice==10:
            break
       else:
         print("print valid choice ") 
      except ValueError:
       print("enter numbers only ")
#now defining tournoment functions 
#defining a function for total players
def totalplayers():
   playercount=0
   with open("players.csv") as file :
      import csv
      dictreader=csv.DictReader(file)
      for dicts in dictreader:
         playercount=playercount+1
   return(playercount)
#define a function for total teams 
def totalteams():
   Teamcount=0
   with open("teams.csv") as file:
      import csv
      dictreader=csv.DictReader(file)
      for dicts in dictreader:
         Teamcount=Teamcount+1
   return(Teamcount)
#creating a function for team with lowest economy
def teamlowesteconomy():
   import numpy as np
   arr=np.genfromtxt("players.csv",
                      dtype=str,
                      delimiter=",",
                      skip_header=1)
   #now
   economy=arr[:,11].astype(float)
   rowindex=np.argmin(economy)
   teamwithlowesteconomy=arr[rowindex,2]
   lowesteconomy=economy[rowindex]
   return(f"{teamwithlowesteconomy} has lowest economy of {lowesteconomy}")
#defining a function for team with most batting average 
def teammostsbattingaverage():
   import numpy as np
   arr=np.genfromtxt("players.csv",
                     dtype=str,
                     delimiter=",",
                     skip_header=1)
   #now 
   averages=arr[:,8].astype(float)
   rowindex=np.argmax(averages)
   teamwithmostbattingaverage=arr[rowindex,2]
   mostbattingaverage=averages[rowindex]
   return(f"{teamwithmostbattingaverage} has best batting average of {mostbattingaverage}")
#defing a function for team with most wickets
def teamwithmostwickets():
   import numpy as np
   arr=np.genfromtxt("players.csv",
                  dtype=str,
                  delimiter=",",
                  skip_header=1)
   wickets=arr[:,9].astype(int)
   rowindexofmostwickers=np.argmax(wickets)
   teamwithmostwickets=arr[rowindexofmostwickers,2]
   mostwickets=wickets[rowindexofmostwickers]
   return(f"{teamwithmostwickets} has most wickets {mostwickets}")
#define a function for top five run scrorers
def topfiverunscrorers():
   import numpy as np
   arr=np.genfromtxt("players.csv",
                     delimiter=",",
                     dtype=str,
                     skip_header=1)        
    #now 
   runs=arr[:,5].astype(int)
   top5indices=np.argsort(runs)[-5:len(runs):1][::-1]
   result=[]
   for indexes in top5indices:
    result.append(f"{runs[indexes]}:{arr[indexes,1]}")
   return(result)
#defining a function for top five wickettakers
def topfivewickettakers():
   result=[]
   import numpy as np
   arr=np.genfromtxt("players.csv"
                     ,dtype=str,
                     delimiter=",",
                     skip_header=1)
   wickets=arr[:,9].astype(int)
   topfivewicketindexes=np.argsort(wickets)[-5:len(wickets):1][::-1]
   for indexes in topfivewicketindexes:
      result.append(f"{arr[indexes,1]}:{wickets[indexes]}")
   return(result)
""""
================================================

searching  DASHBOARD 

================================================
"""""
def searchdashboard():
   while True:
    try:
     print("1 Search player ")
     print("2 search team ")
     print("3 Search match")
     print("4 Back")
     choice=int(input("Enter choice"))
     if choice==1:
       searchplayer()
     elif choice==2:
       searchteam()
     elif choice==3:
      searchmatch()
     elif choice==4:
         break
     else:
         print("enter valid choice ")
    except ValueError:
       print("enter numbers only")
# defining search player function
def searchplayer():
  try:
     player=input( "Enter the players name")
     #now imporing csv
     import csv 
     with open("players.csv")as file :
        reader=csv.DictReader(file)
        for row in reader:
         if row["player_name"].strip().replace(" ","").lower()==player.strip().replace(" ","").lower():
            return(row)
  except FileNotFoundError:
   print("file not found")
#defining search team function 
def searchteam():
   try:
    team=input("Enter team you want to enter")
    with open("teams.csv")as file:
      import csv
      dictreader=csv.DictReader(file )
      for dicts in dictreader:
         if team.strip().replace(" ","").lower()==dicts["teamname"].strip().replace(" ","").lower():
            return(dicts)
   except FileNotFoundError:
     print("csv file missing ")
#defining a function for match function 
def searchmatch():
   try:
    import csv

    team1 = input("Enter team one: ").strip().lower().replace(" ", "")
    team2 = input("Enter team two: ").strip().lower().replace(" ", "")

    with open("matches.csv") as file:
        dictreader = csv.DictReader(file)

        for row in dictreader:

            t1 = row["team1"].strip().lower().replace(" ", "")
            t2 = row["team2"].strip().lower().replace(" ", "")

            # check both directions
            if (team1 == t1 and team2 == t2) or (team1 == t2 and team2 == t1):
              return row 
    return("match not found")
   except FileNotFoundError:
      print("csv file does not exist")