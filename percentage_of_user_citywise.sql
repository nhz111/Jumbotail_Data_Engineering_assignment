/* 2. Evaluation of the performance of different cities: This evaluation is based on the percentage of users from each city. It allows us to
assess how well or poorly different cities are performing in terms of user engagement with the application. By analyzing the distribution
of users across cities, we can identify which cities have a higher or lower percentage of users using the app. */

SELECT
  city,
  COUNT(*) AS count,
  (COUNT(*) / TOTAL_USERS) * 100 AS percentage
FROM user_journey
GROUP BY city
ORDER BY percentage DESC;


-- approach 2

SELECT COUNT() AS total_users,
ROUND(100 * (COUNT() / (SELECT COUNT(*) FROM events WHERE city = 'Banglore')), 2) AS percentage
FROM events
WHERE stage = 'Placed order' AND city = 'Banglore';