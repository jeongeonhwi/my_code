SELECT first_name, phone, country
FROM users
WHERE phone LIKE '%-51__-____' AND country != '서울';
