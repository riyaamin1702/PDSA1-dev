from aflutil import helper
from aflutil import AFLGame 
import heapq

'''
The final challenge is to walk the corrected data and return the five
biggest home wins and losses in the dataset. Use the AFLGames class 
for this one. Create a list of games with their scores. Once you have
the list, you can apply the function heapq.nlargest as discussed in the
lectorial to find final results. There are other ways, but this one
should be straightforward if you understand the example we show.
'''
 #Key for the AFL Game objects
def sortkey(AFLGame):
     return AFLGame.difference

def find_biggest_wins (data_array,where):
  topfive = []
  
  afl_list = []
  for line in data_array:
   team = line[0]
   opponent = line[4]
   year = line[1]
   difference = line[10]
   totalfor = line[6] 
   totalagainst = line[8]
  
   game = AFLGame.AFLGame(team, opponent, year, difference, totalfor, totalagainst)
   afl_list.append(game)
    
   topfive = heapq.nlargest(5, afl_list, key=sortkey)
  return topfive


if __name__ == "__main__":
    input_array = 'results/array-updated.tsv'
    output_file = 'resultsb /bigwins.txt'

    data_array = helper.load_tsv_file(input_array) 
    home_wins = find_biggest_wins (data_array,'H')
    away_wins = find_biggest_wins (data_array,'A')
    helper.write_top_five (home_wins, away_wins,output_file)
