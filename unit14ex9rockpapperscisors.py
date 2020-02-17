"""
 Write a class called Rock_paper_scissors that implements the logic of the game Rockpaper-scissors. 
 For this game the user plays against the computer for a certain number of rounds. Your class should 
 have ﬁelds for the how many rounds there will be, the current round number,and the number o fwins 
 each player has. There should be methods for getting the computer’schoice,ﬁnding the winner of a 
 round,and checking to see if someone has one the (entire) game. You may want more methods."""

class Rock_paper_scissors:
    def __init__(self,L):
        self.L = L

    def __str__(self):
        return ','.join(self.L)

