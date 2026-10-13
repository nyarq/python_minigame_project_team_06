"""메인 메뉴(main.py) 테스트 — 담당: 팀원 A"""

import main
from games import baseball, hangman, rps, tictactoe


def test_all_games_registered():
    assert main.GAMES == {
        "1": hangman,
        "2": baseball,
        "3": rps,
        "4": tictactoe,
    }


def test_show_menu_lists_every_game(capsys):
    main.show_menu()
    out = capsys.readouterr().out
    for key, game in main.GAMES.items():
        assert f"{key}. {game.GAME_NAME}" in out
    assert "0. 종료" in out


def test_main_exits_on_zero(monkeypatch, capsys):
    monkeypatch.setattr("builtins.input", lambda _: "0")
    main.main()
    assert "안녕히 가세요!" in capsys.readouterr().out


def test_main_rejects_invalid_choice(monkeypatch, capsys):
    answers = iter(["9", "abc", "0"])
    monkeypatch.setattr("builtins.input", lambda _: next(answers))
    main.main()
    assert capsys.readouterr().out.count("올바른 번호가 아닙니다.") == 2


def test_main_runs_selected_game(monkeypatch):
    played = []
    monkeypatch.setattr(rps, "play", lambda: played.append("rps"))
    answers = iter(["3", "0"])
    monkeypatch.setattr("builtins.input", lambda _: next(answers))
    main.main()
    assert played == ["rps"]
