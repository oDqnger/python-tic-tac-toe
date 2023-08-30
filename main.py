class Board:
    def __init__(self):
        self.display_board = [["   |", "   |", "   "], ["   |", "   |", "   "], ["   |", "   |", "   "]]
        self.board = [["", "", ""], ["", "", ""], ["", "", ""]]

    def show_board(self):
        print(*self.display_board[0])
        print(*self.display_board[1])
        print(*self.display_board[2])

    def update_board(self, logo, pos):
        if pos <= 2:
            self.display_board[0][pos] = f" {logo}" if pos == 2 else f" {logo} |"
            self.board[0][pos] = logo
        elif pos <= 5:
            self.display_board[1][pos - 3] = f" {logo}" if pos - 3 == 2 else f" {logo} |"
            self.board[1][pos - 3] = logo
        else:
            self.board[2][pos - 6] = logo
            self.display_board[2][pos - 6] = f" {logo}" if pos - 6 == 2 else f" {logo} |"

    def check_win(self):
        # ROWS
        for rows in self.board:
            if all(cell == "X" for cell in rows):
                return "X"
            elif all(cell == "O" for cell in rows):
                return "O"

        # COLUMNS
        for col in range(3):
            if all(self.board[row][col] == "X" for row in range(3)):
                return "X"
            elif all(self.board[row][col] == "O" for row in range(3)):
                return "O"

        # DIAGONALS
        if all(self.board[i][i] == "X" for i in range(3)) or all(self.board[i][2 - i] == "X" for i in range(3)):
            return "X"
        elif all(self.board[i][i] == "O" for i in range(3)) or all(self.board[i][2 - i] == "O" for i in range(3)):
            return "O"

    def check_tie(self):
        count = 0
        for row in self.board:
            for cell in row:
                if cell == "X" or cell == "O":
                    count += 1

        if count == 9:
            return False

        return True


class PlayerOne:
    def __init__(self, name, logo):
        self.name = name
        self.logo = logo
        self.wins = 0
        self.losses = 0
        self.games_played = 0

    def get_name(self):
        return self.name

    def get_logo(self):
        return self.logo

    def get_wins(self):
        return self.wins

    def get_losses(self):
        return self.losses

    def get_games_played(self):
        return self.games_played

    def change_games(self):
        self.games_played += 1

    def change_stats(self, add_by, loss_by):
        self.games_played += 1
        self.wins += add_by
        self.losses += loss_by


class PlayerTwo:
    def __init__(self, name, logo):
        self.name = name
        self.logo = logo
        self.wins = 0
        self.losses = 0
        self.games_played = 0

    def get_name(self):
        return self.name

    def get_logo(self):
        return self.logo

    def get_wins(self):
        return self.wins

    def get_losses(self):
        return self.losses

    def get_games_played(self):
        return self.games_played

    def change_games(self):
        self.games_played += 1

    def change_stats(self, add_by, loss_by):
        self.games_played += 1
        self.wins += add_by
        self.losses += loss_by


def setup():
    while True:
        player_one_name = input("Player one, enter your name: ")
        player_two_name = input("Player two, enter your name: ")

        if player_two_name == player_one_name:
            print("ERROR! You cannot put the same name as person one has put")
            continue

        break

    while True:
        player_one_logo = input(f"{player_one_name}, would you like to be an x or an o? (x/o)").upper()

        if player_one_logo != "X" and player_one_logo != "O":
            print("Please print either, 'x' or 'o'.")
            continue

        break

    player_two_logo = "O" if player_one_logo == "X" else "X"
    players = [PlayerOne(player_one_name, player_one_logo), PlayerTwo(player_two_name, player_two_logo)]

    return players


def display_stats(player_one, player_two):
    print(f"{player_one.get_name()}: ")
    print(f"Wins: {player_one.get_wins()}")
    print(f"Losses: {player_one.get_losses()}")
    print(f"Games played: {player_one.get_games_played()}")
    print(f"\n{player_two.get_name()}: ")
    print(F"Wins: {player_two.get_wins()}")
    print(f"Losses: {player_two.get_losses()}")
    print(F"Games played: {player_two.get_games_played()}")


def game(player_one, player_two):
    print("\nGame started!\n")
    board = Board()
    board.show_board()
    print(
        "\nTo play, you must first enter the cell number of the board. It starts from 1 in the top left corner \nand goes on horizontally to end with 9 in the bottom right corner.")

    game_loop = True
    current_player = player_two if player_one.get_logo() == "X" else player_one
    all_cells = []

    while game_loop:
        cell_num = 0
        current_player = player_two if current_player == player_one else player_one
        while True:
            try:
                cell_num = int(input(f"{current_player.get_name()}, please enter the cell number: "))
                if cell_num < 1 or cell_num > 9:
                    print("ERROR! You need to type in a number greater or equals to 1 and less than or equals to 9!")
                    continue
                elif cell_num in all_cells:
                    print("ERROR! Someone has already placed their sign there! Please try again.")
                    continue

                break
            except:
                print("ERROR! Please enter a number.")
                continue

        all_cells.append(cell_num)
        board.update_board(current_player.get_logo(), cell_num - 1)

        if (not (board.check_win() == "X" or board.check_win() == "O") == False) and game_loop:
            board.show_board()
            break
        game_loop = board.check_tie()

        board.show_board()

    if board.check_win():
        winner = player_one if board.check_win() == player_one.get_logo() else player_two
        loser = player_two if board.check_win() == player_one.get_logo() else player_one
        print(f"Congratulations {winner.get_name()}, you have won this Tic Tac Toe match!\n")
        winner.change_stats(1, 0)
        loser.change_stats(0, 1)
        display_stats(winner, loser)
    else:
        print("\nThis game is a tie!\n")
        player_one.change_games()
        player_two.change_games()
        display_stats(player_one, player_two)

def main():
    print("Welcome to the text-based tic tac toe game!\n")

    while True:
        prompt = input("Press enter if you're ready to start (must have another person playing in your pc)! ")
        if prompt != "":
            print("ERROR! Wrong character used, please enter to play.")
            continue

        break

    players = setup()
    while True:

        game(players[0], players[1])

        while True:
            prompt = input("Would you like to play again (y/n)? ").lower()
            if prompt == "y":
                prompt = input("Would you like to continue with the same names and settings(y/n)? ").lower()
                if prompt == "y":
                    break
                elif prompt == "n":
                    player_one = input(
                        "Player one name(you can keep this the same as last time, just put the same name as you had last time): ")
                    player_two = input(
                        "Player two name(you can keep this the same as last time, just put the same name as you had last time): ")

                    if player_one == player_two:
                        print("ERROR! You cannot have the same name as the other player")
                        continue

                    while True:
                        player_one_logo = input(f"{player_one}, would you like to be an x or an o? (x/o): ").upper()

                        if player_one_logo != "X" and player_one_logo != "O":
                            print("Please print either, 'x' or 'o'.")
                            continue

                        break
                    player_two_logo = "O" if player_one_logo == "X" else "X"

                    player_one = PlayerOne(player_one, player_one_logo)
                    player_two = PlayerTwo(player_two, player_two_logo)

                    players = [player_one, player_two]

                    game(players[0], players[1])
                    continue


            elif prompt == "n":
                print("\nThanks for playing!")
                exit()
            else:
                print("ERROR! Please type in y or n.")

            continue


if __name__ == "__main__":
    main()
