from aflutil import helper

''' 
A function to compute a final scored based on the traditional
per quarter score format used by the AFL. Columns 7 and 5 will
contain something like '1.0 1.4 4.5 5.8'. These map to the 
four quarters and are cumulative. So '5.8' means the team
scored 5 goals worth 6 points each and had 8 behinds for 
1 point each, which should sum up to 38. So the function
should simply take a scoring row and return the final
score for that field. This is not as easy as it looks.
You need to split on spaces and then again on '.'. Once
You have the goals and behinds from the string, you need
to cast them to an integer to do any computations with
them.
'''
def compute_score(S):
  
  ''' 
  TODO by you. Return the correct score as described
  above. 
  '''

  return result

'''
Once you can compute a score using a scoring field,
you can validate every score, win/loss/tie, and score
difference in the raw data. The function should take
the data array, and validate columns 6,8,10,11 of every
row, which are For Final Score, Against Final Score, Result,
and Margin respectively. If a row is incorrect, you should
correct it. So the function accepts the data_array and
returns a modified data array that should have 100% of the
statistics correct.
'''
def validate_all_scores (data_array):

  ''' 
  TODO by you. The input is the original data_array and
  the return value is the corrected data array. 
  '''

  return data_array

'''
The main fuction calls. These should not be modified in
your final version so be careful if you change anything
here.
'''

if __name__ == "__main__":
  output_dir = 'results/'
  error_log = 'results/error.log'
  teams_file = 'data/teams.in'
  input_array_file = 'results/array-initial.tsv'
  output_array_file = 'results/array-updated.tsv'

  helper.create_results_dir(output_dir)
  helper.zero_error_log(error_log)
  data_array = helper.load_tsv_file(input_array_file)
  data_array = validate_all_scores(data_array)
  helper.print_array(data_array,output_array_file)

