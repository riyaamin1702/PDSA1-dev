from io import StringIO
import os 
import pandas as pd
from collections import OrderedDict
from aflutil import helper
import re 

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
#-------------------
	

def process_teams (filePath):
    data_array= []
    with open(filePath,'r') as f:
        for line in f:             
            fields = line.split('|')
             
            if fields[0] not in " Rnd ":
                pass
            else:
                v=fields[1:14]
                data_array.append(v)
                # print(mList)
        return data_array 
                
	
            
			
			
			
     
    
for i in mardown_files:
     #readFiles = helper.read_input_file_names( location + i)
	process_teams(location+i)