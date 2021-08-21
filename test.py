from io import StringIO
import os
from typing import Container
from validate_afl_tsv import compute_score 
import pandas as pd
from collections import OrderedDict
from aflutil import helper
import re 

# location = "data/"
# mardown_files = []
# for file in os.listdir(location):
#     try:
#         if file.endswith(".md"):
#             mardown_files.append(str(file))
#     except Exception as e:
#         raise e 
#         print("No mardown files found")

     #print(readFiles)
# Reading markdown files
#-------------------

# list_str = {'Abc.ex', 'Bcd.ex', 'cde.ex', 'def.jpg', 'efg.jpg'}
# new_set = {x.replace('.ex', '').replace('.jpg', '') for x in list_str}
# print(new_set)
	

# def process_teams (filePath):
#     data_array= []
#     with open(filePath,'r') as f:
#         for line in f:             
            
#             fields = line.split('|')
#             v=fields[1:14]
#             try:
#                 skipVar = v[0]
#             except:
#                 continue
#             if skipVar == ' --- ' or skipVar == ' Rnd ' or skipVar == ' Totals ' or skipVar == ' Averages ' :
#                 pass
#             else:
#                 data_array.append(v)
#         print(data_array)
#     return data_array 


# for i in mardown_files:
#      #readFiles = helper.read_input_file_names( location + i)
# 	process_teams(location+i)
        


# workflow 


'''
We have to computer column 5 and 7 and from lines 
and validate against column 


 R1 	 H 	 Fremantle 	(5) 4.4 7.6 9.8 11.14  	 (6)80 	 (7)0.4 3.8 6.9 8.10  	 (8) 58  (9)W 	 (10)22 	 1-0-0 	 M.C.G. 	  21365 	 Sat 20-Mar-2021 1:45 PM 



6 - For_Total
8 - Against_Total 
9 - Result
10 - Margin 


in the above 

if (index[6] > index[8]) then W else L 
and difference of the index 6 and 8 should also be respected 
 
 
end result to compute result and check with above fields and if wrong then update 
'''


result_path = helper.load_tsv_file('results/array-initial.tsv')
def compute_score(result_path):
    

    # for myList in result_path:
    #     for item in myList:
    #         print(item) 
    
    
    for line in result_path:
        line 
        try:
            c5 = line[3]
            
            c5_split    = c5.split(' ')
            c5_endIndex = c5_split[4]
            c5_eISplit  = c5_endIndex.split('.')
            c5_mulSix   = (int(c5_eISplit[0])*6)
            c5_mulOne   = int(c5_eISplit[1])
            c5_total    = c5_mulSix + c5_mulOne
            totalInStrC5 = (c5_total)
            c4_split = line[4].split(' ')
            indexOneC5 = c4_split[1]
            if(totalInStrC5 == indexOneC5):
                validatedC5Total = totalInStrC5
            
            c7 = line[5] 
            
            c7_split    = c7.split(' ')
            c7_endIndex = c7_split[4]
            c7_eISplit  = c7_endIndex.split('.')
            c7_mulSix   = (int(c7_eISplit[0])*6)
            c7_mulOne   = int(c7_eISplit[1])
            c7_total    = c7_mulSix + c7_mulOne
            totalInStrc7 = (c7_total) 
            c6_split = line[6].split(' ')
            indexOneC7 = c6_split[1]
            if(totalInStrc7 == indexOneC7):
                validatedC7Total = totalInStrc7
            
            
            differenceOfTotal = (totalInStrC5 - totalInStrc7)
            
            
            c8_split = line[8].split(' ')
            indexOneC8 = int(c8_split[1])
            
            # if(differenceOfTotal == indexOneC8):
            #     print("True")
            # else: 
            #     print("false")
                
            if(differenceOfTotal > 0):
                c9 = 'W'
            elif(differenceOfTotal < 0):
                c9 = "L"
            else: 
                c9 = "D"
                
            c9_split = line[7].split(' ')
            indexC9 = c9_split[1]
            
            if(indexC9 == c9):
                pass
            else:
                print(c9)
                  

            
        except:
            continue
        line
    
    result = 0

    return result			
			
			
     
    
#compute_score(result_path)
        
def validate_all_scores (data_array):
  for line in data_array:
    if(len(line) > 3):
      home_Total = line[3]
      away_Total = line[5]
      def_computer_score = [home_Total, away_Total]  
      computer_score = compute_score(def_computer_score)
      #print(computer_score)
    
      val_For_Total = line[4] 
      val_Against_Total = line[6]
      #val_Total = [val_For_Total, val_Against_Total]
      #print(val_Total)
      if(computer_score[0] != val_For_Total):
         val_For_Total = computer_score[0]
         
      if(computer_score[1] != val_Against_Total):
        val_Against_Total = computer_score[1] 
         
      diffoftotal = (int(val_For_Total) - int(val_Against_Total))
      diffoftotal1 = str(diffoftotal)
      if(diffoftotal1 != line[8]):
          line[8] = diffoftotal
          
      if(diffoftotal > 0):
          line[8] = 'W'
      elif(diffoftotal < 0):
            line[8] = "L"
      else: 
            line[8] = "D"    
       
  return data_array   