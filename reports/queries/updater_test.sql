SELECT year, month, day, primary_type, COUNT(primary_type) AS rate FROM chicago_crime.crime
WHERE year = 2019
GROUP BY day, primary_type
HAVING rate > 0
ORDER BY month ASC, day ASC;

SELECT * FROM chicago_crime.crime
WHERE year = 2019 AND month = 5 AND day >= 10;

