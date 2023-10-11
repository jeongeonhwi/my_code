SELECT first_name, country
FROM users
WHERE first_name = '건우' AND country='경기도';

SELECT first_name, country
FROM users
WHERE first_name != '건우' AND country != '경기도'
ORDER BY age ASC;