from Dice import Dice


class Table:
    def __init__(self):
        self.play()

    def play(self):
        self.player1_turn()
        self.player2_turn()

    def player1_turn(self):
        self.player1_dice = []
        for _ in range(5):
            self.player1_dice.append(Dice())

    def player2_turn(self):
        pass

    def hand_result(self):
        pass

    def parse_input(self, input):
        pass

    def choose_move(self):
        pass

    def reroll(self, numbers):
        pass

    def pass_game(self):
        pass

    def choose_winner(self):
        pass

    def print_hand(self, set):
        hand_rows = []
        for row_index in range(5):
            row = []
            for element in set:
                face = getattr(element, "face")
                row.append(face[row_index])
            hand_rows.append(" ".join(row))
        print(hand_rows)