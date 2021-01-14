from game.thrower import Thrower

class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to keep track of the score and control the 
    sequence of play.
    
    Attributes:
        keep_playing (boolean): Whether or not the player wants to keep playing.
        score (number): The total number of points earned.
        thrower (Thrower): An instance of the class of objects known as Thrower.
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        self.keep_playing = True
        self.score = 0
        self.thrower = Thrower()

    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.keep_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means throwing the dice.

        Args:
            self (Director): An instance of Director.
        """
        self.thrower.throw_dice()
        
    def do_updates(self):
        """Updates the important game information for each round of play. In 
        this case, that means updating the score.

        Args:
            self (Director): An instance of Director.
        """
        points = self.thrower.get_points()
        self.score += points
        
    def do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means the dice that were rolled and the score.

        Args:
            self (Director): An instance of Director.
        """
        print(f"\nYou rolled: {self.thrower.dice}")
        if self.thrower.can_throw():
            print(f"Your score is: {self.score}")
            choice = input("Roll again? [y/n] ")
            self.keep_playing = (choice == "y")
            if choice != "y":
                if self.score > 1500:
                    print(f"Good Game. You finished with {self.score}")
                    self.keep_playing = False
                elif self.score > 5000:
                    print(f"Great Googly Moogly!!! You finished with {self.score}")
                    print("Ever consider gambling ;) ")
                    self.keep_playing = False
                else:
                    print(f"You finished with {self.score}. I'm sure you could do better.")
        else:
            self.score = 0
            print(f"Your score is: {self.score}")
            print("Better luck next time!")
            self.keep_playing = False