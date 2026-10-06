from games.baseball import judge, make_answer


def test_make_answer():
    answer = make_answer()

    assert len(answer) == 3
    assert answer.isdigit()
    assert len(set(answer)) == 3


def test_judge():
    assert judge("371", "371") == (3, 0)
    assert judge("371", "317") == (1, 2)
    assert judge("371", "456") == (0, 0)
