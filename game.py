import random

MOVES = {
    "stein": "schere",
    "papier": "stein",
    "schere": "papier",
}


def evaluate_round(player_move: str, computer_move: str) -> int:
    """Return 1 if player wins, 0 for draw, -1 if computer wins."""
    if player_move == computer_move:
        return 0
    if MOVES[player_move] == computer_move:
        return 1
    return -1


def normalize_move(raw_input: str) -> str | None:
    move = raw_input.strip().lower()
    aliases = {
        "s": "stein",
        "p": "papier",
        "sc": "schere",
    }
    if move in MOVES:
        return move
    return aliases.get(move)


def play_game() -> None:
    print("=== Schere, Stein, Papier (Singleplayer) ===")
    print("Du spielst gegen den Computer.")
    print("Eingaben: stein, papier, schere oder kurz s, p, sc")

    rounds = 0
    player_score = 0
    computer_score = 0

    while True:
        player_raw = input("\nDein Zug (oder 'ende'): ")
        if player_raw.strip().lower() in {"ende", "quit", "exit"}:
            break

        player_move = normalize_move(player_raw)
        if player_move is None:
            print("Ungültige Eingabe. Bitte stein, papier oder schere wählen.")
            continue

        computer_move = random.choice(list(MOVES.keys()))
        result = evaluate_round(player_move, computer_move)
        rounds += 1

        print(f"Computer wählt: {computer_move}")

        if result == 1:
            player_score += 1
            print("Du gewinnst diese Runde! 🎉")
        elif result == -1:
            computer_score += 1
            print("Computer gewinnt diese Runde.")
        else:
            print("Unentschieden.")

        print(f"Stand nach {rounds} Runde(n): Du {player_score} : {computer_score} Computer")

    print("\n=== Spiel beendet ===")
    print(f"Endstand: Du {player_score} : {computer_score} Computer")
    if player_score > computer_score:
        print("Gesamtsieg für dich! 🏆")
    elif player_score < computer_score:
        print("Der Computer hat gewonnen.")
    else:
        print("Das Spiel endet unentschieden.")


if __name__ == "__main__":
    play_game()
