#    |   | 
#  0 | 1 | 2
#    |   | 
# -----------
#    |   |
#  3 | 4 | 5
#    |   |
# -----------
#    |   | 
#  6 | 7 | 8
#    |   | 
# TODO
#

### Import Modules ###
from sys import stdout
from sys import exit as systemExit
from random import randint
from random import choice

### Global Var ###	
positions = [x for x in range(9)] # creates an array 9 items long with each item being the position
board = [' ']*9 # creates an empty array of length 9
player_icon = ' '
computer_icon = ' '
next_player = ''  # placeholder variable to store who takes the next turn

### Debugging Tools ###
automated_test_count = 1  # starting at one for use of standard number system
# dictionary of debug options, most are set as booleans
debug_options = {'show_computer_moves':False, 'show_game_checks':False, 'show_each_automated_move':False, 'random_first_move':False,\
   'run_five_automated_tests':False, 'debug_output':False, 'run_custom_auto_tests':False, 'custom_auto_tests_amount':0}

### Functions ### 

# Main calling function - sets up the game then handles calling player turns if game isn't over
def main():
  global player_icon, computer_icon, next_player, debug_options
  # if player icon hasn't been set call the function to do so
  while (player_icon == ' '):
    player_icon, computer_icon = setPlayerIcon()
  print('You are {}\'s'.format(player_icon))
  # showing debug options
  if debug_options['debug_output'] or debug_options['show_game_checks']:
    print('Player icon assigned',file=stdout)
  # main loop
  while not isGameOver():
    # calls playerTurn() or computerTurn() based on the conditions of the next_player variable
    if next_player == 'player':
        drawBoard()
        playerTurn()
        continue
    elif next_player == 'computer':
      index = computerTurn()  # get returned index of computerTurn() (integer)
      board[index] = computer_icon
      next_player = 'player'
      continue
    elif next_player == 'run_five_automated_tests' or next_player == 'run_custom_auto_tests':
      if len(set(board)) != 1:
        player_icon, computer_icon = computer_icon, player_icon
      index = computerTurn()
      board[index] = player_icon
      # showing debug options
      if debug_options['show_each_automated_move'] or debug_options['debug_output']:
        print('automated move',file=stdout)
      continue
    else:
      # if all else fails
      systemExit('Unexpected Error Occured, Please Reload the App (MAIN)')
  drawBoard()
  # showing debug options
  if debug_options['run_five_automated_tests'] or debug_options['run_custom_auto_tests']:
    print('Automated test: ' + str(automated_test_count),file=stdout,end='\n\n')
  playAgain()

# Debugger UI - returns nothing
def debugger():
  quit_debugger = False
  global debug_options
  # printing the UI
  print('Welcome to the Debugger')
  while not quit_debugger:
    print('''
               Option         : Boolean 
    show_computer_moves       : {show_computer_moves} 
    show_game_checks          : {show_game_checks}
    show_each_automated_move  : {show_each_automated_move}
    random_first_move         : {random_first_move}
    run_five_automated_tests  : {run_five_automated_tests}
    debug_output              : {debug_output}
    run_custom_auto_tests     : {run_custom_auto_tests}
    custom_auto_tests_amount  : {custom_auto_tests_amount}
    To exit debugger type q:
    '''.format(**debug_options))
    inp = input('Please type a command \n')
    # choosing command from input
    if inp == 'help':
      print('Current commands are: help, set')
    elif inp[:3] == 'set':
      # try to set given variable as given boolean / integer with cases for bad input
      try:
        var = inp.split(' ')
        if len(var) != 3:
          raise IndexError   
        if var[1] not in list(debug_options.keys()):
          raise KeyError()     
        if (var[1] != 'custom_auto_tests_amount' and var[2].capitalize() != 'True' and var[2].capitalize() != 'False'):
          print('Boolean Value not accepted\nCorrect usage is: set [Option] [Boolean/Digit]')
          continue
        if var[1] == 'custom_auto_tests_amount' and not var[2].isdigit():
          print('Digit Value not accepted\nCorrect usage is: set [Option] [Boolean/Digit]')
          continue
        if var[1] == 'custom_auto_tests_amount' and var[2].isdigit():
          debug_options[var[1]] = int(var[2])
          continue
        elif var[1] != 'custom_auto_tests_amount':
          debug_options[var[1]] = bool(var[2].capitalize() == 'True')
          continue
        else:
          Exception()
      except KeyError:
        print('Undefined debug option\nCorrect usage is: set [Option] [Boolean/Digit]')
        continue
      except IndexError:
        print('2 arguments are required but {} were given\nCorrect usage is: set [Option] [Boolean/Digit]'.format(len(var)-1))
        continue
      except:
        print('Incorrect usage\nCorrect usage is: set [Option] [Boolean/Digit]')
        continue
    elif inp == 'q:':
      quit_debugger = True
    else:
      print('Unkown command, for options type "help"')
      continue

# Handles drawing the board to the terminal - returns nothing
def drawBoard():
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
      |   | '''.format(*board) # fils each '{}' section each variable stored in the board variable sequentially
  print(visualisation)
  # showing debug options
  if debug_options['show_game_checks']:
    print('Board Displayed',file=stdout)

# Handles the player movement - returns nothing (handles placement in function)
def playerTurn():
  global next_player, board
  valid_locations = [str(index) for index,value in enumerate(board) if value == ' ']  # returns a list with all empyty indexes in the board variable
  while True:
    print('''
      |   | 
    0 | 1 | 2
      |   | 
   -----------
      |   |
    3 | 4 | 5
      |   |
   -----------
      |   | 
    6 | 7 | 8
      |   | ''')
    # get user input and test if it is valid
    inp = input('Pleae enter a one of the following locations: '+' '.join(valid_locations)+'\n')
    if inp in valid_locations:
      break
    else:
      print('invalid location, please try again')
      continue
  # set location designated as player icon
  board[int(inp)] = player_icon
  next_player = 'computer'
  # showing debug options
  if debug_options['debug_output']:
    print('Player moved',file=stdout)

# Handles computer movement - returns index
def computerTurn():
  global next_player, board
  # Returns a list with the indexs that are empyty in the board variable
  valid_locations = [str(index) for index,value in enumerate(board) if value == ' ']
  while True:
     # If moving first and random first move is set execute a random move, else choose a corner
    if len(set(board)) == 1:
      if debug_options['random_first_move']:
        return int(choice(valid_locations))
      else:   
        return choice([0,2,6,8])

    else:
      # Tests for a winning move, returns that index if true
      for item in valid_locations:   
        temp_board = board.copy()
        temp_board[int(item)] = computer_icon
        winning_move, a = winningCondition(temp_board)
        if winning_move:
          del temp_board
          if debug_options['debug_output'] or debug_options['show_computer_moves']:
            print('Computer played a winning move',file=stdout)
          return int(item)   
        else:
          del temp_board
          continue
      
      # Tests to prevent wwinning move, return that index if true
      for item in valid_locations:   
        temp_board = board.copy()
        temp_board[int(item)] = player_icon
        winning_move, a = winningCondition(temp_board)
        if winning_move:
          del temp_board
          if debug_options['debug_output'] or debug_options['show_computer_moves']:
            print('Computer prevented a winning move',file=stdout)
          return int(item)
        else:
          del temp_board
          continue

      # Each of the following are choosen in order they appear and executed if computer can't win on next move or block a winnning move
      if board[4] == ' ' and '4' in valid_locations:   #  move on centre if available
        if debug_options['debug_output'] or debug_options['show_computer_moves']:
          print('Computer elected to take the centre',file=stdout)
        return 4

      # If player has taken both diagonals and centre is taken take one of the outer centre
      elif ((board[0] == player_icon and board[8] == player_icon) or (board[2] == player_icon and board[6] == player_icon)): 
        a = randint(0,4)
        if a == 1 and '1' in valid_locations:
          return 1  # top 
        elif a == 2 and '3' in valid_locations:
          return 3  # right
        elif a == 3 and '5' in valid_locations:
          return 5  # left
        elif a == 4 and '7' in valid_locations:
          return 7  # bottom
        else:
          pass

      # The following section covers situations where the computer played first and player went into the centre spot
      elif board[0] == computer_icon and board[4] == player_icon and '8' in valid_locations:
        return 8 
      elif board[2] == computer_icon and board[4] == player_icon and '6' in valid_locations:
        return 6 
      elif board[6] == computer_icon and board[4] == player_icon and '2' in valid_locations:
        return 2 
      elif board[8] == computer_icon and board[4] == player_icon and '0' in valid_locations:
        return 0 
      else:
          pass

      # if above finds no moves, attempt to think 2 moves ahead by repeating the winning move function twice
      for item_a in valid_locations:  
        temp_board = board.copy()
        temp_board[int(item_a)] = computer_icon
        secondary_valid_locations = [str(index) for index,value in enumerate(temp_board) if value == ' ']
        for item_b in secondary_valid_locations:  
          temp_board[int(item_b)] = computer_icon
          winning_move, a = winningCondition(temp_board)
          if winning_move:
            del temp_board, secondary_valid_locations
            if debug_options['debug_output'] or debug_options['show_computer_moves']:
              print('Computer thought 2 moves ahead',file=stdout)
            return int(item_a)
          else:
            continue   
        del temp_board, secondary_valid_locations
      # if no other options choose randomly from available locations
      if debug_options['debug_output'] or debug_options['show_computer_moves']:
        print('Computer executed a random move',file=stdout)
      return int(choice(valid_locations))

# Checks if the game is won / lost / drawn - returns boolean
def isGameOver():
  gameOver, winner = winningCondition(board.copy()) # checks for a winning condition
  if isBoardFull():
    print("Board is full, Game is a Draw")
    return True
  elif gameOver:
    if winner == player_icon:
      print('Congradulations, You Won')
      return True
    elif winner == computer_icon:
      print("Sorry, You Lost")
      return True
    else:
      # if all else fails
      systemExit('Unexpected Error Occured, Please Reload the App (GAMEOVER)')
  else:
    if debug_options['show_game_checks']:
      print('Checked for a gameover',file=stdout)
    return False

# Checks if the board is full - returns boolean      
def isBoardFull():
  # if an empyty space is present in the board return false
  if ' ' in board:
    return False
  else:
    # showing debug options
    if debug_options['show_game_checks']:
      print('Board full check',file=stdout)
    return True

# Checks if there is a 3 in a row present on the board - returns boolean and winning icon
def winningCondition(data):
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
    if debug_options['show_game_checks']:
      print('No current winning positions',file=stdout)
    return False, None
  
# Handles the allocation of player and computer icons - returns list of length 2 with items
def setPlayerIcon():
  global next_player
  # checks for automated tests - if not get input and validate
  if not debug_options['run_five_automated_tests'] and not debug_options['run_custom_auto_tests']:
    inp = input('Would you like to play first y/n\n').lower()
    if (inp != 'y' and inp != 'n' and inp != 'debug' and inp != 'exit'):
      print('Invalid input: Please type either "y" or "n"',end='')
      return [' ',' ']
    # check if user wants to call the debugger
    elif inp == 'debug':
      debugger()
      # run given debug options
      if debug_options['run_five_automated_tests']:
        next_player = 'run_five_automated_tests'
        return ['X','O']
      elif debug_options['run_custom_auto_tests']:
        next_player = 'run_custom_auto_tests'
        return ['X','O']
      else:
        return [' ',' ']
    # handle other input
    elif inp == 'exit':
      systemExit('Game Quit')
    elif inp == 'y':
      next_player = 'player'
      return ['X','O']
    else:
      next_player = 'computer'
      return ['O','X']
  else:
    # returns default if automated tests are running
    return ['X','O']

# Handles the reply system - returns nothing but calls main() function
def playAgain():
  global debug_options, automated_test_count, next_player, board, player_icon, computer_icon
  # check to see that the user isn't running and automated test
  if not debug_options['run_five_automated_tests'] and not debug_options['run_custom_auto_tests']:
    inp = input('Would you like to play again y/n\n').lower()
    # if user wants to play again reset global variables
    if inp == 'y':
        player_icon, computer_icon = [' ', ' ']
        board = [' ']*9
        automated_test_count = 1
        next_player = ''
        main()
    # if user doesn't input 'y' exit system
    else:
      systemExit('Goodbye')
  # if in an autmated test reset board and player icons and check to see if the number of automated tests have been completed
  else:
        player_icon, computer_icon = [' ', ' ']
        board = [' ']*9
        automated_test_count += 1
        if debug_options['run_five_automated_tests'] and automated_test_count == 5:
          debug_options['run_five_automated_tests'] = False
        elif debug_options['run_custom_auto_tests'] and automated_test_count == debug_options['custom_auto_tests_amount']:
          debug_options['run_custom_auto_tests'] = False
        main()

### main call ###
main()