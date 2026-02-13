from game import evaluate_round, normalize_move


def test_evaluate_round_player_wins():
    assert evaluate_round("stein", "schere") == 1
    assert evaluate_round("papier", "stein") == 1
    assert evaluate_round("schere", "papier") == 1


def test_evaluate_round_draw():
    assert evaluate_round("stein", "stein") == 0


def test_evaluate_round_computer_wins():
    assert evaluate_round("stein", "papier") == -1


def test_normalize_move():
    assert normalize_move("Stein") == "stein"
    assert normalize_move("p") == "papier"
    assert normalize_move("sc") == "schere"
    assert normalize_move("x") is None
