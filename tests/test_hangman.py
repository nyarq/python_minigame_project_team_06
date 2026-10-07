from games.hangman import is_solved, mask_word


def test_mask_word_no_guesses():
    assert mask_word("apple", set()) == "_ _ _ _ _"


def test_mask_word_partial():
    assert mask_word("apple", {"a", "p"}) == "a p p _ _"


def test_mask_word_complete():
    assert mask_word("apple", set("apple")) == "a p p l e"


def test_is_solved_false():
    assert not is_solved("apple", {"a", "p", "l"})


def test_is_solved_true():
    assert is_solved("apple", set("apple"))
