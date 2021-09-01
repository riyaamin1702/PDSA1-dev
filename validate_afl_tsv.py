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
  
  result = []
  for i in S:
    
    Total_Split        = i.split()
    last_Quater        = Total_Split[3]
    last_Quater_Split  = last_Quater.split('.')
    mulSix             = int(last_Quater_Split[0])*6
    mulOne             = int(last_Quater_Split[1])
    total_Score        = mulSix + mulOne
    total_Str = ' '+ str(total_Score)+' '
    result.append(total_Str)
    
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
  
  for line in data_array:
      
      home_Total = line[5] #3
      away_Total = line[7] #5
      
      def_compute_score = [home_Total, away_Total]  
      computeScore = compute_score(def_compute_score)
      
      val_For_Total = line[6] #4
      val_Against_Total = line[8] #6
      margin = line[10] #8 
      result = line[9] #7
      
      # For_Total Validation and Update
      if(computeScore[0] != line[6]):
        line[6] = computeScore[0]
        #print(f"Incorrect value found in Round {line[0]} during For_Total validation. The incorrect value was {val_For_Total} and it has been updated to {line[4]}")
      
      # Against_Total Validation and Update
      if(computeScore[1] != line[8]):
        line[8] = computeScore[1]
        #print(f"Incorrect value found in Round {line[0]} during Against_Total validation. The incorrect value was {val_Against_Total} and it has been updated to {line[6]}")
      
      computed_Total = (int(computeScore[0]) - int(computeScore[1])) 
      md_conv_Total = ' '+str(computed_Total)+' '
      
      
      # Margin validation and Update
      if(md_conv_Total != line[10]):
        line[10] = md_conv_Total
        #print(f"Incorrect value found in Round {line[0]} during Margin validation. The incorrect value was {margin} and it has been updated to {line[8]}")
      
      
      # Result validation and update 
      if (computed_Total > 0):
        win_Result = ' W '
        if(win_Result != line[9]):
          line[9] = win_Result
          #print(f"Incorrect value found in Round {line[0]} during Result validation. The incorrect value was {result} and it has been updated to {line[7]}")
      elif(computed_Total < 0):
        lose_Result = ' L '
        if(lose_Result != line[9]):
          line[9] = lose_Result
          #print(f"Incorrect value found in Round {line[0]} during Result validation. The incorrect value was {result} and it has been updated to {line[7]}")
      else:
        draw_result = ' D '
        if(draw_result != line[9]):
          line[9] = draw_result
          #print(f"Incorrect value found in Round {line[0]} during Result validation. The incorrect value was {result} and it has been updated to {line[7]}")

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

