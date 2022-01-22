from Dice import Dice


class Table:
    next_move_string = """Select your next move:\npass: "pass"\nwait: "wait"\nroll dice again: numbers from 1 to 5 (from left to right, eg. 1 2 4)\n"""

    def __init__(self):
        self.play()

    def play(self):
        user_input = input("How many players for this round?\n")
        try:
            int(user_input)
        except ValueError:
            print("Wrong value, type an int!")
        else:
            self.player_count = int(user_input)
            self.all_dice = []
            self.players_hands = []
            for turn in range(self.player_count):
                self.player_turn(turn)

    def player_turn(self, turn):
        player_dice = []
        for _ in range(5):
            player_dice.append(Dice())
        print(f"\nPlayer {turn + 1}:")
        self.print_hand(player_dice)
        self.all_dice.append(player_dice)
        self.choose_move(turn)

    def hand_result(self, turn):
        values_counter = [0, 0, 0, 0, 0, 0]
        # count all dice values in a set
        for dice in self.all_dice[turn]:
            values_counter[getattr(dice, "value")-1] += 1


    def parse_input(self, user_input, turn):
        passed = False
        waited = False
        if user_input:
            user_input = user_input.split()
            for element in user_input:
                try:
                    int(element)
                except ValueError:
                    if element == "pass":
                        self.players_hands.append("pass")
                        passed = True
                    else:
                        print("\nChosen wait\n")
                    break
                else:
                    element = int(element)
                    if element in range(1, 6):
                        self.re_roll(element, turn)
        else:
            print("\nChosen wait\n")
        if not passed:
            print(f"\nPlayer {turn+1}'s final hand:")
            self.print_hand(self.all_dice[turn])
            self.hand_result(turn)

    def choose_move(self, turn):
        user_input = input(self.next_move_string)
        self.parse_input(user_input, turn)

    def re_roll(self, number, turn):
        self.all_dice[turn][number-1].roll()

    def choose_winner(self):
        pass

    @staticmethod
    def print_hand(dice_set):
        hand_rows = []
        for row_index in range(5):
            row = []
            for element in dice_set:
                face = getattr(element, "face")
                row.append(face[row_index])
            hand_rows.append(" ".join(row))
        hand_rows = "\n".join(hand_rows)
        print(hand_rows)
