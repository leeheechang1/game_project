# OTT 플랫폼 데이터 분석 프로젝트

넷플릭스, 티빙 같은 OTT 서비스를 가정하고 회원, 요금제, 콘텐츠, 시청 기록, 리뷰 데이터를 설계한 뒤 Supabase에서 SQL로 분석하는 팀 프로젝트입니다.

## 프로젝트 목표

- OTT 서비스에 필요한 데이터베이스 테이블 설계
- 가상 데이터 삽입
- SQL을 이용한 사용자 행동 분석
- 분석 결과를 표와 그래프로 정리
- GitHub와 Supabase를 이용한 팀 협업

## 사용 도구

- GitHub: SQL 파일 공유와 팀원 작업 관리
- Supabase: 데이터베이스 생성, 데이터 입력, SQL 분석 실행
- VS Code: SQL 파일 작성 및 GitHub push

## 폴더 구조

```text
ott_analysis_project/
  sql/
    01_create_tables.sql
    02_insert_sample_data.sql
    03_analysis_queries.sql
```

## 실행 전 준비

이 프로젝트는 기본적으로 Supabase SQL Editor에서 실행하므로 별도 파이썬 라이브러리 설치가 필요하지 않습니다.

그래프를 파이썬으로 만들 경우에만 아래 라이브러리를 설치하면 됩니다.

```powershell
pip install pandas matplotlib
```

## 실행 순서

Supabase 프로젝트에 접속한 뒤 왼쪽 메뉴에서 `SQL Editor`를 엽니다.

아래 순서대로 SQL 파일 내용을 복사해서 실행합니다.

### 1. 테이블 생성

먼저 테이블을 만듭니다.

```text
ott_analysis_project/sql/01_create_tables.sql
```

생성되는 테이블:

- `plans`: 요금제 정보
- `users`: 회원 정보
- `contents`: 콘텐츠 정보
- `viewing_history`: 시청 기록
- `reviews`: 리뷰 정보

실행 후 Supabase의 `Table Editor`에서 위 5개 테이블이 보이는지 확인합니다.

### 2. 가상 데이터 입력

테이블 생성이 끝난 뒤 샘플 데이터를 넣습니다.

```text
ott_analysis_project/sql/02_insert_sample_data.sql
```

데이터 입력 순서:

```text
plans → users → contents → viewing_history → reviews
```

외래키 연결 때문에 반드시 위 순서대로 실행해야 합니다.

### 3. 분석 쿼리 실행

데이터 입력이 끝나면 분석 쿼리를 실행합니다.

```text
ott_analysis_project/sql/03_analysis_queries.sql
```

분석 내용:

- 인기 콘텐츠 TOP 5
- 요금제별 평균 시청 시간
- 연령대별 선호 장르
- 장르별 평균 평점
- 콘텐츠별 완주율
- 기기별 시청 비율
- 월별 시청량 변화
- 완주/중도 이탈별 평균 평점 비교

처음 실행할 때는 전체를 한 번에 실행하기보다 쿼리 하나씩 복사해서 실행하는 것을 추천합니다.

## 팀 역할

| 담당 | 역할 | 세부 내용 |
|---|---|---|
| 1번 | DB 설계 / 테이블 생성 SQL | 테이블 목록 확정, 컬럼명과 자료형 정리, PK/FK 설정, 테이블 생성 SQL 작성 |
| 2번 | 가상 데이터 생성 / insert | 회원, 요금제, 콘텐츠, 시청 기록, 리뷰 데이터 생성 및 insert SQL 작성 |
| 3번 | SQL 분석 쿼리 작성 | 인기 콘텐츠, 요금제별 시청 시간, 선호 장르, 평점, 완주율 분석 SQL 작성 |
| 4번 | 결과 정리 / 그래프 제작 | 쿼리 결과를 표와 그래프로 정리 |
| 5번 | GitHub / Supabase 관리 + 결론 도출 | 파일 구조 정리, 테이블/데이터 확인, README 작성, 최종 결론 정리 |

## GitHub에서 최신 파일 받기

팀원이 파일을 올린 뒤에는 VS Code 터미널에서 아래 명령어를 실행합니다.

```powershell
git pull
```

## GitHub에 내 작업 올리기

작업한 파일만 추가해서 올립니다.

```powershell
git status
git add 파일경로
git commit -m "작업 내용 설명"
git push
```

예시:

```powershell
git add ott_analysis_project/sql/03_analysis_queries.sql
git commit -m "Add OTT analysis queries"
git push
```

## 주의사항

- GitHub에 SQL 파일을 올렸다고 Supabase에 자동으로 실행되는 것은 아닙니다.
- Supabase SQL Editor에서 직접 `Run`을 눌러야 실제 테이블과 데이터가 생성됩니다.
- Supabase를 팀원이 같이 보려면 같은 Supabase 프로젝트에 초대되어 있어야 합니다.
- `service_role key` 같은 비밀키는 GitHub에 올리면 안 됩니다.
