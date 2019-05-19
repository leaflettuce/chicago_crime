select id, year, primary_type, ward from chicago_crime.crime
WHERE year >= 2018
ORDER BY id DESC
LIMIT 100;