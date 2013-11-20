from graphics import *

def draw_board(w):
    line = Line(Point(0,30),Point(90,30))
    line.draw(w)
    line = Line(Point(0,60),Point(90,60))
    line.draw(w)
    line = Line(Point(30,0),Point(30,90))
    line.draw(w)    
    line = Line(Point(60,0),Point(60,90))
    line.draw(w)

def check_for_winner(board):
    if board[0][0] == board[0][1] and board[0][1] == board[0][2]:
        return board[0][0]
    if board[1][0] == board[1][1] and board[1][1] == board[1][2]:
        return board[1][0]
    if board[2][0] == board[2][1] and board[2][1] == board[2][2]:
        return board[2][0]
    if board[0][0] == board[1][0] and board[1][0] == board[2][0]:
        return board[0][0]
    if board[0][1] == board[1][1] and board[1][1] == board[2][1]:
        return board[0][1]
    if board[0][2] == board[1][2] and board[1][2] == board[2][2]:
        return board[0][2]
    if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        return board[0][0]
    if board[2][0] == board[1][1] and board[1][1] == board[0][2]:
        return board[2][0]
    
    for row in board:
        for square in row:
            if square == None:
                return None
            
    return "no one"
    

def execute_move(board,turn,win):
    p = win.getMouse()
    row = int(p.getY()//30)
    col = int(p.getX()//30)
    if board[row][col] == None:
        board[row][col] = turn        
        text = Text(Point(col*30+15,row*30+15),turn)
        text.draw(win)
        return True
    return False

win = GraphWin("Tic Tac Toe",300,300)

win.setCoords(0,0,90,90)

draw_board(win)
board = [[None,None,None],[None,None,None],[None,None,None]]

# Play the game
turn = "X"
while check_for_winner(board) == None:
    # Execute a turn of the game
    if execute_move(board,turn,win):    
        if turn == "X":
            turn = "O"
        else:
            turn = "X"

print("The winner is",check_for_winner(board))

win.getMouse()
win.close()
