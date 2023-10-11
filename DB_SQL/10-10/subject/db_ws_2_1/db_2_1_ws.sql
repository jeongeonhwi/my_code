CREATE TABLE animals (
  PK INTEGER PRIMARY KEY AUTOINCREMENT,
  animal_name TEXT NOT NULL,
  height INTEGER NOT NULL,
  weight INTEGER NOT NULL,
  age INTEGER
);


-- 2 meal 칼럼 추가하기
ALTER TABLE animals
ADD COLUMN meal TEXT;

-- 3. 첫번째 칼럼인 animal_name의 명칭을 name으로 수정하시오
ALTER TABLE animals
RENAME COLUMN animal_name TO name;

-- 4. 테이블의 명칭을 animals에서 zoo로 변경하시오
ALTER TABLE animals
RENAME TO zoo;

-- 5. zoo 테이블을 삭제하시오.
DROP TABLE zoo;