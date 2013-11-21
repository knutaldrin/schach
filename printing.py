import os
from termcolor import colored, cprint
from board import colors, pieces, getBoard


print_white = lambda x: cprint( x, "white", "on_green" )
print_black = lambda x: cprint( x, "grey", "on_green" )
print_red = lambda x: cprint( x, "red", "on_cyan" )
print_info = lambda x: print( x )

text_white = lambda x: colored( x, "white", "on_green" )
text_black = lambda x: colored( x, "grey", "on_green" )
text_info = lambda x: x 

bgcol = "on_green" #Ugly

def text_board( x, col = "" ):
	global bgcol
	if col == "":
		out = colored( x + " ", "grey", bgcol )
	elif col == colors["white"]:
		out = colored( x + " ", "white", bgcol )
	else:
		out = colored( x + " ", "grey", bgcol )
	if bgcol == "on_green":
		bgcol = "on_blue"
	else:
		bgcol = "on_green"
		
	return out

def newline_board():
	global bgcol
	if bgcol == "on_green":
		bgcol = "on_blue"
	else:
		bgcol = "on_green"
	return "\n"
	
def clearScreen():
	global bgcol
	bgcol = "on_green"
	os.system( "clear" )




piecesPrint = {
#	colors["white"]: {
#		"p": "♙",
#		"r": "♖",
#		"k": "♘",
#		"b": "♗",
#		"x": "♔",
#		"q": "♕" 
#	},
	
	colors["black"]: {
		"p": "♟",
		"r": "♜",
		"k": "♞",
		"b": "♝",
		"x": "♚",
		"q": "♛"
	},
	colors["white"]: {
		"p": "♟",
		"r": "♜",
		"k": "♞",
		"b": "♝",
		"x": "♚",
		"q": "♛"
	}
}

def printBoard():

	text = ""
	i = 0
	text += text_info( "  a b c d e f g h\n" )
	for row in getBoard():
		i += 1
		text += text_info( str( i ) + " " )
		for piece in row:
			if piece == " ":
				text += text_board( " " )
			else:
				text += text_board( piecesPrint[ piece[1] ][ piece[0] ], piece[1] )
				
			#elif piece[1] == colors["white"]:
			#	text += text_white( piece[0] ) + text_white( " " )
			#elif piece[1] == colors["black"]:
			#	text += text_black( piece[0] ) + text_black( " " )
		text += newline_board()
	
	clearScreen()
	print( text + "\n" )