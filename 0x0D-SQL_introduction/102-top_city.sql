-- list the 3 most hotests cities
SELECT `city`, AVG(`value`) AS `top_temp` FROM `temperatures`
WHERE `month` = 7 OR `month` = 8
GROUP BY `city`
ORDER BY `top_temp` DESC
LIMIT 3;
