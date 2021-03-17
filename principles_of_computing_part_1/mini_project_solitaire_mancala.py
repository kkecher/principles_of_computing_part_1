#!/usr/bin/env python2

"""
Student facing implement of solitaire version of Mancala - Tchoukaillon

Goal: Move as many seeds from given houses into the store

In GUI, you make ask computer AI to make move or click to attempt a legal move
"""


class SolitaireMancala:
    """
    Simple class that implements Solitaire Mancala
    """
    
    def __init__(self):
        """
        Create Mancala game with empty store and no houses
        """
        self._board = [0]
    
    def set_board(self, configuration):
        """
        Take the list configuration of initial number of seeds for given houses
        house zero corresponds to the store and is on right
        houses are number in ascending order from right to left
        """
        self._board = list(configuration)

    
    def __str__(self):
        """
        Return string representation for Mancala board
        """
        # copy list to keep original self._board
        copied_board = list(self._board)
        copied_board.reverse()
        return str(copied_board)
    
    def get_num_seeds(self, house_num):
        """
        Return the number of seeds in given house on board
        """
        try:
            return self._board[house_num]
        except IndexError:
            return 'abs(house_num) should be less len(board).\nlen(board) == %d\nabs(house_num) == %d' % (len(self._board), abs(house_num))

    def is_game_won(self):
        """
        Check to see if all houses but house zero are empty
        """
        house_num = 1
        while house_num < len(self._board):
            if self._board[house_num] != 0:
                return False
            house_num += 1
        return True
    
    def is_legal_move(self, house_num):
        """
        Check whether a given move is legal
        """
        try:
            if house_num < 0:
                house_num = len(self._board) - abs(house_num)
            if house_num == 0 and self._board != []:
                return False
            return self._board[house_num] == house_num
        except IndexError:
            return 'abs(house_num) should be less len(board).\nlen(board) == %d\nabs(house_num) == %d' % (len(self._board), abs(house_num))

    
    def apply_move(self, house_num):
        """
        Move all of the stones from house to lower/left houses
        Last seed must be played in the store (house zero)
        """
        if self._board == []:
            return 'abs(house_num) should be less len(board).\nlen(board) == %d\nabs(house_num) == %d' % (len(self._board), abs(house_num))
        try:
            if house_num < 0:
                house_num = len(self._board) - abs(house_num)
            index = house_num - 1
            while index >= 0 and self._board[house_num] > 0:
                self._board[index] += 1
                self._board[house_num] -= 1
                index -= 1
            return self._board
        except IndexError:
            return 'abs(house_num) should be less len(board).\nlen(board) == %d\nabs(house_num) == %d' % (len(self._board), abs(house_num))
        
    def choose_move(self):
        """
        Return the house for the next shortest legal move
        Shortest means legal move from house closest to store
        Note that using a longer legal move would make smaller illegal
        If no legal move, return house zero
        """
        house_num = 1
        while house_num < len(self._board):
            if self._board[house_num] == house_num:
                return house_num
            house_num += 1
        return 0
    
    def plan_moves(self):
        """
        Return a sequence (list) of legal moves based on the following heuristic: 
		After each move, move the seeds in the house closest to the store 
		when given a choice of legal moves
        Not used in GUI version, only for machine testing
        """
        copied_board = list(self._board)
        legal_moves = []
        legal_move = self.choose_move()
        while legal_move != 0:
            legal_moves.append(legal_move)
            self._board = self.apply_move(legal_move)
            legal_move = self.choose_move()
        self._board = copied_board
        return legal_moves
 
# Create tests to check the correctness of your code

def test_mancala():
    """
    Test code for Solitaire Mancala
    """
    
    my_game = SolitaireMancala()
    print ("Testing init - Computed:", my_game, "Expected: [0]")
    
    config1 = [0, 0, 1, 1, 3, 5, 0]    
    my_game.set_board(config1)   
    
    print ("Testing set_board - Computed:", str(my_game), "Expected:", str([0, 5, 3, 1, 1, 0, 0]))
    print ("Testing get_num_seeds - Computed:", my_game.get_num_seeds(1), "Expected:", config1[1])
    print ("Testing get_num_seeds - Computed:", my_game.get_num_seeds(3), "Expected:", config1[3])
    print ("Testing get_num_seeds - Computed:", my_game.get_num_seeds(5), "Expected:", config1[5])

    # add more tests here
    
#test_mancala()


# Import GUI code once you feel your code is correct
#import poc_mancala_gui
#poc_mancala_gui.run_gui(SolitaireMancala())
