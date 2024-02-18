<<<<<<< HEAD
-- Lists the number of records with the same score in the table second_table.
-- Records are ordered by descending count.
SELECT `score`, COUNT(*) AS `number`
FROM `second_table`
GROUP BY `score`
ORDER BY `number` DESC;
=======
-- select score
SELECT score, COUNT(score) as number
-- select table
FROM second_table
-- count the scores
GROUP BY score;
>>>>>>> f87d9a95787dde15a905f7ffe759820dd508082a
