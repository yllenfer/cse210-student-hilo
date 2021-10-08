# It might have a director and a chooser?
# it should generate random numbers from 1 to 13
# player starts with 300 points
# player should get if the number is higher or lower
# dealer or director displays the card
# player gets 100 points if the card is guessed
# player loses 75 points if card is not guessed
# if player reaches 0 points game is over, otherwise player chooses to continue or not
# If a player decides not to play again the game is over
# from game.player import Player
import random
from game.player import Player


class Dealer:
    def __init__(self):
        self.playing = True
        self.score = 300
        self.player = Player()

    def input(self):
        self.player.get_card_number()

    def start_game(self):
        # if we are playing we need to get stuff
        while self.playing:
            self.out_puts()

    def out_puts(self):
        while self.playing:
            self.player.get_card_number()
            print(f"This card is {self.player.card_number}")
            card_guess = input("Higher or lower? [h/l]: ")
            second_number = random.randint(1, 13)
            # try:
            #     card_guess(int)
            # except:
            #     print("Please enter a letter")
            #     continue
            if second_number >= self.player.card_number and card_guess == "h":
                self.score += 100
            elif second_number <= self.player.card_number and card_guess == "h":
                self.score -= 75
            elif second_number >= self.player.card_number and card_guess == "l":
                self.score -= 75
            elif second_number <= self.player.card_number and card_guess == "l":
                self.score += 100
            elif self.score == 0:
                print("Game over!")
            print(f"Next card was:{second_number}")
            print(f"Your score is: {self.score}")
            keep = input("Keep playing? [y/n]")
            if keep == "y":
                self.playing = True
            elif keep == "n":
                self.playing = False
