# DB:SQL
### 기존의 데이터 저장 방식
1. 파일(File) 이용
2. 스프레드 시트(Spreadsheet) 이용 예: 엑셀
### 관계형 데이터베이스
데이터 간에 관계가 있는 데이터 항목들의 모음
* 테이블, 행, 열의 정보를 구조화하는 방식
* 서로 관련된 데이터 포인터를 저장하고 이에 대한 액세스를 제공
### 관계
여러 테이블 간의 (논리적) 연결
### PK(primary key), FK(foreign key)
1. pk : 고객의 고유한 id값
2. fk : 누가 어떤 주문을 했는지 식별하기 위한 외래 키
### 관계형 데이터베이스 관련 키워드
1. Table (aka Relation)
  - 데이터를 기록하는 곳
2. Field (aka Column, Attribute)
  - 각 필드에는 고유한 데이터 형식(타입)이 지정됨, 열
3. Record (aka Row, Tuple)
  - 각 레코드에는 구체적인 데이터 값이 저장됨, 행
4. Database (aka Schelma)
  - 테이블의 집합
5. Primary Key (기본 키)
  - 각 레코드의 고유한 값
  - 관계형 데이터베이스에서 레코드의 식별자로 활용
6. Foreign Key (외래 키)
  - 테이블의 필드 중 다른 테이블의 레코드를 식별할 수 있는 키
  - 다른 테이블의 기본 키를 참조
  - 각 레코드에서 서로 다른 테이블 간의 관계를 만드는 데 사용
### DBMS
데이터 베이스를 관리하는 소프트웨어 프로그램
* 데이터 저장 및 관리를 용이하게 하는 시스템
* 데이터베이스와 사용자 간의 인터페이스 역할
* 사용자가 데이터 구성, 업데이트, 모니터링, 백업, 복구 등을 할 수 있도록 도움
### RDBMS
관계형 데이터 베이스를 관리하는 소프트웨어 프로그램
**RDBMS 서비스 종류**
* SQLite
* MySQL
* PostgreSQL
* Oracle Database
### 데이터베이스 정리
* Table은 데이터가 기록되는 곳
* Table에는 행에서 고유하게 식별 가능한 기본 키라는 속성이 있으며, 외래 키를 사용하여 각 행에서 서로 다른 테이블 간의 관계를 만들 수 있음
* 데이터는 기본 키 또는 외래 키를 통해 결합(join)될 수 있는 여러 테이블에 걸쳐 구조화 됨
### SQL(Structure Query Language)
데이터베이스에 정보를 저장하고 처리하기 위한 프로그래밍 언어
### SQL Syntax
* SQL 키워드는 대소문자를 구분하지 않음
  - 하지만 대문자로 작성하는 것을 권장 (명시적 구분)
* 각 SQL Statements의 끝에는 세미콜론(;)이 필요
  - 세미콜론은 각 SQL Statements을 구분하는 방법(명령어의 마침표)
### SQL Statements
SQL을 구성하는 가장 기본적인 코드 블록
```SQL Statements
SELECT column_name FROM table_name;
```
* 해당 예시 코드는 SELECT Statement라 부름
* 이 Statement는 SELECT,FROM 2개의 keyword로 구성 됨
### 수행 목적에 따른 SQL Statements 4가지 유형
1. DDL - 데이터 정의
2. DQL - 데이터 검색
3. DML - 데이터 조작
4. DCL - 데이터 제어

| 유형 | 역할 |SQL키워드|
| ------ | -----------|------------ |
| DDL (Data Definition Language) | 데이터의 기본 구조 및 현식 변경  | CREATE,DROP,ALTER
| DQL (Data Query Language)  | 데이터 검색 | SELECT |
| DML (Data Manipulation Language)| 데이터 조작(추가, 수정, 삭제) | INSERT, UPDATE, DELETE |
| DCL (Data Control Language)| 데이터 및 작업에 대한 사용자 권한 제어 | COMMIT, ROLLBACK, GRANT, REVOKE | 
### Query
* '데이터베이스로부터 정보를 요청'하는 것
* 일반적으로 SQL로 작성하는 코드를 쿼리문(SQL문)이라 함
* 모든 RDBMS에서 SQL 표준을 지원
* 다만 각 RDBMS마다 독자적인 기능에 따라 표준을 벗어나는 문법이 존재하니 주의
### SELECT statement
테이블에서 데이터를 조회
```SQL Statements
SELECT
  select_list
FROM
  table_name;
```
* SELECT 키워드 이후 데이터를 선택하려는 필드를 하나 이상 지정
* FROM 키워드 이후 데이터를 선택하려는 테이블의 이름을 지정
### SELECT 활용1 : 테이블 employees에서 LastName 필드의 모든 데이터를 조회
```SQL Statements
-- 01. Querying data
-- 단일 필드 데이터 조회
SELECT
  LastName
FROM
  employees;

-- 복수 필드 데이터 조회
SELECT
  LastName, FirstName
FROM
  employees;

-- 전체 필드 데이터 조회
SELECT
  *
FROM
  employees;

-- FirstName 전체 필드 데이터 조회(단, 조회시 FirstName이 아닌 '이름'으로 출력되도록 변경
SELECT
  FirstName AS '이름'
FROM
  employees;

-- 테이블 tracks에서 Name, Milliseconds 필드의 모든 데이터 조회(단, Milliseconds 필드는 60000으로 나눠 분 단위 값으로 출력)
SELECT
  Name, Milliseconds / 60000 AS '재생 시간(분)'
FROM
  tracks;
```
### SELECT 정리
* SELECT 문을 사용하여 테이블의 데이터를 조회 및 반환
* '*'(asterisk)를 사용하여 모든 필드 
### ORDER BY statement
조회 결과의 레코드를 정렬
```SQL Statements
SELECT
  select_list
FROM
  table_name
ORDER BY
  column1 [ASC|DESC],
  column2 [ASC|DESC],
  ...;
```
* FROM clause 뒤에 위치
* 하나 이상의 컬럼을 기준으로 결과를 오름차순(ASC, 기본값), 내림차순(DESC) 으로 정렬
```SQL Statements
-- 오름차순으로 정렬
SELECT
  FirstName
FROM
  employees
ORDER BY
  FirstName ASC;

-- 내림차순으로 정렬
SELECT
  FirstName
FROM
  employees
ORDER BY
  FirstName DESC;

-- 테이블 customers에서 Country 필드를 기준으로 내림차순으로 정렬 한 다음 City필드 기준으로 오름차순 정렬하여 조회
SELECT
  Country, City
FROM
  customers
ORDER BY
  Country DESC,
  City ASC;

-- 테이블 tracks에서 Milliseconds 필드를 기준으로 내림차순으로 정렬한 다음 Name,Milliseconds 필드의 모든 데이터를 조회
SELECT
  Name, Milliseconds /60000 AS '재생 시간(분)'
FROM
  tracks
ORDER BY
  Milliseconds DESC;
```
### 정렬에서의 NULL
* NULL 값이 존재할 경우 오름차순 정렬 시 결과에서 NULL이 먼저 출력
```SQL Statements
-- NULL 정렬 예시
SELECT
  ReportsTo
FROM
  employees
ORDER BY
  ReportsTo;
```
### SELECT statement 실행 순서
1. 테이블에서(FROM)
2. 조회하여(SELECT)
3. 정렬 (ORDER BY)
### Filtering data 관련 Keywords
* Clause
  - DISTINCT
  - WHERE
  - LIMIT
* Operator
  - BETWEEN
  - IN
  - LIKE
  - Comparison
  - Logical
### DISTINCT statement
조회 결과에서 중복된 레코드를 제거
```SQL Statements
SELECT DISTINCT
  select_list
FROM
  table_name;
```
```SQL Statements
-- 테이블 customers에서 중복없는 Country 조회
SELECT DISTINCT
  Country
FROM
  customers
ORDER BY
  Country;
```
### WHERE statement
* 조회 시 특정 검색 조건을 지정
```SQL Statements
SELECT
  select_list
FROM
  table_name
WHERE
  search_condition;
```
```SQL Statements
-- 테이블 customers에서 City필드 겂이 'prague'인 데이터의 LastName,FirstName,City 조회
SELECT
  LastName, FirstName, City
FROM
  customers
WHERE
  City = 'Prague';

-- 위와 조건은 같지만 프라하가 아닌 데이터 조회
SELECT
  LastName, FirstName, City
FROM
  customers
WHERE
  City != 'Prague';

-- 테이블 customers에서 Company 필드 값이 NULL이고, Country 필드 값이 'USA'인 데이터의 LastName,FirstName,Company,Country 조회
SELECT
  LastName, FirstName, Company, Country
FROM
  customers
WHERE
  Company IS NULL AND Country = 'USA';

-- 테이블 customers에서 Company 필드 값이 NULL이거나, Country 필드 값이 'USA'인 데이터의 LastName,FirstName,Company,Country 조회
SELECT
  LastName, FirstName, Company, Country
FROM
  customers
WHERE
  Company IS NULL OR Country = 'USA';

-- 테이블 tracks에서 Bytes필드 값이 100000 이상 500000 이하인 데이터의 Name, Bytes조회
SELECT
  Name, Bytes
FROM
  tracks
WHERE
  100000 <= Bytes AND Bytes<= 500000;
  -- Bytes BETWEEN 100000 and 500000;

-- 테이블 tracks에서 Bytes 필드 값이 100000 이상 500000이하인 데이터의 Name,Bytes을 Bytes를 기준으로 오름차순 조회
SELECT
  Name, Bytes
FROM
  tracks
WHERE
  100000 <= Bytes AND Bytes<= 500000
  -- Bytes BETWEEN 100000 and 500000;
ORDER BY
  Bytes;

-- 테이블 customers에서 Country필드 값이 'Canada'또는 'Germany'또는 'France'인 데이터의 LastName,FirstName,Country조회
SELECT
  LastName,FirstName, Country
FROM
  customers
WHERE
  Country IN ('Canada','Germany','France');
  -- Country = 'Canada'
  -- OR Country = 'Germany'
  -- OR Country = 'France';

-- 테이블 customers에서 Country필드 값이 'Canada'또는 'Germany'또는 'France'가 아닌 데이터의 LastName,FirstName,Country조회
SELECT
  LastName,FirstName, Country
FROM
  customers
WHERE
  Country NOT IN ('Canada','Germany','France');

-- 테이블 customers에서 LastName 필드 값이 son으로 끝나는 데이터의 LastName, FirstName 조회
SELECT
  LastName, FirstName
FROM
  customers
WHERE
  LastName LIKE '%son';

-- 테이블 customers에서 FirstName필드 값이 4자리면서 'a'로 끝나는 데이터의 LastName, FirstName 조회
SELECT
  LastName, FirstName
FROM
  customers
WHERE
  FirstName LIKE '___a';
```
### Comparison Operators : 비교 연산자
=, >=, <=, IS, LIKE, IN, BETWEEN, AND
### Logical Operators : 논리 연산자
AND(&&), OR(||), NOT(!)
### IN Operator
값이 특정 목록 안에 있는지 확인
### LIKE Operator
값이 특정 패턴에 일치하는지 확인 (Wildcards와 함께 사용)
### Wildcard Characters
* '%' : 0개 이상의 문자열과 일치 하는지 확인 예시 ('%a' : 마지막 글자가 a인 문자 조회)
* '_' : 단일 문자와 일치하는지 확인 예시 ('___a' : 4글자인 문자중 마지막 글자가 a인 문자 조회)
### LIMIT clause
조회하는 레코드 수를 제한
```SQL
SELECT
  select_list
FROM
  table_name
LIMIT [offset,] row_count;
```
* 하나 또는 두 개의 인자를 사용 (0 또는 양의 정수)
* row_count는 조회하는 최대 레코드 수를 지정
```SQL
-- 테이블 tracks에서 TrackId,Name,Bytes 필드 데이터를 Bytes기준 내림차순으로 7개만 조회
SELECT
  TrackId, Name, Bytes
FROM
  tracks
ORDER BY
  bytes DESC
LIMIT 7;

-- 테이블 tracks에서 TrackId,Name,Bytes 필드 데이터를 Bytes기준 내림차순으로 4번째부터 7번째 데이터만 조회
SELECT
  TrackId, Name, Bytes
FROM
  tracks
ORDER BY
  bytes DESC
LIMIT 3, 4;
-- LIMIT 4 OFFSET 3;
```
### GROUP BY clause
레코드를 그룹화하여 요악본 생성('집계 함수'와 함께 사용)
### Aggregation Functions 집계 함수
값에 대한 계산을 수행하고 단일한 값을 반환하는 함수
* SUM, AVG, MAX, MIN, COUNT
### GROUP BY syntax
```SQL
SELECT
  c1, c2, .... , cn, aggregate_function(ci)
FROM
  table_name
GROUP BY
  c1, c2, ... , cn;
```
* FROM 및 WHERE 절 뒤에 배ㅣ
* GROUP BY 절 뒤에 그룹화 할 필드 목록을 작성
```SQL
-- COUNT 함수가 그룹에 대한 집계된 값을 계산
SELECT
  Country, COUNT(*)
FROM
  customers
GROUP BY
  Country;

-- 테이블 tracks Composer필드를 그룹화하여 각 그룹에 대한 Bytes의 평균 값을 내림차순 조회
SELECT
  Composer, AVG(Bytes)
FROM
  tracks
GROUP BY
  Composer
ORDER BY
  AVG(Bytes) DESC;

-- 에러
-- 테이블 tracks에서 Composer필드를 그룹화하여 각 그룹에 대한 Milliseconds의 평균 값이 10 미만인 데이터 조회(단, Milliseconds 필드는 60000으로 나눠 분 단위 값의 평균으로 계산)
SELECT
  Composer,
  AVG(Milliseconds / 60000) AS avgOfminute
FROM
  tracks
WHERE
  avgOfminute < 10
GROUP BY
  Composer;

-- 에러 해결
SELECT
  Composer,
  AVG(Milliseconds / 60000) AS avgOfminute
FROM
  tracks
GROUP BY
  Composer
HAVING
  avgOfminute < 10;
```
### SELECT statement 실행 순서
1. 테이블에서 (FROM)
2. 특정 조건에 맞추어 (WHERE)
3. 그룹화 하고 (GROUP BY)
4. 만약 그룹 중에서 조건이 있다면 맞추고 (HAVING)
5. 조회하여 (SELECT)
6. 정렬하고 (ORDER BY)
7. 특정 위치의 값을 가져옴 (LIMIT)
### CREATE TABLE statement
```SQL
-- 테이블 생성
CREATE TABLE table_name (
  column_1 data_type constraints,
  column_1 data_type constraints,
  ...,
)
```
* 각 필드에 적용할 데이터 타입 작성
* 테이블 및 필드에 대한 제약조건(constraints) 작성
```SQL
-- examples 테이블 생성 및 확인
CREATE TABLE examples (
  ExamId INTEGER PRIMARY KEY AUTOINCREMENT,
  LastName VARCHAR(50) NOT NULL,
  FirstName VARCHAR(50) NOT NULL
);
```
### SQLite 데이터 타입
1. NULL
  - 아무런 값도 포함하지 않음을 나타냄
2. INTEGER
  - 정수
3. REAL
  - 부동 소수점
4. TEXT
  - 문자열
5. BLOB
  - 이미지, 동영상, 문서 등의 바이너리 데이터
### Constraints : 제약조건
테이블의 필드에 적용되는 규칙 또는 제한 사항
- 데이터의 무결성을 유지하고 데이터베이스의 일관성을 보장
* 대표적인 제약 조건
  - PRIMARY KEY
    - 해당 필드를 기본 키로 지정
      - INTEGER 타입에만 적용되며 INT, BIGINT등과 같은 정수 유형은 적용되지 않음
  - NOT NULL
    - 해당 필드에 NULL 값을 허용하지 않도록 지정
  - FOREIGN KEY
    - 다른 테이블과의 외래 키 관계를 정의
### AUTOINCREMENT keyword
자동으로 고유한 정수 값을 생성하고 할당하는 필드 속성
### AUTOINCREMENT 특징
* 필드의 자동 증가를 나타내는 특수한 키워드
* 주로 primary key필드에 적용
* INTEGER PRIMARY KEY AUTOINCREMENT가 작성된 필드는 항상 새로운 레코드에 대해 이전 최대 값보다 큰 값을 할당
* 삭제된 값은 무시되며 재사용할 수 없게 됨
### ALTER TABLE statement
테이블 및 필드 조작
### ALTER TABLE 역할
* ALTER TABLE ADD COLUMN : 필드 추가
* ALTER TABLE RENAME COLUMN : 필드 이름 변경
* ALTER TABLE DROP COLUMN : 필드 삭제
* ALTER TABLE RENAME TO : 테이블 이름 변경
* **SQLite는 modify가 없다.**
```SQL
ALTER TABLE
  table_name
ADD COLUMN
  column_definition;
```
* ADD COLUMN 키워드 이후 추가하고자 하는 새 필드의 이름과 데이터 타입 및 제약 조건 작성
### ALTER TABLE ADD COLUMN 활용
```SQL
CREATE TABLE examples (
  -- 필드 데이터타입 제약조건1, 제약조건2
  ExamId INTEGER PRIMARY KEY AUTOINCREMENT,
  LastName VARCHAR(50) NOT NULL,
  FirstName VARCHAR(50) NOT NULL
);


PRAGMA table_info('examples');

-- 컬럼 추가

ALTER TABLE
  examples
ADD COLUMN
  Country VARCHAR(100) NOT NULL;


-- examples 테이블에 다음 조건에 맞는 Age 필드 추가
ALTER TABLE
  examples
ADD COLUMN
  AGE INTEGER NOT NULL;


-- examples 테이블에 다음 조건에 맞는 Address 필드 추가
ALTER TABLE
  examples
ADD COLUMN
  Address VARCHAR(100) NOT NULL;


-- examples 테이블 Address 필드의 이름을 PostCode로 변경
ALTER TABLE
  examples
RENAME COLUMN
  Address TO PostCode;


-- examples 테이블의 PostCode필드를 삭제
ALTER TABLE examples
DROP COLUMN PostCode;


-- examples 테이블 이름을 new_examples로 변경
ALTER TABLE
  examples
RENAME TO
  new_examples;
```
### DROP TABLE statement
* 테이블 삭제
```SQL
-- examples 테이블 삭제
DROP TABLE examples;
```
### INSERT statement
* 테이블 레코드 삽입
```SQL
INSERT INTO table_name (c1, c2, ...)
VALUES (v1, v2, ...);
```
* INSERT INTO 절 다음에 테이블 이름과 괄호 안에 필드 목록 작성
* VALUES 키워드 다음 괄호 안에 해당 필드에 삽입할 값 목록 작성
### INSERT statement 실습 테이블 작성
```SQL
CREATE TABLE Articles (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title VARCHAR(100) NOT NULL,
  content VARCHAR(200) NOT NULL,
  createAt DATE NOT NULL
);


-- articles 테이블에 다음과 같은 데이터 입력
-- 모든 컬럼 명시
INSERT INTO Articles
  (id, title, content, createAt)
VALUES
  (1, 'hello', 'world', '2000-01-01');

-- 모든 컬럼을 다 넣는 경우에는 컬럼명을 생략할 수 있다.
INSERT INTO Articles
VALUES
  (2, 'hello', 'ssafy', '2002-01-01');


-- ID 를 생략하는 버전 오토인크리먼트 프라임 키를 설정했기때문에 생략가능
INSERT INTO Articles
  (title, content, createAt)
VALUES
  ('Nice', 'to meet you', '2002-01-01');


-- articles 테이블에 다음과 같은 여러 데이터를 추가 입력하기
INSERT INTO 
  articles (title, content, createAt)
VALUES
  ('title1', 'content1', '1900-01-01'),
  ('title2', 'coentent2', '1900-01-01'),
  ('title3', 'content3', '1900-01-01');
-- 일부 RDBMS만 사용가능


-- DATE 함수를 사용해 articles 테이블에 다음과 같은 데이터를 추가 입력
INSERT INTO Articles
VALUES (100, 'date', 'fucntion', DATE());
```
### 데이터 수정하기 (Update data)
* UPDATE statement : 테이블 레코드 수정
```SQL
UPDATE table_name
SET column_name = expression,
[WHERE
  condition];
```
* SET 절 다음에 수정 할 필드와 새 값을 지정
* WHERE 절에서 수정 할 레코드를 지정하는 조건 작성
* WHERE 절을 작성하지 않으면 모든 레코드를 수정
```SQL
-- 데이터 수정하기
-- 모든 데이터의 title 컬럼이 전부 수정됨
UPDATE Articles
SET title = 'new_title'


-- 조건을 명시하자
UPDATE Articles
SET title = 'new_title'
WHERE id = 1;


UPDATE Articles
SET 
  title = 'new_title',
  content = 'new_content'
WHERE id = 2;
```
### DELETE statement
테이블 레코드 삭제
```SQL
DELETE FROM table_name
[WHERE
  condition];
```
* DELETE FROM 절 다음에 테이블 이름 작성
* WHERE 절에서 삭제할 레코드를 지정하는 조건 작성
* WHERE 절을 작성하지 않으면 모든 레코드를 삭제
```SQL
-- Articles테이블의 1번 레코드 삭제
DELETE FROM
  Articles
WHERE
  id = 1;


-- Articles테이블에서 작성일이 오래된 순으로 레코드 2개 삭제
-- 서브 쿼리를 사용해야한다

-- 1. 내부 쿼리 먼저 작성
SELECT id
FROM Articles
ORDER BY createAt
LIMIT 2;

-- 2. 삭제 구문 작성
DELETE FROM Articles
WHERE id IN (
  SELECT id
  FROM Articles
  ORDER BY createAt
  LIMIT 2
);
```
### join : 관계
여러 테이블 간의 (논리적) 연결
### 관계의 필요성
* 커뮤니티 게시판에 필요한 데이터 생각해보기

| id | title | content | writer | role |
|----|-------|---------|--------|------|
| 1 | 제목1 | 내용1 | 하석주 | admin |
| 2 | 제목2 | 내용2 | 송윤미 | student |
| 3 | 제목3 | 내용3 | 유하선 | student |

* 하석주가 작성한 모든 게시글 조회하기
* 어떤 문제가 있을까? : 동명이인이 있다면, 혹은 특정 데이터가 수정된다면
```SQL
SELECT
  *
FROM
  테이블
WHERE writer = '하석주';
```
### join이 필요한 순간
* 테이블을 분리하면 데이터 관리는 용이해질 수 있으나 출력시에는 문제가 있음
* 테이블 한 개만을 출력할 수 밖에 없어 다른 테이블과 결합하여 출력하는 것이 필요해짐
### JOIN clause
둘 이상의 테이블에서 데이터를 검색하는 방법
* INNER JOIN
* LEFT JOIN
### INNER JOIN clause
두 테이블에서 값이 일치하는 레코드에 대해서만 결과를 반환
```SQL
SELECT
  select_list
FROM
  table_a
INNER JOIN table_b
  ON table_b.fk = table_a.pk;
```
* FROM 절 이후 메인 테이블 지정 (table_a)
* INNER JOIN 절 이후 메인 테이블과 조인할 테이블을 지정 (table_b)
* ON 키워드 이후 조인 조건을 작성
* 조인 조건은 table_a과 table_b 간의 레코드를 일치시키는 규칙을 지정
```SQL
-- 조인 실습하기전에 사전준비
CREATE TABLE users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name VARCHAR(50) NOT NULL
);

CREATE TABLE newarticles (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title VARCHAR(50) NOT NULL,
  content VARCHAR(100) NOT NULL,
  userId INTEGER NOT NULL,
  FOREIGN KEY (userId) REFERENCES users(id)
);


INSERT INTO users
  (name)
VALUES
  ('하석주'), ('송윤미'), ('유하선');

INSERT INTO newarticles
  (title, content, userId)
VALUES
  ('제목1', '내용1', 1),
  ('제목2', '내용2', 2),
  ('제목3', '내용3', 1),
  ('제목4', '내용4', 4),
  ('제목5', '내용5', 1);
-- 사전준비 종료

-- 전체 데이터를 조인
SELECT *
FROM users INNER JOIN newarticles
ON users.id = newarticles.userId;


-- 테이블을 특정하고 싶다면 필드들을 선언하고 조인
-- WHERE을 사용해서 더욱더 필터링 할 수 있다.
SELECT newarticles.title, users.id
FROM users INNER JOIN newarticles
ON users.id = newarticles.userId
WHERE users.id = 1;
```
### LEFT JOIN clause
오른쪽 테이블의 일치하는 레코드와 함께 왼쪽 테이블의 모든 레코드 반환
```SQL
SELECT
  select_list
FROM
  table_a
INNER JOIN table_b
  ON table_b.fk = table_a.pk;
```
* FROM 절 이후 왼쪽 테이블 지정 (table_a)
* LEFT JOIN 절 이후로 오른쪽 테이블 지정 (table_b)
* ON 키워드 이후 조인 조건을 작성
  - 왼쪽 테이블의 각 레코드를 오른쪽 테이블의 모든 레코드와 일치시킴

```SQL
-- 이너 조인과 다르게 래프트 조인은 어떤 테이블이 왼쪽에 두냐에 따라 값이 달라진다.
SELECT * 
FROM newarticles LEFT JOIN users
  ON users.id = newarticles.userId;

-- 순서가 달라지니 위와 값이 다르다
SELECT * 
FROM users LEFT JOIN newarticles
  ON users.id = newarticles.userId;


-- 게시글 작성 이력이 없는 회원 정보 조회하기
SELECT * 
FROM users LEFT JOIN newarticles
  ON users.id = newarticles.userId
WHERE newarticles.userId IS NULL;
```