from aflutil import helper

'''
Main function to implement. To get it working,
you need open in input file in input_files and
walk each line by line. The text files are
cleanly formatted markdown with all data using
the '|' separator. So, each line if not empty
can be split into fields using the split function.
You can keep the data clean by using the strip
operator to remove trailing and leading spaces
in lines and fields.
Your goal is simple -- build a two dimensional
array (list of lists) where every line adheres
to the teams_header, which is 14 columns of data.
You can then convert this to a pandas dataframe
or easily compute and validate simple statistical
data by walking each rown in the list as you will
know what information it should contain.
'''

 # '''The main data array. '''
def process_teams (input_files):
    data_array= []
    for i in input_files:
      with open(i,'r') as f:
        for line in f:
            fields = line.split('|')
            if len(fields)>1:
                v=fields[1:14]
                data_array.append(v)
                # print(mList)
      return data_array 



'''
This is the main function.
You should not modify this unless you
want to print the header in testing.
Make sure to comment it out in your
submission or you'll fail the
test harness.
'''
if __name__ == "__main__":
  output_dir = 'results/'
  error_log = 'results/error.log'
  teams_file = 'data/teams.in'
  array_file = 'results/array-initial.tsv'

  helper.create_results_dir(output_dir)
  helper.zero_error_log(error_log)
  teams_files = helper.read_input_file_names(teams_file)
  data_array = process_teams(teams_files)
  helper.print_header()
  helper.print_array(data_array,array_file)

