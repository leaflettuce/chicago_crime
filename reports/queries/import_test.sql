select id, year, primary_type, ward from chicago_crime.crime
WHERE year = 2019
ORDER BY id DESC
LIMIT 100;