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