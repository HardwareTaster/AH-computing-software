
rows = 4
cols = 6
seats = [['-' for c in range(cols)] for r in range(rows)]
 
# TODO 1: fill every seat with '-'
 
# TODO 3: mark seats (1,1), (2,4) and (3,0) as 'X'
seats [1][1], seats [2][4], seats [3][0] = "X" ,"X", "X"
# TODO 2: display the grid neatly, one row per line
for row in range(rows):
	print(seats[row])
 
# TODO 4: count and display the number of free seats
counter = 0
for row in range (rows):
	for col in range (cols):
		if seats [row][col] == "-":
			counter+= 1

print (counter)


#-------------------------------------------------------------------------------------------------



board = [
	['X', 'X', 'X'],
	['O', 'X', 'O'],
	['O', 'O', 'X']
]
 
for row in range(3):
	print(board[row])
 
winner = ''
 
# TODO 1: check rows
for row in range (3):
 	if board[row][0]== board[row][1] == board[row][2]:
 		winner = board[row][0]
 
# TODO 2: check columns
for col in range (3):
	if board[0][col]== board[1][col] == board[2][col]:
			winner = board[0][col]
# TODO 3: check diagonals
for row in range (3):
	if board[0][0]== board[1][1] == board[2][2] or board[0][2]== board[1][1] == board[2][0]:
		winner = board[1][1]
# TODO 4: report the result

if winner == '':
	print('No winner')
else:
    print(winner, 'has won')
