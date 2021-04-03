**Snake & Ladder with No Graphics**

In this project we will develop a Snake and Ladder game. However, we have made things a bit easy for ourselves by avoiding graphics and slightly changing the rules of the game. Rules of our Snake and Ladder are as follows:
1) We have just 1 player in the game.
2) The player starts at 0 and wins the game on reaching 100.
3) There should be at least 3 ladders in the game. 
4) There should be at least 3 snakes in the game. 
5) You can define (start, end)  points of the snakes and ladders on your own. 
6) You will roll a dice that should produce an integer value in the range [1, 6]. The produced integer value should be random. (Use random function to generate the output)
7) Your player can have 2 states -(i) AtHome (ii) RoamFree. 

When the game begins, the player is at position 0 and its state is AtHome.
The player can only move forward once its state turns to RoamFree. For the state to turn to RoamFree, it is necessary for the dice to show a value of 6. 
Once the state of the player is RoamFree, the player is eligible to move forward. Thus, any time the dice is rolled and the state of the player is RoamFree, the player will move forward. For eg.,
 
 
 if the current position of the player is 0 **and** the current state is RoamFree **and** the dice shows 3
	The new position will become old position + new position i.e. 0 + 3 = 3
	
Once the player reaches a new position that is the lower point of the ladder, the player’s position will automatically be changed to the higher point of the ladder. For eg., 
	if the current position of the player is 3 **and** the current state is RoamFree, **and** The dice shows 2
		The position will become 5 **and** 
		if this position i.e. 5 is the starting point of a ladder that ends at 10,
			The final position of the player would become 10.
			
Similarly, once the player reaches a new position that is the mouth of the snake, the player’s position will automatically be changed to the tail of the snake.
To win the game the player should exactly reach 100. In case the player is at 98, there are just 2 valid moves that the player can make. 
	If the dice shows 1, the player shifts to 99 and the game is still on.
	If the dice shows 2, the player shifts to 100 and wins the game.
	For any value of dice >= 3 the player can’t move and will remain at its own position while the game is still on.
	
	


Note that this is an interactive problem, in which the user will press enter when the die is supposed to be rolled.

Your Output Should somewhat like this :


----------------------------- Total Dice rolls before this: 0 ----------------------------------

Ladders: [(5, 10), (18, 59), (79, 100)]
Snakes: [(11, 7), (27, 4), (82, 63)]
CurrentPosition: 0
CurrentState: AtHome
Press 1 to roll a die and 2 to exit!!
Pressed 1, rolling a die
Dice value: 5

After the dice is rolled:
CurrentPostion: 0
PlayerState: AtHome
---------------------------------------------------------------


----------------------------- Total Dice rolls before this: 1 ----------------------------------

Ladders: [(5, 10), (18, 59), (79, 100)]
Snakes: [(11, 7)]
CurrentPosition: 0
CurrentState: AtHome
Press 1 to roll a die and 2 to exit!!
Pressed 1, rolling a die
Dice value: 6

After the dice is rolled:
CurrentPostion: 0
PlayerState: RoamFree
---------------------------------------------------------------

-----------------------------Total Dice rolls before this: 2 ----------------------------------

Ladders: [(5, 10), (18, 59), (79, 100)]
Snakes: [(11, 7)]
CurrentPosition: 0
CurrentState: RoamFree
Press 1 to roll a die and 2 to exit!!
Pressed 1, rolling a die
Dice value: 5

After the dice is rolled:
CurrentPostion: 10 (Since it gets a ladder)
PlayerState: RoamFree
---------------------------------------------------------------

----------------------------Total Dice rolls before this: 3-----------------------------------

Ladders: [(5, 10), (18, 59), (79, 100)]
Snakes: [(11, 7)]
CurrentPosition: 10
CurrentState: RoamFree
Press 1 to roll a die and 2 to exit!!
Pressed 1, rolling a die
Dice value: 1

After the dice is rolled:
CurrentPostion: 7 (Since it is bit by a snake)
PlayerState: RoamFree
---------------------------------------------------------------

This keeps on going till the very end, when we reach a situation like

------------------------- Total Dice rolls before this: 28 --------------------------------------

Ladders: [(5, 10), (18, 59), (79, 100)]
Snakes: [(11, 7)]
CurrentPosition: 98
CurrentState: RoamFree
Press 1 to roll a die and 2 to exit!!
Pressed 1, rolling a die
Dice value: 2

After the dice is rolled:
CurrentPostion: 100 (Since it is bit by a snake)
PlayerState: RoamFree

Hurray you won!! Bye bye :)
---------------------------------------------------------------




