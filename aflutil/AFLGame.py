
''' 
This class is used only for the final challenge problem where
you must find the five biggest home wins and losses.
'''    
class AFLGame:

  def __init__(self, team, opponent, year, difference, totalfor, totalagainst):
    self.team = team
    self.opponent = opponent
    self.year = year
    self.difference = difference
    self.totalfor = totalfor
    self.totalagainst = totalagainst

  def __str__(self):
    return self.team + '-' + self.opponent + ' (' + self.year + ') : '  + self.totalfor + '-' + self.totalagainst + '\n'

