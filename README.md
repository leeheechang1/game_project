# 팀3 OTT 플랫폼 데이터 분석

OTT 서비스를 주제로 한 데이터베이스 분석 프로젝트입니다.  
회원, 요금제, 콘텐츠, 시청 기록, 리뷰 데이터를 Supabase에 넣고 SQL로 분석했습니다.

## 사용 도구

- Supabase: 테이블 생성, 데이터 입력, SQL 실행
- GitHub: 팀원별 SQL 파일 공유
- VS Code: SQL 파일 작성 및 push

## 테이블 구조

프로젝트에서 사용하는 테이블은 총 5개입니다.

| 테이블 | 설명 | 주요 컬럼 |
|---|---|---|
| `plans` | OTT 요금제 정보 | `plan_id`, `plan_name`, `monthly_price`, `max_devices`, `video_quality` |
| `users` | 회원 정보 | `user_id`, `email`, `username`, `age`, `gender`, `plan_id`, `join_date` |
| `contents` | 콘텐츠 정보 | `content_id`, `title`, `genre`, `content_type`, `runtime`, `release_date`, `rating_standard` |
| `viewing_history` | 시청 기록 | `history_id`, `user_id`, `content_id`, `viewed_at`, `watched_time`, `device` |
| `reviews` | 리뷰 정보 | `review_id`, `user_id`, `content_id`, `score`, `review_text`, `created_at` |

테이블 관계는 아래처럼 연결됩니다.

```text
plans.plan_id → users.plan_id
users.user_id → viewing_history.user_id
contents.content_id → viewing_history.content_id
users.user_id → reviews.user_id
contents.content_id → reviews.content_id
```

## 파일 위치

현재 분석 쿼리 파일은 아래 위치에 있습니다.

```text
ott_analysis_project/sql/03_analysis_queries.sql
```

이 파일은 3번 담당자가 작성한 SQL 분석 쿼리 모음입니다.

## 실행 순서

Supabase에서 아래 순서로 진행합니다.

1. 테이블 생성 SQL 실행
2. 샘플 데이터 insert SQL 실행
3. 분석 쿼리 실행

테이블과 데이터가 먼저 들어가 있어야 분석 쿼리 결과가 나옵니다.

데이터 입력 순서는 아래처럼 진행하는 것이 안전합니다.

```text
plans → users → contents → viewing_history → reviews
```

`users`는 `plans`를 참조하고, `viewing_history`와 `reviews`는 `users`, `contents`를 참조하기 때문에 순서가 중요합니다.

## 분석 쿼리 내용

`03_analysis_queries.sql`에는 아래 분석이 들어 있습니다.

| 번호 | 분석 내용 | 사용 테이블 |
|---|---|---|
| 1 | 가장 많이 시청된 콘텐츠 TOP 5 | `viewing_history`, `contents` |
| 2 | 요금제별 평균 시청 시간 | `viewing_history`, `users`, `plans` |
| 3 | 연령대별 선호 장르 | `viewing_history`, `users`, `contents` |
| 4 | 장르별 평균 리뷰 점수 | `reviews`, `contents` |
| 5 | 콘텐츠별 완주율 | `viewing_history`, `contents` |
| 6 | 기기별 시청 비율 | `viewing_history` |
| 7 | 월별 시청량 변화 | `viewing_history` |
| 8 | 완주 여부에 따른 평균 리뷰 점수 | `viewing_history`, `contents`, `reviews` |

완주율은 `watched_time`이 콘텐츠 전체 길이인 `runtime`의 90% 이상이면 완주로 계산했습니다.

## 실행 방법

Supabase에서 실행할 때는 아래처럼 하면 됩니다.

1. Supabase 프로젝트 접속
2. 왼쪽 메뉴에서 SQL Editor 클릭
3. `03_analysis_queries.sql` 파일 내용 복사
4. 쿼리를 하나씩 붙여넣고 Run 실행
5. 결과 표를 확인한 뒤 그래프 담당자에게 전달

처음에는 전체 쿼리를 한 번에 실행하기보다 하나씩 실행하는 것이 좋습니다.  
에러가 나면 어떤 쿼리에서 문제가 생겼는지 바로 확인할 수 있습니다.

## 라이브러리 설치

SQL만 실행할 경우 별도 라이브러리 설치는 필요 없습니다.

분석 결과를 파이썬으로 그래프화할 경우 아래 라이브러리를 사용할 수 있습니다.

```powershell
pip install pandas matplotlib
```

## Git 사용

최신 파일을 받을 때:

```powershell
git pull
```

작업한 파일을 올릴 때:

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

- GitHub에 SQL 파일을 올려도 Supabase에 자동으로 실행되지는 않습니다.
- 실제 테이블 생성, 데이터 입력, 분석 실행은 Supabase SQL Editor에서 직접 해야 합니다.
- 같은 DB를 보려면 팀원들이 같은 Supabase 프로젝트에 들어가 있어야 합니다.
- Supabase 비밀키나 service role key는 GitHub에 올리지 않습니다.
