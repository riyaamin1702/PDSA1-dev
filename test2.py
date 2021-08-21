
from io import StringIO
import os 
import pandas as pd
from collections import OrderedDict
from pandas.io.formats.format import TextAdjustment
from aflutil import helper
from pandas.io.pytables import Table

spath = 'C:\Users\riyaa\A1\data'
teams_file = 'data/teams.in'
teams_files = helper.read_input_file_names(teams_file)


def process_teams(input_files):
	data_array = []
	with open(input) as f:
		for line in f:
			line = line.strip()
			fields = line.split('|')
			data_array.append(fields)
	return data_array

output_dir = 'results/'
error_log = 'results/error.log'
teams_file = 'data/teams.in'
array_file = 'results/array-initial.tsv'

helper.create_results_dir(output_dir)
helper.zero_error_log(error_log)
teams_files = helper.read_input_file_names(teams_file)
#print (teams_file)
data_array = process_teams(teams_files)
#helper.print_header()
helper.print_array(data_array,array_file)


def process_teams(input_files):
	data_array = []
	for i in input_files:
		with open(i, 'r') as file:
			text = file.read()
			fileText=''
			for t in text:
				fileText += t
				lines = fileText.split('\n')
				for l in lines:
					fields = l.split('|')
					lineList = []
					for f in fields:
						f = f.rstrip()
						lineList.append(f)
					data_array.append(lineList)
	return data_array


	def process_teams(input_files):
	data_array = []
	for i in input_files:
		with open(i, 'r') as file:
			text = file.read()
			fileText=''
			for t in text:
				fileText += t
				lines = fileText.split("\n")
				print(fileText)
				#for l in lines:
				#	fields = l.split('|')
				#	lineList = []
				#	for f in fields:
				#		f = f.rstrip()
				#		lineList.append(f)
				#	data_array.append(lineList)
	return data_array