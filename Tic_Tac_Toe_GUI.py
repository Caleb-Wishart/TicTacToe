#   TODO
#   

### Imports ###
import tkinter as tk
from sys import stdout
from sys import exit as systemExit
from random import choice

### Class ###
class TicTacToe(tk.Frame):

  ### Functions ###
  # sets up the class wide variables and calls the board setup functions
  def __init__(self, master=None):       
    # Initalisation of program
    super().__init__(master)
    self.master = master
    self.pack()
    ### Class Variables ###
    self.board = {'top_left': ' ', 'top_center': ' ', 'top_right': ' ',\
      'mid_left': ' ', 'mid_center': ' ', 'mid_right': ' ', 'bottom_left': ' ', 'bottom_center': ' ', 'bottom_right': ' '}
    self.button_board = {}
    self.debug_board = {}
    self.positions = [x for x in range(9)]
    self.player_icon = 'X'
    self.computer_icon = 'O'
    self.next_player = ''
    self.gamestate = 'Game Running'


    ### Debugging Tools ###
    self.automated_test_count = 1
    self.debug_options = {'show_computer_moves':False, 'show_game_checks':False, 'random_first_move':False,\
      'debug_output':False, 'run_custom_auto_tests':False, 'custom_auto_tests_amount':0, 'no_cpu':False}

    self.boardFunc()

  # creates the buttons on the board and aligns them to a grid
  def boardFunc(self):
    # Local Variables
    fg_c = 'black'
    bg_c = 'white'
    pad_style = 'ridge'
    pad_x = 3
    pad_y = 3
    # Initalisation of buttons

    # status button
    self.status_button = tk.Button(self,text=self.gamestate,fg='red',relief='raised',state='disabled',width=21)
    self.status_button.grid(columnspan='6',row='0',padx=pad_x,pady=pad_y)

    # Top row
    self.button_board.update({'top_left' : tk.Button(self,text='   ',fg=fg_c,bg=bg_c,relief=pad_style,command=lambda: self.updateBoard('top_left') ) } )
    self.button_board['top_left'].grid(column='0',columnspan='2',row='1',padx=pad_x,pady=pad_y,sticky='E')

    self.button_board.update({'top_center' : tk.Button(self,text='   ',fg=fg_c,bg=bg_c,relief=pad_style,command=lambda: self.updateBoard('top_center') ) } )
    self.button_board['top_center'].grid(column='2',columnspan='2',row='1',padx=pad_x,pady=pad_y)

    self.button_board.update({'top_right' : tk.Button(self,text='   ',fg=fg_c,bg=bg_c,relief=pad_style,command=lambda: self.updateBoard('top_right') ) } )
    self.button_board['top_right'].grid(column='4',columnspan='2',row='1',padx=pad_x,pady=pad_y,sticky='W')

    # middle row
    self.button_board.update({'mid_left' : tk.Button(self,text='   ',fg=fg_c,bg=bg_c,relief=pad_style,command=lambda: self.updateBoard('mid_left') ) } )
    self.button_board['mid_left'].grid(column='0',columnspan='2',row='2',padx=pad_x,pady=pad_y,sticky='E')

    self.button_board.update({'mid_center' : tk.Button(self,text='   ',fg=fg_c,bg=bg_c,relief=pad_style,command=lambda: self.updateBoard('mid_center') ) } )
    self.button_board['mid_center'].grid(column='2',columnspan='2',row='2',padx=pad_x,pady=pad_y)

    self.button_board.update({'mid_right' : tk.Button(self,text='   ',fg=fg_c,bg=bg_c,relief=pad_style,command=lambda: self.updateBoard('mid_right') ) } )
    self.button_board['mid_right'].grid(column='4',columnspan='2',row='2',padx=pad_x,pady=pad_y,sticky='W')

    # bottom row
    self.button_board.update({'bottom_left' : tk.Button(self,text='   ',fg=fg_c,bg=bg_c,relief=pad_style,command=lambda: self.updateBoard('bottom_left') ) } )
    self.button_board['bottom_left'].grid(column='0',columnspan='2',row='3',padx=pad_x,pady=pad_y,sticky='E')

    self.button_board.update({'bottom_center' : tk.Button(self,text='   ',fg=fg_c,bg=bg_c,relief=pad_style,command=lambda: self.updateBoard('bottom_center') ) } )
    self.button_board['bottom_center'].grid(column='2',columnspan='2',row='3',padx=pad_x,pady=pad_y)

    self.button_board.update({'bottom_right' : tk.Button(self,text='   ',fg=fg_c,bg=bg_c,relief=pad_style,command=lambda: self.updateBoard('bottom_right') ) } )
    self.button_board['bottom_right'].grid(column='4',columnspan='2',row='3',padx=pad_x,pady=pad_y,sticky='W')

    # Options and Quit
    self.restart_button = tk.Button(self,text='Restart',fg='red',relief='raised',command=self.resetBoard,width=8)
    self.restart_button.grid(column='0',columnspan='3',row='4',padx=pad_x,pady=pad_y)

    self.icon_button = tk.Button(self,text='Play as O',fg='red',relief='raised',command=self.setPlayerIcons,width=8)
    self.icon_button.grid(column='3',columnspan='3',row='4',padx=pad_x,pady=pad_y)

    quit_button = tk.Button(self,text='QUIT',fg='red',relief='raised',command=self.master.destroy,width=6)
    quit_button.grid(column='0',columnspan='2',row='5',padx=pad_x,pady=pad_y)

    debug_show = tk.Button(self,text='Debug Options',fg='red',relief='raised',command=self.debugOptionsGUI)
    debug_show.grid(column='2',columnspan='4',row='5',padx=pad_x,pady=pad_y)
  
  # updates the displayed board  - returns nothing
  def updateBoard(self,location):
    if not self.isGameOver():
      self.board[location] = self.player_icon
      self.button_board[location]['text'] = self.player_icon
      self.button_board[location]['state'] = 'disabled'
      if not self.isGameOver() and not self.debug_options['no_cpu']:
        location = self.computerTurn()
        self.board[location] = self.computer_icon
        self.button_board[location]['text'] = self.computer_icon
        self.button_board[location]['state'] = 'disabled'
        if self.isGameOver():
          self.gameOverDisplay()
      elif not self.isGameOver() and self.debug_options['no_cpu']:
        self.player_icon, self.computer_icon = self.computer_icon, self.player_icon
      else:
        self.gameOverDisplay()
    else:
      self.gameOverDisplay()

    # showing debug options
    if self.debug_options['show_game_checks']:
      print('Board Updated',file=stdout)

  # Handles computer movement - returns index
  def computerTurn(self):
    # Returns a list with the indexs that are empyty in the board variable
    valid_locations = [key for key,value in self.board.items() if value == ' ']
    if len(valid_locations) == 0:
      return None
    while True:
      # If moving first and random first move is set execute a random move, else choose a corner
      if len(set(list(self.board.values()))) == 1:
        if self.debug_options['random_first_move']:
          return choice(valid_locations)
        else:   
          return choice(['top_left','top_right','bottom_left','bottom_right'])

      else:
        # Tests for a winning move, returns that index if true
        for item in valid_locations:   
          temp_board = self.board.copy()
          temp_board[item] = self.computer_icon
          winning_move, a = self.winningCondition(list(temp_board.values()))
          if winning_move:
            del temp_board
            # showing debug options
            if self.debug_options['debug_output'] or self.debug_options['show_computer_moves']:
              print('Computer played a winning move',file=stdout)
            return item  
          else:
            del temp_board
            continue
        
        # Tests to prevent wwinning move, return that index if true
        for item in valid_locations:   
          temp_board = self.board.copy()
          temp_board[item] = self.player_icon
          winning_move, a = self.winningCondition(list(temp_board.values()))
          if winning_move:
            del temp_board
            # show debug options
            if self.debug_options['debug_output'] or self.debug_options['show_computer_moves']:
              print('Computer prevented a winning move',file=stdout)
            return item
          else:
            del temp_board
            continue

        # Each of the following are choosen in order they appear and executed if computer can't win on next move or block a winnning move
        if self.board['mid_center'] == ' ' and 'mid_center' in valid_locations:   #  move on centre if available
          if self.debug_options['debug_output'] or self.debug_options['show_computer_moves']:
            print('Computer elected to take the centre',file=stdout)
          return 'mid_center'

        # If player has taken both diagonals and centre is taken take one of the outer centre
        # TODO has potential exploiation issues if one of the randomly choosen locations is already picked
        elif ((self.board['top_left'] == self.player_icon and self.board['bottom_right'] == self.player_icon) or (self.board['top_right'] == self.player_icon and self.board['bottom_left'] == self.player_icon)): 
          options = [value for value in valid_locations if value == 'top_center' or value == 'mid_left' or value == 'mid_right' or value == 'bottom_center']
          return choice(options)

        # The following section covers situations where the computer played first and player went into the centre spot
        elif self.board['top_left'] == self.computer_icon and self.board['mid_center'] == self.player_icon and 'bottom_right' in valid_locations:
          return 'bottom_right' 
        elif self.board['top_right'] == self.computer_icon and self.board['mid_center'] == self.player_icon and 'bottom_left' in valid_locations:
          return 'bottom_left' 
        elif self.board['bottom_left'] == self.computer_icon and self.board['mid_center'] == self.player_icon and 'top_right' in valid_locations:
          return 'top_right'
        elif self.board['bottom_right'] == self.computer_icon and self.board['mid_center'] == self.player_icon and 'top_left' in valid_locations:
          return 'top_left' 
        else:
            pass

        # if above finds no moves, attempt to think 2 moves ahead by repeating the winning move function twice
        for item_a in valid_locations:  
          temp_board = self.board.copy()
          temp_board[item_a] = self.computer_icon
          secondary_valid_locations = [key for key,value in self.board.items() if value == ' ']
          for item_b in secondary_valid_locations:  
            temp_board[item_b] = self.computer_icon
            winning_move, a = self.winningCondition(list(temp_board.values()))
            if winning_move:
              del temp_board, secondary_valid_locations
              # showing debug options
              if self.debug_options['debug_output'] or self.debug_options['show_computer_moves']:
                print('Computer thought 2 moves ahead',file=stdout)
              return item_a
            else:
              continue   
          del temp_board, secondary_valid_locations
        # if no other options choose randomly from available locations
        if self.debug_options['debug_output'] or self.debug_options['show_computer_moves']:
          print('Computer executed a random move',file=stdout)
        return choice(valid_locations)

  # Checks if the game is won / lost / drawn - returns boolean
  def isGameOver(self):
    gameOver, winner = self.winningCondition(list(self.board.copy().values()),'p') # checks for a winning condition
    if self.isBoardFull():
      self.gamestate = 'Board is full, Game is a Draw'
      if self.debug_options['debug_output']:
        print('Computer executed a random move',file=stdout)
      return True
    elif gameOver:
      if winner == self.player_icon:
        self.gamestate = 'Congradulations, You Won'
        if self.debug_options['debug_output']:
          print('Computer executed a random move',file=stdout)
        return True
      elif winner == self.computer_icon:
        self.gamestate = 'Sorry, You Lost'
        if self.debug_options['debug_output']:
          print('Computer executed a random move',file=stdout)
        return True
      else:
        # if all else fails
        systemExit('Unexpected Error Occured, Please Reload the App (GAMEOVER)')
    else:
      # show debug options
      if self.debug_options['show_game_checks']:
        print('Checked for a gameover',file=stdout)
      return False

  # Checks if the board is full - returns boolean      
  def isBoardFull(self):
    # if an empyty space is present in the board return false
    
    # showing debug options
    if self.debug_options['show_game_checks']:
      print('Board full check',file=stdout)
    if ' ' in list(self.board.values()):
      return False
    else:
      return True

  # Checks if there is a 3 in a row present on the board - returns boolean and winning icon
  def winningCondition(self,data,user='c'):
    # checks if all values in the given range is the same using set logic
    if len(set(data[0:3])) == 1 and ' ' not in data[0:3]:     # Top row
      return True, data[0]
    elif len(set(data[3:6])) == 1 and  ' ' not in data[3:6]:   # Middle Row
      return True, data[3]
    elif len(set(data[6:9])) == 1 and  ' ' not in data[6:9]:    # Bottom Row
      return True, data[6]
    elif len(set(data[::3])) == 1 and  ' ' not in data[::3]:   # First Column
      return True, data[0]
    elif len(set(data[1::3])) == 1 and  ' ' not in data[1::3]:  # Second Column
      return True, data[1]
    elif len(set(data[::-3])) == 1 and  ' ' not in data[::-3]:  # Third Column
      return True, data[2]
    elif len(set(data[::4])) == 1 and  ' ' not in data[::4]:   # Diagonal Left->Right
      return True, data[0]
    elif len(set(data[2:8:2])) == 1 and  ' ' not in data[2:8:2]: # Diagonal Right->Left
      return True, data[2]
    else:
      # showing debug options
      if self.debug_options['show_game_checks'] and user == 'p':
        print('No current winning positions',file=stdout)
      return False, None

  # Adjusts the board status display and disables buttons    
  def gameOverDisplay(self):
    # set status button
    self.status_button['state'] = 'normal'
    self.status_button['text'] = self.gamestate
    self.status_button['state'] = 'disabled'
    self.restart_button['text'] = 'Play Again'
    # disabling all remaining buttons
    locations = [key for key in self.board.keys() if self.button_board[key]['state'] != 'disabled']
    for item in locations:
      self.button_board[item]['state'] = 'disabled'

  # Adjusts the board status display, enables buttons and rests moves    
  def resetBoard(self):
    locations = [key for key in self.board.keys()]
    # reset all input locations
    for item in locations:
      self.board[item]=' '
      self.button_board[item]['text'] = '   '
      self.button_board[item]['state'] = 'normal'
    # reset other buttons
    self.status_button['state'] = 'normal'
    self.status_button['state'] = 'disabled'
    self.restart_button['text'] = 'Restart'
    # if computer plays first make that move
    if self.computer_icon == 'X':
      location = self.computerTurn()
      self.board[location] = self.computer_icon
      self.button_board[location]['text'] = self.computer_icon
      self.button_board[location]['state'] = 'disabled'
      firstMove = location
    # if we are running auto tests do this
    if self.debug_options['run_custom_auto_tests'] and self.automated_test_count-1 != self.debug_options['custom_auto_tests_amount']:
      for i in range(4):
        location = self.computerTurn()
        self.updateBoard(location)
      # lets the player know whats happening
      visualisation = '''
            |   | 
          {} | {} | {}
            |   | 
        -----------
            |   |
          {} | {} | {}
            |   |
        -----------
            |   | 
          {} | {} | {}
            |   | '''.format(*self.board.values()) # fils each '{}' section each variable stored in the board variable sequentially
      print('Automated Test: {}\nResult: {}\n{}\nFirst move was: {}\n\n'.format(self.automated_test_count,self.gamestate,visualisation,firstMove),file=stdout)
      # add on to the test count
      self.restart_button['text'] = 'Next Test'
      self.automated_test_count += 1
    # reset if count is reached
    if self.automated_test_count-1 == self.debug_options['custom_auto_tests_amount'] and self.debug_options['custom_auto_tests_amount'] != 0:
      self.automated_test_count = 1
      self.debug_options['run_custom_auto_tests'] = False
      self.restart_button['text'] = 'Play Again'
    # reset the game state
    self.gamestate = 'Game Running'
    self.status_button['text'] = self.gamestate

  # Handles the debug options GUI
  def debugOptionsGUI(self):
    # 'show_computer_moves':False, 'show_game_checks':False, 'show_each_automated_move':False,
    # 'debug_output':False, 'run_custom_auto_tests':False, 'custom_auto_tests_amount':0
    # Createa and manage window
    debug = tk.Toplevel(self)
    debug.title('Debug Options')
    debug.resizable(0,0)
    # Local Variables
    fg_c = 'black'
    bg_c = 'white'
    pad_style = 'ridge'
    pad_x = 3
    pad_y = 3
    counter = 0
    # Initalisation of buttons
    options = [key for key in self.debug_options.keys()]
    for item in options:
      # buttons for boolean options
      if isinstance(self.debug_options[item],bool):
        self.debug_board.update({item : tk.Button(debug,text=item,fg=fg_c,bg=bg_c,relief=pad_style,state='disabled',width=22) } )
        self.debug_board[item].grid(column='0',row=counter,padx=pad_x,pady=pad_y)
        self.debug_board.update({item + 'variable' : tk.Button(debug,text=str(self.debug_options[item]),fg=fg_c,bg=bg_c,relief=pad_style,width=5,command=lambda a=item: self.debugOptionsSet(a) ) } )
        self.debug_board[item + 'variable'].grid(column='1',row=counter,padx=pad_x,pady=pad_y)
      # buttons for integer options
      elif isinstance(self.debug_options[item],int):
        self.debug_board.update({item : tk.Button(debug,text=item,fg=fg_c,bg=bg_c,relief=pad_style,state='disabled',width=22) } )
        self.debug_board[item].grid(column='0',row=counter,padx=pad_x,pady=pad_y)
        self.debug_board.update({item + 'variable' : tk.Entry(debug,fg=fg_c,bg=bg_c,width=5) } )
        self.debug_board[item + 'variable'].insert(0,str(self.debug_options[item]))
        self.debug_board[item + 'variable'].grid(column='1',row=counter,padx=pad_x,pady=pad_y)
        self.debug_board.update({item+'submit' : tk.Button(debug,text='Submit',fg=fg_c,bg=bg_c,relief=pad_style,width=5,command=lambda a=item: self.debugOptionsSet(a) ) } )
        self.debug_board[item+'submit'].grid(column='1',row=counter+1,padx=pad_x,pady=pad_y)
        counter += 1
      counter += 1
    # Quit Button
    quit_button = tk.Button(debug,text='Close Debug Options',fg='red',relief='raised',command=debug.destroy)
    quit_button.grid(columnspan='2',row=counter,padx=pad_x,pady=pad_y)

  # setting the debug options
  def debugOptionsSet(self,location):
    # settings for boolean options
    if isinstance(self.debug_options[location],bool):
      self.debug_options[location] = not self.debug_options[location]
      self.debug_board[location+'variable']['text'] = str(self.debug_options[location])
    # settings for integer options
    elif isinstance(self.debug_options[location],int):
      self.debug_options[location] =  int(self.debug_board[location+'variable'].get())

  # setting the player icons
  def setPlayerIcons(self):
    self.player_icon, self.computer_icon = self.computer_icon, self.player_icon
    # Updating Board
    self.icon_button['text'] = 'Play as {}'.format(self.computer_icon)
     # showing debug options
    if self.debug_options['show_game_checks'] or self.debug_options['debug_output']:
      print('Switched Player icons, Player = {} and Computer = {}'.format(self.player_icon, self.computer_icon),file=stdout)
    self.resetBoard()

  def abc(self, a):
    return a

### Class Call ###

root = tk.Tk()

# Create Application
app = TicTacToe(master=root)
print(app.abc('a'))
# Window Managment
app.master.title('Tic-Tac-Toe')
app.master.geometry('200x200')
app.master.resizable(0,0)

if __name__ == "__main__":
  # Start Program
  app.mainloop()