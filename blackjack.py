import time
import numpy as np

class Blackjack:
    def __init__(self, delay=1):
        """
        Blackjack class that is used to run a blackjack session keeping track
        of dealer hand and player hands. Follows traditional blackjack rules.
        """
        #initiate playing deck
        self.cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        #counts dealer and player wins
        self.dealer_wins = 0
        self.player_wins = 0
        #used to initiate a blackjack session
        self.session = False
        #delay in seconds to print output
        self.delay = delay
    
    def print_dealer(self, show):
        """
        Helper function used to print the hand of the dealer.
        Parameters
            show: Bool value to show full hand (True) or hide first card (False)
        """
        #initiate output string
        hand = "Dealer Hand: [ "
        #alter string depending if we want to show full cards or not
        if show == True:
            #add dealers cards to output string
            for card in self.dealer:
                hand = hand + str(card) + " , "
            hand = hand[:-2] + "] -> " + str(sum(self.dealer))
        else:
            hand = hand + " * , "
            #add dealers cards to output string
            for card in self.dealer[1:]:
                hand = hand + str(card) + " , "
            hand = hand[:-2] + "] "
        print(hand)
    
    def print_player(self):
        """
        Helper function used to pring the hand of the player
        """
        hand = "Player Hand: [ "
        #add players cards to output string
        for card in self.player:
            hand = hand + str(card) + " , "
        hand = hand[:-2] + "] -> " + str(sum(self.player))
        print(hand)
    
    def evaluate(self):
        """
        Helper function used to evaluate the outcome of a blackjack game comparing
        dealer cards and player cards
        """
        time.sleep(self.delay)
        print("Player Stands, Showing Dealer Hand")
        time.sleep(self.delay)
        self.print_dealer(True)
        #bool value to determine if we are currently playing
        game = True
        while game:
            if sum(self.dealer) < 17:
                #dealer must hit
                time.sleep(self.delay)
                print("Dealer Hits")
                self.dealer.append(np.random.choice(self.cards))
                time.sleep(self.delay)
                self.print_dealer(True)
                #handles hand if there is an Ace value
                if 11 in self.dealer and sum(self.dealer) > 21:
                    self.dealer[self.dealer.index(11)] = 1
                    time.sleep(self.delay)
                    print("Dealer Over 21 changed Ace from 11 to 1")
                    time.sleep(self.delay)
                    self.print_dealer(True)
            elif sum(self.dealer) > 21:
                #dealer busts
                time.sleep(self.delay)
                print("Dealer BUST!!! Player Wins!!!")
                self.player_wins += 1
                game = False
            else:
                #dealer must stand
                time.sleep(self.delay)
                print("Dealer Stands")
                if sum(self.dealer) > sum(self.player):
                    time.sleep(self.delay)
                    print("Dealer wins!")
                    self.dealer_wins += 1
                elif sum(self.dealer) < sum(self.player):
                    time.sleep(self.delay)
                    print("Player wins!")
                    self.player_wins += 1
                else:
                    time.sleep(self.delay)
                    print("There is a draw, Push")
                game = False
    
    def play(self):
        """
        Function used to play 1 game of blackjack
        """
        #initiate dealer and player hands
        self.dealer = list(np.random.choice(self.cards, size=2))
        self.player = list(np.random.choice(self.cards, size=2))
        time.sleep(self.delay)
        self.print_dealer(False)
        time.sleep(self.delay)
        self.print_player()
        #handles blackjack on first two cards
        if sum(self.player) == 21 and sum(self.dealer) != 21:
            print("Blackjack!! Player Wins!!")
            self.player_wins += 1
            game = False
        elif sum(self.player) == 21 and sum(self.dealer) == 21:
            print("PUSH! Both dealer and player have Blackjack!")
            game = False
        else:
            game = True
        #bool value we play the game if no blackjack
        while game:
            time.sleep(self.delay)
            print("H to hit and S to stand or Q to quit")
            action = input()
            #handles player hit action
            if action.lower() == "h":
                #get another card
                self.player.append(np.random.choice(self.cards))
                time.sleep(self.delay)
                self.print_player()
                #handles Ace in hand edgecase
                if 11 in self.player and sum(self.player) > 21:
                    self.player[self.player.index(11)] = 1
                    time.sleep(self.delay)
                    print("Over 21 changed Ace from 11 to 1")
                    time.sleep(self.delay)
                    self.print_player()
                elif sum(self.player) > 21:
                    time.sleep(self.delay)
                    print("BUST!!! Player Loses")
                    self.dealer_wins += 1
                    game = False
            #handles player stand action
            elif action.lower() == "s":
                self.evaluate()
                game = False
            #handles player quit action
            elif action.lower() == "q":
                print("Player Ends Session")
                self.session = False
                game = False

    def blackjack_session(self):
        """
        Function used to run a continuous blackjack session that keeps score
        """
        print("---Initiating BlackJack Session---")
        #initiates a blackjack session
        self.session = True
        while self.session:
            time.sleep(self.delay)
            print("[Score] Player: " + str(self.player_wins) + " Dealer: " + str(self.dealer_wins))
            self.play()
            if not self.session:
                break
            time.sleep(self.delay)
            print("--- Initiating New Game ---")

if __name__ == "__main__":
    Blackjack().blackjack_session()