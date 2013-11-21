import copy

boardInit = [
	[ "r2", "k2", "b2", "q2", "x2", "b2", "k2", "r2" ],
	[ "p2", "p2", "p2", "p2", "p2", "p2", "p2", "p2" ],
	[ " ", " ", " ", " ", " ", " ", " ", " " ],
	[ " ", " ", " ", " ", " ", " ", " ", " " ],
	[ " ", " ", " ", " ", " ", " ", " ", " " ],
	[ " ", " ", " ", " ", " ", " ", " ", " " ],
	[ "p1", "p1", "p1", "p1", "p1", "p1", "p1", "p1" ],
	[ "r1", "k1", "b1", "q1", "x1", "b1", "k1", "r1" ]
]

board = boardInit

pieces = {
	"pawn": "p",
	"rook": "r",
	"bishop": "b",
	"knight": "k",
	"king": "x",
	"queen": "q",
	"empty": " "
}

colors = {
	"white": "1",
	"black": "2"
}

def boardIndex( pos ):
	return board[pos[0]][pos[1]]
	
def movePiece( oldpos, newpos ):
	board[newpos[0]][newpos[1]] = boardIndex( oldpos )
	board[oldpos[0]][oldpos[1]] = " "
	
def promote( pos, to ):
	board[pos[0]][pos[1]] = to + board[pos[0]][pos[1]][1]
	
def findKing( color ):
	for i in range( 0, 8 ):
		for j in range( 0, 8 ):
			pos = [ i, j ]
			piece = boardIndex( pos )
			if piece[0] == pieces["king"] and piece[1] == color:
				return pos

def resetBoard():
	global board
	board = boardInit
	
def getBoard():
	global board
	return board
	
def getBoardCopy():
	return copy.deepcopy( getBoard() )
	
def setBoard( newBoard ):
	global board
	board = newBoard
	
def setBoardCopy( newBoard ):
	setBoard( copy.deepcopy( newBoard ) )
	
resetBoard() # Ugly namespacing