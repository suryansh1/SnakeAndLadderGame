from random import randint

class SnakesAndLadders:

	def __init__(self):
		self.roamFree = False #when this is False, state is AtHome
		self.gameWon = False

		self.dieValue = 0
		self.currentPosition = 0
		self.dieRolls = 0

		self.ladders = {5:10, 18:59, 79:100}
		self.snakes = {11:7, 27:4, 82:63}

	def rollDie(self):
		
		self.dieValue = randint(1,6)
		self.dieRolls += 1
		print("\n\n\t\t Pressed 1, rolling a die\n\n")
		print("\t\t\t Die Value :{}".format(self.dieValue))
		print("\n\n\t\t After die roll :")


	def checkWin(self):

		if self.currentPosition == 100: 
			self.gameWon = True
			print("\t\t Hurray you won in {} die rolls Bye bye :)\n\n\n".format\
												(self.dieRolls))
			print("\t\t --------------------------------------------------------")
			quit()

		return False

	def getState(self):
		retVal = "roamFree" if self.roamFree else "atHome"
		return retVal

	def changeState(self):
		''' Changes the state to roamFree from atHome'''
		self.roamFree = True

	def updatePosition(self):
		''' Changes the currentPosition based on die roll, 
			when in roamFree state'''

		newPosition = self.currentPosition + self.dieValue

		if newPosition > 100:
			print("\t\t Need to get exactly {} to win, on your die roll, try again".
					format(100 - self.currentPosition))

			print("\t\t CurrentPostion: {} (unchanged)".format\
									(self.currentPosition))
			return

		if newPosition in self.snakes:
			self.currentPosition = self.snakes[newPosition]
			print("\t\t CurrentPostion: {} (Since you were bit by a snake)".format\
									(self.currentPosition))

			return

		if newPosition in self.ladders:
			self.currentPosition = self.ladders[newPosition]
			print("\t\t CurrentPostion: {} (Since you climbed a ladder)".format\
									(self.currentPosition))
			return

		self.currentPosition = newPosition
		print("\t\t CurrentPostion: {}".format(self.currentPosition))

	def startGame(self):
		''' Start the game from atHome state '''

		while not self.checkWin():
			print("\t\t -----------Total Die rolls before this: {} -------------".format\
													(self.dieRolls))

			print("\t\t Ladders : {}".format(self.ladders))
			print("\t\t Snakes : {}".format(self.snakes))
			print("\t\t CurrentPostion: {}".format(self.currentPosition))
			print("\t\t CurrentState: {}".format(self.getState()))		

			userInput = int(input("\n\n\t\t\t Press 1 to roll a die and 2 to exit : \t\t")	)

			if userInput == 2:
				print("\t\t Quitting Game, Goodbye ")
				print("\n\n--------------------------------------------------------")
				quit()

			elif userInput == 1:

				self.rollDie()				

				if not self.roamFree:
					if self.dieValue == 6 :	
						self.changeState()

					print("\t\t CurrentPostion: {}".format(self.currentPosition))
					print("\t\t CurrentState: {}".format(self.getState()))		

				else: 
					self.updatePosition()
					print("\t\t CurrentState: {}".format(self.getState()))		


			else:
				print("\t\t Invalid Input, try again")

			print("\t\t --------------------------------------------------------\n\n\n")


def main():

	print("\n\n\t\t Welcome to Snakes And Ladders\n\n")
	print("\n\n\t\t Get a 6 on your die roll, to move into roamFree state\n\n")

	game = SnakesAndLadders()
	game.startGame()

if __name__ == "__main__":
	main()






