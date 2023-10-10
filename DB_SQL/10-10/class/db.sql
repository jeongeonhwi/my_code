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
ALTER TABLE examples
RENAME TO new_examples;


-- examples 테이블 삭제
DROP TABLE examples;