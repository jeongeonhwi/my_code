CREATE TABLE contacts (
  PK INTEGER PRIMARY KEY AUTOINCREMENT,
  email TEXT NOT NULL UNIQUE,
  name TEXT NOT NULL,
  age INTEGER NOT NULL
);

INSERT INTO contacts
  (email, name, age)
VALUES
  ('ssafy@naver.com', 'ssafy', 21);