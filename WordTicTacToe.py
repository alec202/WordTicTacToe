"""Word Tic-Tac-Toe: a word version of Tic-Tac-Toe where three words that have the same letter in the second position
in a row need to match in order to win.

Alec Mirambeau 10/31/2022"""


# Creation of the class that will be used
class ticTacToe:

    # method that determines if the users guess is a valid guess or not
    def chooseWord(self, words, used, word):
        """
        :param words: A list of all the available words that the user can use to play the game
        :param used: A list of all the used words so far from the user's playing the game
        :param word: The word that the user guessed on their turn
        :return: return True if the word the user guessed is in the words list, otherwise return False
        """
        if word in words:
            words.remove(word)
            used.append(word)
            return True
        return False

    # method that will print the board out each time it's called
    def printBoard(self, board):
        """
        :param board: The list of the words that are in a list to represent the board that the users play on
        :return: nothing, prints the board
        """
        count = 0
        for i in range(0, len(board), 1):
            if i == 0 or i == 3 or i == 6:
                print("----------------------")
                print(f"|{board[i]:^6}", end="|")
                count += 1
            else:
                print(f"{board[i]:^6}", end="|")
                count += 1
            if count % 3 == 0:
                print()
        print("----------------------")

    # method to print all of the availble words
    def printAvailableWords(self, words):
        """
        :param words: list of all the available words that the user can input
        :return: nothing, prints all available words the users can use to play the game
        """
        print("The available words to choose from are:", end=" ")
        for i, word in enumerate(words):
            if i == (len(words) - 1):
                print(word, end=". ")
            else:
                print(word, end=", ")

    # method to verify if the position to place the word in is available
    def wordPlaceChecker(self, position, board):
        """
        :param position: The spot on the board the user wants to place their word
        :param board: List of words that are in the current board
        :return: False if the position is unavailable or out of bounds, else return True
        """
        if (type(position) != int) or (position > 8 or position < 0) or (board[position] != ""):
            return False
        return True

    # check the rows for a win
    def checkRows(self, board):
        """
        :param board: List of words that are in the current board
        :return: return True if the user has three words in a row where the second character matches,
        """
        for i in range(0, 9, 3):
            if (len(board[i]) > 0 and len(board[i + 1]) > 0 and len(board[i + 2]) > 0) and \
                    (board[i][1] == board[i + 1][1] == board[i + 2][1]):
                return True
        return False

    # Method to check the colums for a win
    def checkCols(self, board):
        """
        :param board:List of words that are in the current board
        :return: Return True if the player has a win in any of the columns else it returns false
        """
        for i in range(0, 3, 1):
            if ((len(board[i]) > 0 and len(board[i + 3]) > 0 and len(board[i + 6]) > 0) and \
                    (board[i][1] == board[i + 3][1] == board[i + 6][1])):
                return True
        return False

    # method to check for a left diagnol for a win
    def checkLeftDiag(self, board):
        """
        :param board: List of words that are in the current board
        :return: Returns True if the player has a win in the left diagonal, else returns false
        """
        if ((len(board[0]) > 0 and len(board[4]) > 0 and len(board[8]) > 0) and (
                board[0][1] == board[4][1] == board[8][1])):
            return True
        return False

    # method to check for a right diagnol for a win
    def checkRightDiag(self, board):
        """
        :param board: List of words that are in the current board
        :return: Returns True if the player has a win in the right diagonal, else return False
        """
        if ((len(board[2]) > 0 and len(board[4]) > 0 and len(board[6]) > 0) and (
                board[2][1] == board[4][1] == board[6][1])):
            return True
        return False

    # creating the main method of the class
    def main(self):
        """
        :return: nothing, just the main method to run the program
        """
        # initialize variables
        board = ["" for i in range(0, 9)]
        words = ["hen", "bee", "less", "air", "bits", "lip", "soda", "book", "lot"]
        used = []
        # self.count = 0
        self.gameOver = False
        self.player = 0

        # code that does the actual program
        # Code to get a guess from the user until the user enters a valid guess
        while not self.gameOver:
            # assign the player variable with the correct player value of 1 or 2
            self.player += 1
            if self.player % 2 == 0:
                self.player = 2
            else:
                self.player = 1
                # print the board and the available words
            self.printBoard(board)
            self.printAvailableWords(words)
            # get the user's guess and verify it's a valid guess
            # print(f"\nIt is player {self.player}"'s turn to pick a word.')
            user_input = input(f"\nPlayer {self.player} enter a word:\n").lower()
            while not self.chooseWord(words, used, user_input):
                print("That isn't a valid word choice, enter another word")
                user_input = input()

            # get the position for the user's guess and verify it's a valid position
            word_place = int(input("Enter the number for the spot that you want to put your word (0 - 8)\n"))
            while not self.wordPlaceChecker(word_place, board):
                word_place = int(input("Invalid position, enter another position\n"))

            # assign the board with the users guess at the users picked position
            board[word_place] = user_input

            # check if the player has won at all
            if self.checkRows(board) or self.checkCols(board) or self.checkLeftDiag(board) or self.checkRightDiag(
                    board):
                print(f"***************************\nplayer {self.player} won, congrats to them!")
                self.gameOver = True

            # verify that the game is able to continue
            if len(words) == 0:
                print("no more available words so game over")
                self.gameOver = True

        self.printBoard(board)




# main part of the program
if __name__ == "__main__":
    # class declaration and then calling the main method
    run_pr = ticTacToe()
    run_pr.main()
