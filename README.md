# 🎮 Game Hub

콘솔에서 즐기는 미니 게임 모음입니다. (GitHub 협업 실습 프로젝트)

## 실행 방법

```bash
python -m venv venv
# Windows: venv\Scripts\activate    /  macOS·Linux: source venv/bin/activate
pip install -r requirements.txt
python main.py
```

## 팀원 소개

> **[충돌 지점 ③]** 자기 이름 줄을 채워 주세요. (모두 같은 표를 고치므로 충돌이 납니다!)

| 역할 | 이름              | GitHub ID          | 담당                                            |
| ---- | ----------------- | ------------------ | ----------------------------------------------- |
| A    | 박채환               | nyarq              | 팀장 · `main.py`, `utils.py`, README, 병합 관리 |
| B    | 이승재            | foam0315           | `games/hangman.py` (행맨)                       |
| C    | 유수포프 사이드한 | Seidkhan-Yusupov   | `games/baseball.py` (숫자 야구)                 |
| D    | 변시우            | byunsiwoo106-pixel | `games/rps.py` (가위바위보)                     |
| E    | 김다현            | dreamingh07        | `games/tictactoe.py` (틱택토)                   |

## 게임 목록

| 게임       | 설명                                                                                  | 상태 |
| ---------- | ------------------------------------------------------------------------------------- | ---- |
| 행맨       | 영어 알파벳을 입력해 숨겨진 단어를 맞히는 게임                                        | ✅   |
| 숫자 야구  | 서로 다른 숫자 3개를 추측하며 스트라이크와 볼로 정답을 맞히는 게임 (한국어/영어 지원) | ✅   |
| 가위바위보 | 컴퓨터와 가위바위보를 겨루는 게임                                                                     | ✅   |
| 틱택토     | 3×3 칸에 O와 X를 번갈아 표시하여 한 줄을 먼저 완성하는 게임                           | ✅   |

## 협업 규칙

- `main` 브랜치에는 **직접 push 하지 않습니다.** 반드시 Pull Request!
- 브랜치 이름: `feature/<게임이름>` (예: `feature/hangman`)
- 커밋 메시지: `feat:` `fix:` `test:` `docs:` `chore:` 로 시작 (예: `feat: 행맨 글자 마스킹 함수 추가`)
- PR은 **다른 팀원 1명 이상의 승인** 후 병합합니다.
- 비밀번호·토큰·`.env`는 절대 커밋하지 않습니다.
