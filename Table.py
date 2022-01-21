from Dice import Dice


class Table:
    next_move_string = """Select your next move:\npass: "pass"\nwait: "wait"\nroll dice again: numbers from 1 to 5 (from left to right, eg. 1 2 4)\n"""

    def __init__(self):
        self.play()

    def play(self):
        self.player1_turn()
        self.player2_turn()

    # TURNS TO REWRITE, 1 METHOD FOR ALL PLAYERS
    def player1_turn(self):
        self.player1_dice = []
        for _ in range(5):
            self.player1_dice.append(Dice())
        print("player 1:")
        self.print_hand(self.player1_dice)
        self.choose_move(1)

    def player2_turn(self):
        pass

    def hand_result(self, turn):
        pass

    def parse_input(self, user_input, turn):
        user_input = user_input.split()
        if len(user_input) == 1:
            try:
                int(user_input[0])
            except ValueError:
                if user_input[0] == "pass":
                    self.choose_winner(True, turn)
                else:
                    print("\nChosen wait\n")
                    self.hand_result(turn)
        else:
            for number in user_input:
                try:
                    int(number)
                except ValueError:
                    print("\nChosen wait\n")
                    self.hand_result(turn)

    def choose_move(self, turn):
        user_input = input(self.next_move_string)
        self.parse_input(user_input, turn)

    def re_roll(self, numbers):
        pass

    def choose_winner(self, passed=False, player=0):
        if passed == False:
            pass
        else:
            if player == 1:
                print("\nPlayer 2 won!\n")
            else:
                print("\nPlayer 1 won!\n")

    def print_hand(self, set):
        hand_rows = []
        for row_index in range(5):
            row = []
            for element in set:
                face = getattr(element, "face")
                row.append(face[row_index])
            hand_rows.append(" ".join(row))
        hand_rows = "\n".join(hand_rows)
        print(hand_rows)
