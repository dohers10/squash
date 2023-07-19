class Player:
    def __init__(self, name):
        self.name = name
        self.games_played = 0
        self.games_won = 0
        self.points_scored = 0
        self.points_conceded = 0
        self.total_points = 0
        self.red_frogs = 0

    def update_stats(self, won, points_scored, points_conceded):
        self.games_played += 1
        self.games_won += won
        self.points_scored += points_scored
        self.points_conceded += points_conceded
        if won:
            self.total_points += 3
        if points_scored == 0:
            self.red_frogs += 1


def play_game(player1, player2):
    p1_score, p2_score = 0, 0
    while True:
        try:
            p1_score = int(input(f"{player1.name} score: "))
            p2_score = int(input(f"{player2.name} score: "))
        except ValueError:
            print("Invalid input. Please enter integer scores.")
            continue

        if p1_score < 0 or p2_score < 0:
            print("Invalid input. Scores cannot be negative.")
            continue

        if p1_score == p2_score:
            print("Scores cannot be equal. Keep playing fools! (or fix typo)")
            continue

        if abs(p1_score - p2_score) < 2:
            print("Scores must have a difference of at least 2 points.")
            continue

        if p1_score == 0:
            print("Red frogs heading your way, son.")
            continue
        
        if p2_score == 0:
            print("Red frogs heading your way, son.")
            continue
            
        break

    if p1_score > p2_score:
        player1.update_stats(1, p1_score, p2_score)
        player2.update_stats(0, p2_score, p1_score)
        return player1.name
    else:
        player1.update_stats(0, p1_score, p2_score)
        player2.update_stats(1, p2_score, p1_score)
        return player2.name


def round_robin(players):
    num_players = len(players)
    num_rounds = 2

    for round_num in range(1, num_rounds + 1):
        print(f"\n---- Round {round_num} ----")

        # Allow the user to choose the order of players for this round
        player_order = []
        for i in range(num_players):
            player_order.append(input(f"Enter Player {i+1}'s position (1 to {num_players}): "))
        
        try:
            player_order = [int(position) for position in player_order]
            if len(set(player_order)) != num_players:
                raise ValueError("Invalid input. Each position must be unique.")
            if not all(1 <= position <= num_players for position in player_order):
                raise ValueError("Invalid input. Positions must be in the range 1 to num_players.")
        except ValueError as ve:
            print(ve)
            return

        round_matches = [(players[i-1], players[j-1]) for i, j in zip(player_order, player_order[1:] + [player_order[0]])]

        for match in round_matches:
            print(f"{match[0].name} vs {match[1].name}")
            winner = play_game(match[0], match[1])
            print(f"{winner} wins!")


def print_league_table(players):
    print("\nLeague Table:")
    print("{:<10} {:<12} {:<10} {:<10} {:<16} {:<16} {:<10} {:<10}".format(
        "Player", "Games Played", "Games Won", "Games Lost",
        "Points Scored", "Points Conceded", "Total Points", "Red Frogs"))
    for player in players:
        print("{:<10} {:<12} {:<10} {:<10} {:<16} {:<16} {:<10} {:<10}".format(
            player.name, player.games_played, player.games_won,
            player.games_played - player.games_won, player.points_scored,
            player.points_conceded, player.total_points, player.red_frogs))


def main():
    # Gather additional information
    matchday_number = int(input("Enter the Matchday number: "))
    court_number = input("Enter the Court number: ")
    new_ball = input("Is a new ball being used? (yes or no): ").lower() == "yes"
    # Input player names
    player_names = [input(f"Enter name for Player {i+1}: ") for i in range(3)]
    players = [Player(name) for name in player_names]

    # Play the round-robin matches
    round_robin(players)

    # Display the league table
    print_league_table(players)


if __name__ == "__main__":
    main()
