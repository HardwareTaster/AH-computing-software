
rows = 4
cols = 6
seats = [['-' for c in range(cols)] for r in range(rows)]
 
TODO 1: fill every seat with '-'
 
TODO 3: mark seats (1,1), (2,4) and (3,0) as 'X'
seats [1][1], seats [2][4], seats [3][0] = "X" ,"X", "X"
TODO 2: display the grid neatly, one row per line
for row in range(rows):
	print(seats[row])
 
TODO 4: count and display the number of free seats
counter = 0
for row in range (rows):
	for col in range (cols):
		if seats [row][col] == "-":
			counter+= 1
print (counter)
-----------------------------------------------------------------------------------------------------

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

--------------------------------------------------------------------------------
seat = [ ['' for col in range(5)] for row in range(2)]
seat[0][0] = 'D'
seat[0][1] = 'AB'
seat[0][2] = 'MD'
seat[1][4] = 'LL'
seat[1][0] = 'ES'
seat[1][2] = 'T'


for row in range(2):
    print(seat[row])


# TODO 1: ask the user for their initials, and a row and column for their seat
initials = input("enter intitails")
row = int(input("enter row: 0 or 1"))
col = int(input("enter column: 0-5 "))
while seat[row][col] != '':
	print ("seat taken")
	row = int(input("enter row: 0 or 1"))
	col = int(input("enter column: 0-5 "))
seat[row][col] = "initials"

TODO 2: check whether that row and column is free (equal to '')


TODO 3: if it is free, store the initials at that row and column


TODO 4: if it is not free, display an error message and ask again for a row and column

#-------------------------------------------------------------------------------------

students = ['Ali', 'Bea', 'Cal', 'Dee', 'Eve']
student_averages = []
test_averages = []
marks = [
	[14, 16, 12, 18],
	[9,  11, 15, 10],
	[20, 19, 18, 20],
	[7,  8,  10, 6],
	[15, 14, 16, 17]
]
 
for r in range(len(marks)):
	print(students[r], marks[r])
 
# TODO 1: average mark per student
for r in range(5):
	total = 0
	for c in range (4):
		total += marks [r][c]
	average = total/4
	student_averages.append(average)
print (student_averages)
# TODO 2: average mark per test (per column)
for c in range (4):
	total = 0
	for r in range(5):
		total += marks [r][c]
	average = total/5
	test_averages.append(average)
print (test_averages)
# TODO 3: highest mark, student and test
max = 0
for r in range(5):
	for c in range (4):
		if marks [r][c]>max:
			max =  marks[r][c]
			high_student = students[r]
			test = c+1
print ("the highest mark was ",max, "attained by", high_student, "on test", test)
# TODO 4: lowest mark, student and test
min = 999
for r in range(5):
	for c in range (4):
		if marks [r][c]<min:
			min =  marks[r][c]
			low_student = students[r]
			test = c+1
print ("the lowest mark was ",min, "attained by", low_student, "on test", test)
