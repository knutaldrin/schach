from board import boardIndex, pieces, colors
from printing import printBoard
import board
import copy
import exceptions

def posLegal( pos ):
	if pos[0] < 0 or pos[0] > 7:
		return False
	
	if pos[1] < 0 or pos[1] > 7:
		return False
	
	return True
	
def legalMoves( pos ):
	piece = boardIndex( pos )
	legal = []
	if piece[0] == pieces["pawn"]: # Pawn is a shite to code
		legal = legalMovesPawn( pos, piece )
					
	elif piece[0] == pieces["rook"]: # Ez
		legal = legalMovesRook( pos, piece )
				
	elif piece[0] == pieces["bishop"]: # Copypaste
		legal = legalMovesBishop( pos, piece )
				
	elif piece[0] == pieces["queen"]: # Hax hax
		# Queen is equal to bishop and rook, so DRY!
		legal = legalMovesQueen( pos, piece )
		
	elif piece[0] == pieces["king"]:
		legal = legalMovesKing( pos, piece )
		
	elif piece[0] == pieces["knight"]:
		legal = legalMovesKnight( pos, piece )
	
	return legal
	
	
def legalMovesPawn( pos, piece ):
	legal = []
	if piece[1] == colors["white"]:
		# Can move two spaces first move
		if( pos[0] == 6 ):
			newPos = [ pos[0]-2, pos[1] ]
			if posLegal( newPos ):
				if boardIndex( newPos ) == " ":
					legal.append( newPos )
	
		newPos = [ pos[0]-1, pos[1] ]
		if posLegal( newPos ):
			if boardIndex( newPos ) == " ":
				legal.append( newPos )
		
		newPos = [ pos[0]-1, pos[1]-1 ]
		if posLegal( newPos ):
			if boardIndex( newPos ) != " " and boardIndex( newPos )[1] != piece[1]:
				legal.append( newPos )
			
		newPos = [ pos[0]-1, pos[1]+1 ]	
		if posLegal( newPos ):
			if boardIndex( newPos ) != " " and boardIndex( newPos )[1] != piece[1]:
				legal.append( newPos )
		
	else: #Black
		# Can move two spaces first move
		if( pos[0] == 1 ):
			newPos = [ pos[0]+2, pos[1] ]
			if posLegal( newPos ):
				if boardIndex( newPos ) == " ":
					legal.append( newPos )
					
		newPos = [ pos[0]+1, pos[1] ]
		if posLegal( newPos ):
			if boardIndex( newPos ) == " ":
				legal.append( newPos )
		
		newPos = [ pos[0]+1, pos[1]-1 ]
		if posLegal( newPos ):
			if boardIndex( newPos ) != " " and boardIndex( newPos )[1] != piece[1]:
				legal.append( newPos )
		
		newPos = [ pos[0]+1, pos[1]+1 ]
		if posLegal( newPos ):	
			if boardIndex( newPos ) != " " and boardIndex( newPos )[1] != piece[1]:
				legal.append( newPos )
				
	return legal				

def legalMovesRook( pos, piece ):
	legal = []
	# Just brute force it, once for each direction
	for i in range( 1, 8 ):
		newPos = [ pos[0]-i, pos[1] ]
		
		if not posLegal( newPos ):
			break
		
		if boardIndex( newPos ) == " ":
			legal.append( newPos )
			continue
		
		# This means there is a piece on the new pos
		if boardIndex( newPos )[1] != piece[1]: # Different color => enemy
			legal.append( newPos )
			break # Since we can't move through pieces
		else: # Friendly, not allowed
			break
	
	for i in range( 1, 8 ):
		newPos = [ pos[0]+i, pos[1] ]
		if not posLegal( newPos ):
			break
		
		if boardIndex( newPos ) == " ":
			legal.append( newPos )
			continue
		
		# This means there is a piece on the new pos
		if boardIndex( newPos )[1] != piece[1]: # Different color => enemy
			legal.append( newPos )
			break # Since we can't move through pieces
		else: # Friendly, not allowed
			break
			
	for i in range( 1, 8 ):
		newPos = [ pos[0], pos[1]-i ]
		
		if not posLegal( newPos ):
			break
		
		if boardIndex( newPos ) == " ":
			legal.append( newPos )
			continue
		
		# This means there is a piece on the new pos
		if boardIndex( newPos )[1] != piece[1]: # Different color => enemy
			legal.append( newPos )
			break # Since we can't move through pieces
		else: # Friendly, not allowed
			break
	
	for i in range( 1, 8 ):
		newPos = [ pos[0], pos[1]+i ]
		
		if not posLegal( newPos ):
			break
		
		if boardIndex( newPos ) == " ":
			legal.append( newPos )
			continue
		
		# This means there is a piece on the new pos
		if boardIndex( newPos )[1] != piece[1]: # Different color => enemy
			legal.append( newPos )
			break # Since we can't move through pieces
		else: # Friendly, not allowed
			break
			
	return legal
	
def legalMovesBishop( pos, piece ):
	legal = []
	# Just brute force it, once for each direction
	for i in range( 1, 8 ):
		newPos = [ pos[0]-i, pos[1]-i ]
		
		if not posLegal( newPos ):
			break
		
		if boardIndex( newPos ) == " ":
			legal.append( newPos )
			continue
		
		# This means there is a piece on the new pos
		if boardIndex( newPos )[1] != piece[1]: # Different color => enemy
			legal.append( newPos )
			break # Since we can't move through pieces
		else: # Friendly, not allowed
			break
	
	for i in range( 1, 8 ):
		newPos = [ pos[0]+i, pos[1]-i ]
		if not posLegal( newPos ):
			break
		
		if boardIndex( newPos ) == " ":
			legal.append( newPos )
			continue
		
		# This means there is a piece on the new pos
		if boardIndex( newPos )[1] != piece[1]: # Different color => enemy
			legal.append( newPos )
			break # Since we can't move through pieces
		else: # Friendly, not allowed
			break
			
	for i in range( 1, 8 ):
		newPos = [ pos[0]-i, pos[1]+i ]
		
		if not posLegal( newPos ):
			break
		
		if boardIndex( newPos ) == " ":
			legal.append( newPos )
			continue
		
		# This means there is a piece on the new pos
		if boardIndex( newPos )[1] != piece[1]: # Different color => enemy
			legal.append( newPos )
			break # Since we can't move through pieces
		else: # Friendly, not allowed
			break
	
	for i in range( 1, 8 ):
		newPos = [ pos[0]+i, pos[1]+i ]
		
		if not posLegal( newPos ):
			break
		
		if boardIndex( newPos ) == " ":
			legal.append( newPos )
			continue
		
		# This means there is a piece on the new pos
		if boardIndex( newPos )[1] != piece[1]: # Different color => enemy
			legal.append( newPos )
			break # Since we can't move through pieces
		else: # Friendly, not allowed
			break
			
	return legal
	
def legalMovesKnight( pos, piece ):
	legal = []
	# Funny little hopper
	
	newPos = [ pos[0]-2, pos[1]-1 ]
	if posLegal( newPos ):	
	
		if boardIndex( newPos ) == " ":
			legal.append( newPos )
		else:
			# This means there is a piece on the new pos
			if boardIndex( newPos )[1] != piece[1]: # Different color => enemy
				legal.append( newPos )
			else: # Friendly, not allowed
				pass
				
	newPos = [ pos[0]-2, pos[1]+1 ]
	if posLegal( newPos ):	
	
		if boardIndex( newPos ) == " ":
			legal.append( newPos )
		else:
			# This means there is a piece on the new pos
			if boardIndex( newPos )[1] != piece[1]: # Different color => enemy
				legal.append( newPos )
			else: # Friendly, not allowed
				pass
				
	newPos = [ pos[0]+2, pos[1]-1 ]
	if posLegal( newPos ):	
	
		if boardIndex( newPos ) == " ":
			legal.append( newPos )
		else:
			# This means there is a piece on the new pos
			if boardIndex( newPos )[1] != piece[1]: # Different color => enemy
				legal.append( newPos )
			else: # Friendly, not allowed
				pass
				
	newPos = [ pos[0]+2, pos[1]+1 ]
	if posLegal( newPos ):	
	
		if boardIndex( newPos ) == " ":
			legal.append( newPos )
		else:
			# This means there is a piece on the new pos
			if boardIndex( newPos )[1] != piece[1]: # Different color => enemy
				legal.append( newPos )
			else: # Friendly, not allowed
				pass		
				
	newPos = [ pos[0]-1, pos[1]-2 ]
	if posLegal( newPos ):	
	
		if boardIndex( newPos ) == " ":
			legal.append( newPos )
		else:
			# This means there is a piece on the new pos
			if boardIndex( newPos )[1] != piece[1]: # Different color => enemy
				legal.append( newPos )
			else: # Friendly, not allowed
				pass
				
	newPos = [ pos[0]-1, pos[1]+2 ]
	if posLegal( newPos ):	
	
		if boardIndex( newPos ) == " ":
			legal.append( newPos )
		else:
			# This means there is a piece on the new pos
			if boardIndex( newPos )[1] != piece[1]: # Different color => enemy
				legal.append( newPos )
			else: # Friendly, not allowed
				pass
				
	newPos = [ pos[0]+1, pos[1]-2 ]
	if posLegal( newPos ):	
	
		if boardIndex( newPos ) == " ":
			legal.append( newPos )
		else:
			# This means there is a piece on the new pos
			if boardIndex( newPos )[1] != piece[1]: # Different color => enemy
				legal.append( newPos )
			else: # Friendly, not allowed
				pass
				
	newPos = [ pos[0]+1, pos[1]+2 ]
	if posLegal( newPos ):	
	
		if boardIndex( newPos ) == " ":
			legal.append( newPos )
		else:
			# This means there is a piece on the new pos
			if boardIndex( newPos )[1] != piece[1]: # Different color => enemy
				legal.append( newPos )
			else: # Friendly, not allowed
				pass
			
	return legal
	
def legalMovesQueen( pos, piece ):
	return legalMovesRook( pos, piece ) + legalMovesBishop( pos, piece ) 
	
def legalMovesKing( pos, piece ):
	legal = []
	
	# A bit modified, no breaks
	for i in range( -1, 2 ): # range is REALLY FUCKED UP
		for j in range( -1, 2 ):
			newPos = [ pos[0]+i, pos[1]+j ]
		
			if not posLegal( newPos ):
				continue
			
			if boardIndex( newPos ) == " ":
				legal.append( newPos )
				continue
		
			# This means there is a piece on the new pos
			if boardIndex( newPos )[1] != piece[1]: # Different color => enemy
				legal.append( newPos )
			else: # Friendly, not allowed
				continue
				
	# More processing needed, king is not allowed to check himself.
	#Fuck this shit
#	for iter, move in enumerate( legal ):
#		for i in range( 0, 8 ):
#			for j in range( 0, 8 ):
#				enemyPos = [ i, j ]
#				if boardIndex( enemyPos ) != " " and boardIndex( enemyPos )[1] != piece[1]: # Enemy
#					for enemyMove in legalMoves( enemyPos ):
#						if boardIndex( enemyPos )[0] == pieces["pawn"]:
#							if enemyPos[1] == enemyMove[1]:
#								continue # Pawns are only a threat diagonally
#						if move == enemyMove:
#							legal.pop( iter )
	
	return legal
	
def isKingCheck( color ):
	kingPos = board.findKing( color )
	for i in range( 0, 8 ):
		for j in range( 0, 8 ):
			enemyPos = [ i, j ]
			enemy = boardIndex( enemyPos )
			if enemy == " " or enemy[1] == color: # Empty or friend
				continue
				
			for enemyMove in legalMoves( enemyPos ):
				if enemy[0] == pieces["pawn"]:
					if enemyPos[1] == enemyMove[1]:
						continue # Pawns are only a threat diagonally
				
				if enemyMove == kingPos:
					return True
	
	return False
	
def isKingMate( color ):
	# Check if king is even mate before checking moves
	if not isKingCheck( color ):
		return False	
	kingPos = board.findKing( color )
	oldBoard = board.getBoardCopy() # Fuck this shallow copy shit
	kingMate = True
	for move in legalMoves( kingPos ):
		board.setBoardCopy( oldBoard )
		board.movePiece( kingPos, move )

		if not isKingCheck( color ):
			kingMate = False
			break
		
	# King is mate if no "not-checks" are found
	board.setBoard( oldBoard ) # Revert board
	return kingMate	
	
def movePiece( pos, to ):
	if not posLegal( to ):
		raise exceptions.IllegalPositionException
	
	allowed = False
	for move in legalMoves( pos ):
		if move == to:
			allowed = True
			break
			
	if not allowed:
		raise exceptions.IllegalMoveException
	
	boardCopy = board.getBoardCopy()
	board.movePiece( pos, to )
	
	if isKingCheck( boardIndex( to )[1] ):
		board.setBoard( boardCopy ) # Revert move
		raise exceptions.SelfCheckException # Cannot check self
	
	