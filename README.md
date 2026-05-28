# OTT 플랫폼 데이터 분석 프로젝트

OTT 서비스를 예시로 잡고, 회원 정보부터 시청 기록, 리뷰 데이터까지 직접 설계해서 분석해보는 프로젝트입니다.

넷플릭스나 티빙 같은 서비스를 생각하면서 `어떤 콘텐츠가 많이 시청되는지`, `요금제별로 시청 시간이 다른지`, `연령대별 선호 장르가 있는지`를 SQL로 확인하는 방식으로 진행했습니다.

## 사용한 도구

- GitHub: 팀원별 SQL 파일 공유
- Supabase: 테이블 생성, 데이터 입력, SQL 실행
- VS Code: SQL 파일 작성 및 GitHub 업로드

## 폴더 구조

```text
ott_analysis_project/
  sql/
    01_create_tables.sql
    02_insert_sample_data.sql
    03_analysis_queries.sql
```

## 실행 방법

이 프로젝트는 따로 프로그램을 실행하는 방식이 아니라, Supabase의 SQL Editor에서 SQL 파일을 순서대로 실행하면 됩니다.

### 1. 테이블 생성

먼저 아래 파일의 내용을 Supabase SQL Editor에 붙여넣고 실행합니다.

```text
ott_analysis_project/sql/01_create_tables.sql
```

생성되는 테이블은 총 5개입니다.

- `plans`: 요금제 정보
- `users`: 회원 정보
- `contents`: 콘텐츠 정보
- `viewing_history`: 시청 기록
- `reviews`: 리뷰 정보

실행 후에는 Supabase의 Table Editor에서 테이블이 잘 만들어졌는지 확인합니다.

### 2. 샘플 데이터 입력

테이블 생성이 끝나면 샘플 데이터를 넣습니다.

```text
ott_analysis_project/sql/02_insert_sample_data.sql
```

데이터는 아래 순서로 들어가야 합니다.

```text
plans → users → contents → viewing_history → reviews
```

`users`가 `plans`를 참조하고, `viewing_history`와 `reviews`가 `users`, `contents`를 참조하기 때문에 순서가 중요합니다.

### 3. 분석 쿼리 실행

데이터 입력까지 끝난 뒤 아래 파일의 쿼리를 실행합니다.

```text
ott_analysis_project/sql/03_analysis_queries.sql
```

분석한 내용은 아래와 같습니다.

- 인기 콘텐츠 TOP 5
- 요금제별 평균 시청 시간
- 연령대별 선호 장르
- 장르별 평균 평점
- 콘텐츠별 완주율
- 기기별 시청 비율
- 월별 시청량 변화
- 완주 여부에 따른 평균 평점 비교

처음에는 전체를 한 번에 실행하기보다, 쿼리 하나씩 실행하면서 결과를 확인하는 게 좋습니다.

## 라이브러리 설치

SQL 분석만 할 경우에는 따로 설치할 라이브러리가 없습니다.

그래프를 파이썬으로 만들 경우에는 아래 라이브러리를 설치하면 됩니다.

```powershell
pip install pandas matplotlib
```

## 팀 역할

| 담당 | 역할 | 작업 내용 |
|---|---|---|
| 1번 | DB 설계 / 테이블 생성 SQL | 테이블 구조 정리, 컬럼명과 자료형 설정, PK/FK 설정 |
| 2번 | 가상 데이터 생성 / insert | 회원, 요금제, 콘텐츠, 시청 기록, 리뷰 데이터 작성 |
| 3번 | SQL 분석 쿼리 작성 | 인기 콘텐츠, 요금제별 시청 시간, 선호 장르, 평점, 완주율 분석 |
| 4번 | 결과 정리 / 그래프 제작 | 쿼리 결과를 표와 그래프로 정리 |
| 5번 | GitHub / Supabase 관리 + 결론 도출 | 파일 정리, DB 확인, README 작성, 최종 결론 정리 |

## Git 사용 방법

팀원이 올린 최신 파일을 받을 때는 아래 명령어를 사용합니다.

```powershell
git pull
```

내가 작업한 파일을 올릴 때는 아래 순서로 진행합니다.

```powershell
git status
git add 파일경로
git commit -m "커밋 메시지"
git push
```

예시:

```powershell
git add ott_analysis_project/sql/03_analysis_queries.sql
git commit -m "Add OTT analysis queries"
git push
```

## 주의할 점

- GitHub에 SQL 파일을 올린다고 Supabase에 자동으로 반영되지는 않습니다.
- 실제 테이블 생성과 데이터 입력은 Supabase SQL Editor에서 직접 실행해야 합니다.
- Supabase를 팀원들이 같이 보려면 같은 프로젝트에 초대되어 있어야 합니다.
- 비밀키나 service role key 같은 정보는 GitHub에 올리면 안 됩니다.
