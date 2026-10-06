"""행맨 게임 — 담당 B."""

import random

GAME_NAME = "행맨"
WORDS = ("apple", "banana", "python", "school", "computer", "window", "keyboard", "monitor", "coffee", "github")
MAX_CHANCES = 6


def mask_word(word: str, guessed: set[str]) -> str:
    """맞힌 글자는 보여 주고 나머지는 밑줄로 표시한다."""
    return " ".join(letter if letter in guessed else "_" for letter in word)


def is_solved(word: str, guessed: set[str]) -> bool:
    """단어의 모든 글자를 맞혔는지 확인한다."""
    return all(letter in guessed for letter in word)


def play() -> None:
    """한 판을 진행한 뒤 메인 메뉴로 돌아간다."""
    word = random.choice(WORDS)
    guessed: set[str] = set()
    chances = MAX_CHANCES

    print(f"\n[{GAME_NAME}] 영어 알파벳을 한 글자씩 입력하세요.")
    print("틀릴 수 있는 기회는 6번입니다.")

    while chances > 0 and not is_solved(word, guessed):
        print("\n단어:", mask_word(word, guessed))
        print(f"남은 기회: {chances}")
        print("입력한 글자:", " ".join(sorted(guessed)) or "없음")

        letter = input("알파벳 한 글자: ").strip().lower()

        if len(letter) != 1 or not ("a" <= letter <= "z"):
            print("영어 알파벳 한 글자만 입력하세요.")
            continue

        if letter in guessed:
            print("이미 입력한 글자입니다. 다른 글자를 입력하세요.")
            continue

        guessed.add(letter)

        if letter in word:
            print("맞혔습니다!")
        else:
            chances -= 1
            print("단어에 없는 글자입니다.")

    if is_solved(word, guessed):
        print(f"성공! 정답은 {word}입니다.")
    else:
        print(f"실패! 정답은 {word}입니다.")

    print("메인 메뉴로 돌아갑니다.")
