

class TicTacToe:
  combination = []
  pot_winner_combination_list = []
  winner_number = 0

  def __init__(self):
    self.combination = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
  
  def __repr__(self):
    return '---------\n| {} {} {} |\n| {} {} {} |\n| {} {} {} |\n---------'.format(self.combination[0], self.combination[1], self.combination[2], self.combination[3], self.combination[4], self.combination[5], self.combination[6], self.combination[7], self.combination[8])

  def whose_step(self):
    x = 0
    o = 0
    for a in self.combination:
      if a == 'X':
        x += 1
      elif a == 'O':
        o += 1
    if (x - o) == 1:
      return('O')
    else:
      return('X')
      
          
  def new_step(self):
    dictionary = (1, 2, 3)
    while True:
      step  = input('Enter the coordinates: ')
      
      try:
        x_step = int(step.split(' ')[0])
        y_step = int(step.split(' ')[1])

        if 0 < x_step < 4 and 0 < y_step < 4:
          if (x_step, y_step) == (1, 1):
            if self.combination[6] == ' ':
              self.combination[6] = self.whose_step()
              break
            else:
              print('This cell is occupied! Choose another one!')
          elif (x_step, y_step) == (1, 2):
            if self.combination[3] == ' ':
              self.combination[3] = self.whose_step()
              break
            else:
              print('This cell is occupied! Choose another one!')
          elif (x_step, y_step) == (1, 3):
            if self.combination[0] == ' ':
              self.combination[0] = self.whose_step()
              break
            else:
              print('This cell is occupied! Choose another one!')
          elif (x_step, y_step) == (2, 1):
            if self.combination[7] == ' ':
              self.combination[7] = self.whose_step()
              break
            else:
              print('This cell is occupied! Choose another one!')    
          elif (x_step, y_step) == (2, 2):
            if self.combination[4] == ' ':
              self.combination[4] = self.whose_step()
              break
            else:
              print('This cell is occupied! Choose another one!')
          elif (x_step, y_step) == (2, 3):
            if self.combination[1] == ' ':
              self.combination[1] = self.whose_step()
              break
            else:
              print('This cell is occupied! Choose another one!')
          elif (x_step, y_step) == (3, 1):
            if self.combination[8] == ' ':
              self.combination[8] = self.whose_step()
              break
            else:
              print('This cell is occupied! Choose another one!')
          elif (x_step, y_step) == (3, 2):
            if self.combination[5] == ' ':
              self.combination[5] = self.whose_step()
              break
            else:
              print('This cell is occupied! Choose another one!')    
          elif (x_step, y_step) == (3, 3):
            if self.combination[2] == ' ':
              self.combination[2] = self.whose_step()
              break
            else:
              print('This cell is occupied! Choose another one!')
        else:
          print('Coordinates should be from 1 to 3!')

      except:
        print("You should enter numbers!")

  def initial_board(self):
    return '---------\n|       |\n|       |\n|       |\n---------'

  def full_game(self):
    print(self.__repr__())
    while True:
      self.new_step()
      print(self.__repr__())
      result =  self.game()
      if result == 'Impossible':
        break
      elif result == 'X wins':
        break
      elif result == 'O wins':
        break
      elif result == 'Draw':
        break

  def potential_winner_combination(self, input_):
    list_ = []
    a = 0
    b = 0
    for i in range(3):
        list_.append('{}{}{}'.format(input_[a], input_[a + 1], input_[a + 2]))
        list_.append('{}{}{}'.format(input_[b], input_[b + 3], input_[b + 6]))
        a += 3
        b += 1
    # diagonal
    list_.append('{}{}{}'.format(input_[0], input_[4], input_[8]))
    list_.append('{}{}{}'.format(input_[2], input_[4], input_[6]))
    return list_

  def game(self):
    # potential winner list
    self.pot_winner_combination_list = self.potential_winner_combination(self.combination)
    # how many winners in actual potential winner list
    self.winner_number = how_many_winners(self.pot_winner_combination_list)
    if self.winner_number < 1:
      # Game not finished
      if counter_(self.combination,' ') > 1:
        if abs(counter_(self.combination, 'X') - counter_(self.combination, 'O')) <= 1:
            return 'Game not finished'
        elif abs(counter_(self.combination, 'X') - counter_(self.combination, 'O')) > 1:
            print('Impossible')
            return 'Impossible'
      # Impossible
      elif abs(counter_(self.combination, 'X') - counter_(self.combination, 'O')) > 1:
        print('Impossible')
        return 'Impossible'
      # Draw
      elif counter_(self.combination, ' ') == 0:
        print('Draw')
        return 'Draw'
    elif self.winner_number  == 1:
      print('{} wins'.format(winner(self.pot_winner_combination_list)))
      return '{} wins'.format(winner(self.pot_winner_combination_list))
    elif self.winner_number  > 1:
      print('Impossible')
      return 'Impossible'

# transform input string to literals list
def sequence_transform(input_):
    sequence = []
    for liter in range(9):   
      sequence.append(input_[liter])
    return sequence  

# who winner
def winner(potential_winner):
  for pot in potential_winner:
    if pot[0] == pot[1] == pot[2]:
      return pot[0]

# how many literals
def counter_(seq, char_):
  count = 0
  for a in seq:
    if a == char_:
      count +=1
  return count

# how many winners
def how_many_winners(potential):
  winner_counter = 0
  for a in potential:
    if a[0] == a[1] == a[2] and a[0] != ' ':
      winner_counter += 1
  return winner_counter


game = TicTacToe()
game.full_game()
