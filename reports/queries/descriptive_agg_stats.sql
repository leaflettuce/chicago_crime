############################
# Annual daily crime rate  #
############################

SELECT year, AVG(daily_counts.counts) AS average

FROM (
SELECT year, day, COUNT(*) AS counts
FROM chicago_crime.crime
GROUP BY year, month, day
) AS daily_counts

GROUP BY year
ORDER BY year ASC;


##########################
# AVG monthly rate trend #
##########################

SELECT month, AVG(monthly_counts.counts) AS average

FROM (
SELECT year, month, COUNT(*) AS counts
FROM chicago_crime.crime
GROUP BY year, month
) AS monthly_counts

GROUP BY month
ORDER BY month ASC;


##########################
# AVG rate by crime type #
##########################

SELECT primary_type, AVG(type_counts.counts) AS daily_average

FROM (
SELECT year, month, day, primary_type, COUNT(*) AS counts
FROM chicago_crime.crime
GROUP BY year, month, day, primary_type
) AS type_counts

GROUP BY primary_type
ORDER BY daily_average DESC;


###########################
# crime rates by location #
###########################

SELECT community AS location, AVG(type_counts.counts) AS daily_average

FROM (
SELECT year, month, day, community, COUNT(*) AS counts
FROM chicago_crime.crime
WHERE community IS NOT NULL
GROUP BY year, month, day, community
) AS type_counts

GROUP BY location
ORDER BY location ASC; # see map for community location