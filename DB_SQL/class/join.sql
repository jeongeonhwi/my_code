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