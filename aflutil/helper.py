import sys
from collections import OrderedDict
import os 
from pathlib import Path

'''
The column header format you want to produce as the
main output. This is a ordered dictionary where the lookup 
value can be used to pull data from a two dimensional
array of all data later.
'''
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
    Date=14
)

'''
Create Results Directory if missing.
'''
def create_results_dir(output_dir):
  try:
    if not os.path.exists(output_dir):
      Path(output_dir).mkdir(parents=True,exist_ok=True)
  except Exception as e:
    eprint ("[ERROR] Could not create output directory.")
    eprint ("[ERROR] with exception: {}".format(str(e)))

'''
Zero error log.
'''
def zero_error_log(error_log):
  with open(error_log,'w') as err_file:
    err_file.write('')

'''
Error print to error log.
'''
def eprint(*args, **kwargs):
  with open('results/error.log','a') as err_file:
    print(*args, file=err_file, **kwargs)
    err_file.write('\n')

'''
Print the header for testing.
Don't include this enabled in your solution.
'''
def print_header ():
  out = []
  for k,v in teams_header.items():
    out.append(k)
  out_str = '\t'.join(out)
  print (out_str)

''' 
Function to create the input file list that
can easily be walked to process all of the
data. 
'''
def read_input_file_names(in_file):
  input_files = []
  with open (in_file,'r') as f:
    for line in f:
      file_name = 'data/' + line.strip()
      input_files.append(file_name)
  return input_files

''' 
Function to print the final array data you have agregated.
'''
def print_array(data_array, array_file):
  with open(array_file,'w') as out_file:
    for row in data_array:
      out_str = '\t'.join(row)
      out_file.write(out_str + '\n')

''' 
Function to create the input file list that
can easily be walked to process all of the
data. 
'''
def read_input_file_names(in_file):
  input_files = []
  with open (in_file,'r') as f:
    for line in f:
      file_name = 'data/' + line.strip()
      input_files.append(file_name)
  return input_files

'''
Load the tsv file as an array
'''
def load_tsv_file(input_file):
	data_array = []
	with open(input_file,'r') as f:
		for line in f:
			line = line.strip()
			fields = line.split('\t')
			data_array.append(fields)
	return data_array

'''
Print the biggest home and away wins to
a results file.
'''
def write_top_five(home_wins, away_wins,output_file):
  with open(output_file,'w') as f:
    f.write('--------------\n')
    f.write('Biggest Home Wins\n')
    f.write('--------------\n')
    for game in home_wins:
      f.write(str(game))
    f.write('\n')
    f.write('--------------\n')
    f.write('Biggest Away Wins\n')
    f.write('--------------\n')
    for game in away_wins:
      f.write(str(game))
    f.write('\n')

