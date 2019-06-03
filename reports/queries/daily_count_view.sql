CREATE VIEW `new_view` AS
SELECT year, month, day, primary_type,  COUNT(*) AS count
FROM chicago_crime.crime
GROUP BY year, month, day, primary_type
ORDER BY year ASC, month ASC, day ASC;