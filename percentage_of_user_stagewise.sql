/*1. Percentage of users in each stage of the user journey: This indicates the proportion of users at each stage of the journey within the
application. It provides insights into how users progress through the different steps of the app. */

SELECT
  stage,
  COUNT(*) AS count,
  (COUNT(*) / TOTAL_USERS) * 100 AS percentage
FROM user_journey
GROUP BY stage
ORDER BY percentage DESC;


--approach2

SELECT COUNT(*) AS total_users,
       ROUND(100 * (COUNT() / (SELECT COUNT() FROM events)), 2) AS percentage
FROM events
WHERE stage = 'Placed order';


