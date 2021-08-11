from io import StringIO
import os 
import pandas as pd
from collections import OrderedDict
from pandas.io.formats.format import TextAdjustment
from aflutil import helper
from pandas.io.pytables import Table


location = "data/"
mardown_files = []

for file in os.listdir(location):
    try:
        if file.endswith(".md"):
            mardown_files.append(str(file))
    except Exception as e:
        raise e 
        print("No mardown files found")



     #print(readFiles)

# Reading markdown files
#-------------------------------------------------------
    


def process_teams (filePath):
      f = open(filePath, "r")
      
      content = f.read()

      # change new line character from '\r\n' to '\n'
      lines = content.split('|')

      # Remove the first and last 2 lines of the file
      # StringIO can be considered as a file stored in memory
      #df = pd.read_csv(filePath, sep='|', header=teams_header[2])

      # df = pd.read_table(StringIO("".join(lines[2:-2])),sep="|",index_col=0,  header=0)
      #md = pd.DataFrame({"a": [0, 1], "b":[2, 3]}).to_markdown()  
      #print(md)
      #df = pd.read_table('mf.md', sep="|", header=0, index_col=1, skipinitialspace=True).dropna(axis=1, how='all').iloc[1:0]


      
     

    
for i in mardown_files:
     #readFiles = helper.read_input_file_names( location + i)
     process_teams(location+i)


teams_header = OrderedDict(
    Team=0,
    Year=1,
    Round=2,
    Where=3,
    Opponent=4,
    For_Scoring=5,
    For_Total=6, 
    Against_Scoring=7,
    Against_Total=8, 
    Result=9, 
    Margin=10,
    WDL=11,
    Venue=12,
    Crowd=13,
    Date=14)