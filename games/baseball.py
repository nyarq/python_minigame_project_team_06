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
    answer = make_answer()

    for attempt in range(1, 10):
        guess = input(f"[{attempt}/9] 숫자 3개를 입력하세요: ")

        strike, ball = judge(answer, guess)
        print(f"{strike} 스트라이크, {ball} 볼")

        if strike == 3:
            print("정답입니다!")
            return

    print(f"게임 오버! 정답은 {answer}입니다.")
