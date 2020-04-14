import random
class Hangman:
  data = ['python', 'java', 'kotlin', 'javascript'] 
  letter_data = []
  sel_word = []
  sel__word_repr = []
  letter = ''
  LIFE = 8
  state = True

  def __init__(self):
    self.sel_word = list(random.choice(self.data))
    self.sel_word_repr = list(''.join(['-' for i in range(len(self.sel_word))]))
    self.concatenation()
    self.game()
  
  def input_letter(self):
    self.letter = input('Input a letter: ')

  def check_letter(self):
    if len(self.letter) == 1:
      if self.letter.islower():
        if self.letter in self.letter_data:
          print('You already typed this letter')
        else:
          if self.letter in self.sel_word:
            for n, i in enumerate(self.sel_word):
              if i == self.letter:
                self.sel_word_repr[n] = i
          else:
            print('No such letter in the word')
            self.LIFE -= 1
      else:
        print('It is not an ASCII lowercase letter') 
    else:
      print('You should print a single letter')
    self.letter_data.append(self.letter)

  def check_win(self):
    if self.LIFE == 0 and self.sel_word_repr != self.sel_word:
      print('You are hanged!')
      self.state = False
    elif self.sel_word_repr == self.sel_word:
      print('You guess the word!\nYou survived!')
      self.state = False

  def concatenation(self):
    print(''.join([a for a in self.sel_word_repr]))
    self.game()

  def game(self):
    while self.state:
      self.input_letter()
      self.check_letter()
      self.check_win()
      if self.state == True:
        print()
        self.concatenation()
        
game = Hangman()
print('H A N G M A N\n')
while True:
  var = input('Type "play" to play the game, "exit" to quit:')
  if var == 'game':
    game = Hangman()
  elif var == 'exit':
    break
