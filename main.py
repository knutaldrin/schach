from movelogic import legalMoves, movePiece, isKingCheck, isKingMate, movePiece, posLegal
from printing import printBoard
from board import colors, pieces
import board
from exceptions import *
import printing

board.resetBoard()

def main():
	while( True ):
		printing.clearScreen()
		print( "Velkommen til Knuts sjakk-simulator 3000!" )
		print( "Vil du spille et parti sjakk?" )
		a = input()
		if a == "":
			continue
		if a[0].lower() != "j" and a[0].lower() != "y":
			print( "Du kommer i alle fall ikke å bli verdensmester hvis du ikke en gang vil prøve!" )
			exit()
		else:
			break
		
	printing.clearScreen()
	
	print( "Hvit og svart spiller annenhver tur. Hvit begynner." )
	print( "Du flytter ved å skrive brikkeposisjon og den du vil flytte til." )
	print( "Ex. \"b7b5\" flytter bonden på b7 til b5." )
	print( "Trykk enter for å starte!" )
	input()
	
	# YEEEAH
	#printing.printBoard()
	
	whoseTurn = colors["white"]
	
	while( True ):
		printing.printBoard()
		
		if whoseTurn == colors["white"]:
			if isKingMate( colors["white"] ):
				printing.print_red( "HVIT ER SJAKK MATT! GRATULERER, SVART!" )
				break
			elif isKingCheck( colors["white"] ):
				printing.print_red( "Hvits konge er satt i sjakk." )
			
			print( "Hvits tur!" )
		if whoseTurn == colors["black"]:
			if isKingMate( colors["black"] ):
				printing.print_red( "SVART ER SJAKK MATT! GRATULERER, HVIT!" )
				break
			elif isKingCheck( colors["black"] ):
				printing.print_red( "Svartss konge er satt i sjakk." )
			
			print( "Svarts tur!" )
			
		print( "Hva vil du flytte? (fratil)" )
		print( "Skriv q for å avslutte" )
		while( True ):
			a = input()
			if a.lower() == "q":
				print( "Ha det bra!" )
				exit()
		
			if len( a ) != 4:
				print( "Skriv posisjon du vil flytte fra og til (ex. a4b7)" )
				continue
		
			frompos, topos = str2pos( a )
		
			if not posLegal( frompos ) or not posLegal( topos ):
				print( "Du kan ikke flytte utenfor brettet!" )
				print( "Prøv noe annet!" )
				continue
				
			if board.boardIndex( frompos ) == " ":
				print( "Det står ingen brikke der du vil flytte fra!" )
				print( "Flytt en brikke!" )
				continue
		
			if board.boardIndex( frompos )[1] != whoseTurn:
				print( "Fy fy! Du kan bare flytte dine egne brikker." )
				print( "Prøv en annen!" )
				continue
			
			try:
				movePiece( frompos, topos )
			except SelfCheckException:
				print( "Du kan ikke sette deg selv i sjakk." )
				print( "Prøv noe annet." )
				continue
			except IllegalPositionException:
				print( "Du kan ikke flytte til et sted utenfor brettet." )
				print( "Prøv igjen." )
				continue
			except IllegalMoveException:
				print( "Ugyldig trekk!" )
				print( "Prøv et annet." )
				continue
			except:
				print( "WTF" )
				input()
				
			piece = board.boardIndex( topos )
			if piece[0] == pieces["pawn"]:
				if( ( piece[1] == colors["white"] and topos[0] == 0 ) or
				   ( piece[1] == colors["black"] and topos[0] == 7 ) ):
				   	printing.printBoard()
				   	print( "Gratulerer, du får forfremmet bonden din!" )
				   	print( "Hva vil du ha? (q, k, r, b)" )
				   	while( True ):
				   		lel = input()
				   		lel = lel[:1].lower()
				   		if( lel != "q" and lel != "k" and lel != "r" and lel != "b" ):
				   			print( "Skriv q, k r eller b" )
				   			continue
				   		else:
				   			break
				   	
				   	board.promote( topos, lel )
			
			if whoseTurn == colors["white"]:
				whoseTurn = colors["black"]
			else:
				whoseTurn = colors["white"]
				
			break
				
		
	input()
			
def str2pos( string ):
	string = string.lower()
	y1 = ord( string[:1] ) - 97
	x1 = int( string[1:2] ) - 1
	y2 = ord( string[2:3] ) - 97
	x2 = int( string[3:4] ) - 1
	return [x1, y1], [x2, y2]
	
			
	
main()