# For Testing

def main():
    matchday_number = int(input("Enter the Matchday number: "))
    court_number = input("Enter the Court number: ")
    new_ball = input("Is a new ball being used? (yes or no): ").lower() == "yes"
    player_names = [input(f"Enter name for Player {i+1}: ") for i in range(3)]
    players = [Player(name) for name in player_names]

    live_matchday = True
    match_results = []

    while live_matchday:
        match_input = input("Enter match result ('name score1 - score2 name', 'name skip - skip name' or 'END'): ")

        if match_input.lower() == "end":
            live_matchday = False
        else:
            try:
                parts = match_input.split()
                if len(parts) == 5 and parts[1] == "skip" and parts[3] == "-":
                    name1, name2 = parts[0], parts[4]
                    if name1 == name2:
                        raise ValueError
                    match_results.append(("skip", None, None, "skip"))
                elif len(parts) == 5 and parts[1] != "skip" and parts[3] == "-" and parts[4] != "skip":
                    name1, score_str1, _, score_str2, name2 = parts
                    score1 = int(score_str1)
                    score2 = int(score_str2)
                    match_results.append((name1, score1, score2, name2))
                else:
                    raise ValueError
            except (ValueError, IndexError):
                print("Invalid input format. Please use 'name score1 - score2 name', 'name skip - skip name', or 'END'.")
                continue

            if name1 != "skip":
                if name1 not in player_names or name2 not in player_names:
                    print("Invalid player names.")
                    continue

                player1 = next(player for player in players if player.name == name1)
                player2 = next(player for player in players if player.name == name2)

                if score1 > score2:
                    update_player_stats(player1, won=True, points_scored=score1, points_conceded=score2)
                    update_player_stats(player2, won=False, points_scored=score2, points_conceded=score1)
                else:
                    update_player_stats(player1, won=False, points_scored=score1, points_conceded=score2)
                    update_player_stats(player2, won=True, points_scored=score2, points_conceded=score1)

    print("\nMatchday finalized. Updating player stats...")
    print_league_table(players)

if __name__ == "__main__":
    main()
