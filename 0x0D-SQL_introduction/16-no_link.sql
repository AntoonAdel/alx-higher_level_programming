-- List and order all records in the second_table that
-- Dont have a blank name
SELECT `score`, `name` FROM `second_table`
WHERE `name` IS NOT NULL
ORDER BY `score` DESC
