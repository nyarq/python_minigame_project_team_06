import random

GAME_NAME = "숫자 야구"


def make_answer() -> str:
    digits = "0123456789"
    picked = random.sample(digits, 3)
    return "".join(picked)


def judge(answer: str, guess: str) -> tuple[int, int]:
    strike = 0
    ball = 0

    for i in range(3):
        if guess[i] == answer[i]:
            strike += 1
        elif guess[i] in answer:
            ball += 1

    return strike, ball


def play() -> None:
    """한 판을 진행한다. 끝나면 return 하여 메인 메뉴로 돌아간다."""
    lang = input("언어 선택 / Select language (ko/en): ").lower()
    answer = make_answer()

    for attempt in range(1, 10):
        if lang == "en":
            guess = input(f"[{attempt}/9] Enter 3 different digits: ")
        else:
            guess = input(f"[{attempt}/9] 서로 다른 숫자 3개를 입력하세요: ")

        if len(guess) != 3 or not guess.isdigit() or len(set(guess)) != 3:
            if lang == "en":
                print("Please enter 3 different digits.")
            else:
                print("서로 다른 숫자 3개를 입력하세요.")
            continue

        strike, ball = judge(answer, guess)

        if lang == "en":
            print(f"{strike} Strike, {ball} Ball")
        else:
            print(f"{strike} 스트라이크, {ball} 볼")

        if strike == 3:
            print("Correct!" if lang == "en" else "정답입니다!")
            return

    if lang == "en":
        print(f"Game over! The answer was {answer}.")
    else:
        print(f"게임 오버! 정답은 {answer}입니다.")
