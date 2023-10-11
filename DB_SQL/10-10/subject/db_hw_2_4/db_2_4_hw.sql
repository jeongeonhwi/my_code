-- 테이블을 생성
CREATE TABLE zoo (
  name TEXT NOT NULL,
  eat TEXT NOT NULL,
  weight INT NOT NULL,
  height INT,
  age INT
);

-- 레코드 작성
INSERT INTO zoo VALUES 
('gorilla', 'omnivore', 215, 180, 5),
('tiger', 'carnivore', 220, 115, 3),
('elephant', 'herbivore', 3800, 280, 10),
('dog', 'omnivore', 8, 20, 1),
('panda', 'herbivore', 80, 90, 2),
('pig', 'omnivore', 70, 45, 5);


-- 비긴 트렌젝션을 선언하고 삭제를 진행하고 롤백을 하면 삭제라는 명령어를 무효화 한다
BEGIN;
  DELETE FROM zoo
  WHERE weight < 100;
ROLLBACK;
-- 비긴 트렌젝션을 선언하고 커밋을 하면 삭제된다.
BEGIN;
  DELETE FROM zoo
  WHERE eat = 'omnivore';
COMMIT;

-- 셀렉은 해당하는 정보들을 보여준다
SELECT COUNT(*)
FROM zoo;
