"""가위바위보 결과 판정 테스트."""

import pytest

from games.rps import decide


def test_scissors_beats_paper():
    assert decide("가위", "보") == "win"


def test_scissors_loses_to_rock():
    assert decide("가위", "바위") == "lose"


def test_same_choice_is_draw():
    assert decide("보", "보") == "draw"


def test_invalid_choice_raises_value_error():
    with pytest.raises(ValueError):
        decide("연필", "보")
