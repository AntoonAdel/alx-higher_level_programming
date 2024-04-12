-- maximum temperature of each state
SELECT `state`, MAX(value) AS `max_temperature`
FROM `temperatures`
GROUP BY `state`
ORDER BY `state`;
