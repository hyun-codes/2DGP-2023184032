# Drill #8 — 애니메이션 뷰어

## 스프라이트 출처

- 작품: Blue Knight / Knight and knight animation
- 제작자: ChiliGames
- 출처: https://opengameart.org/content/knight-and-knight-animation
- 원본: https://opengameart.org/sites/default/files/BlueKnightSpriteSheet.png
- 라이선스: CC0 (https://creativecommons.org/publicdomain/zero/1.0/)

교수님 실습 자료의 SamuraiSheet 대신 직접 검색한 기사 시트를 사용합니다.

## 실행

저장소 루트에서 Python과 pico2d가 설치된 환경으로 실행합니다.

```powershell
.\.venv\Scripts\python.exe .\Labs\LEC08_Animation\animation_viewer.py
```

현재 터미널이 `Labs/LEC08_Animation`이라면:

```powershell
python animation_viewer.py
```

이미지는 코드와 같은 폴더에서 불러오므로 실행 위치에 영향을 받지 않습니다.
ESC 또는 창 닫기로 종료합니다. 실습용 `character_runs.py`는 실행에 사용하지 않습니다.

## 구현한 과제 조건

- 소스 파일명: `animation_viewer.py` (기존 LEC08 실습 폴더에 작성).
- 800×600 화면 중앙에서 캐릭터를 4배 확대하여 출력합니다.
- 실제 프레임 높이는 90~121픽셀로, 출력 높이는 360~484픽셀입니다.
  가장 작은 프레임도 화면 높이의 절반인 300픽셀보다 큽니다.
- 각 동작의 전체 프레임을 5회 재생한 뒤 마지막 프레임에서 1초 정지합니다.
- 대기 → 걷기 → 달리기 → 점프 → 공격 → 소환 순서로 무한 반복합니다.
- 동작별로 0.08~0.14초의 프레임 간격을 적용합니다.
- 재생 중과 1초 정지 중 모두 창 닫기 및 ESC 입력을 처리합니다.

| 동작 | 프레임 수 | 프레임 간격 |
| --- | ---: | ---: |
| Idle (대기) | 11 | 0.14초 |
| Walk (걷기) | 10 | 0.11초 |
| Run (달리기) | 10 | 0.08초 |
| Jump (점프) | 10 | 0.10초 |
| Attack (공격) | 10 | 0.10초 |
| Summon (소환) | 9 | 0.12초 |

## 가산점 기능 — 제출 시 명시

1. **프레임마다 크기가 다른 복잡한 Sprite Sheet 지원 (+2점)**
   모든 프레임을 `(left, top, width, height)` 튜플로 개별 저장합니다.
   예를 들어 공격 프레임은 76×97, 107×100, 98×119, 121×96 등 서로 다른
   크기를 실제로 사용합니다. `to_clip_rectangle()`에서
   `bottom = 이미지 높이 - top - height`로 pico2d 좌표로 변환하고,
   `clip_draw()`에서 그 프레임의 너비·높이를 적용합니다.
   출력도 동일한 4배 배율을 사용하므로 비율이 왜곡되지 않습니다.
2. **애니메이션별 서로 다른 프레임 수 지원 (+2점)**
   대기 11프레임, 걷기·달리기·점프·공격 각 10프레임, 소환 9프레임을
   지원합니다. 고정된 프레임 개수를 가정하지 않고 각 동작의 프레임 튜플을
   순회하므로 모든 프레임이 정확히 5회씩 재생됩니다.

제출 설명에 붙여 넣을 문장:

> 불규칙한 Blue Knight Sprite Sheet를 사용해 프레임별 서로 다른 클리핑
> 좌표와 크기를 적용했으며, 동작마다 다른 프레임 수(11·10·9)를 지원했습니다.
> 캐릭터를 중앙에 4배 확대 표시하고, 각 동작을 5회 재생한 뒤 1초 정지하며
> 모든 동작을 차례로 무한 반복하도록 구현했습니다.

## 교수님 LEC08 HTML 반영

`Slides/LEC 08 애니메이션.html`의 `clip_draw()`를 통한 프레임 추출,
이미지의 왼쪽 아래 원점, 확대 출력, 불규칙한 시트의 프레임별 bounding box,
Sprite → Action → Frame 튜플 자료 구조를 반영했습니다.

## 검증

저장소 루트에서:

```powershell
.\.venv\Scripts\python.exe -B -m unittest discover -s Labs/LEC08_Animation -p test_animation_viewer.py -v
```

6개 테스트로 프레임 영역/확대 크기, 두 가산점 조건, 5회 반복 후 1초 정지,
재생/정지 중 종료, ESC/창 닫기, 전체 순환과 캔버스 종료를 확인합니다.
실제 pico2d 소프트웨어 렌더러로 60개 프레임의 출력도 확인했습니다.
커밋은 `drill-08` 브랜치에서 구현 단계별로 기록했습니다.
