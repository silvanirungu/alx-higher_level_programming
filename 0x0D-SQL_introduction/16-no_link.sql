<<<<<<< HEAD
-- Lists all records of the table second_table having a name value.
-- Records are ordered by descending score.
SELECT `score`, `name`
FROM `second_table`
WHERE `name` != ""
ORDER BY `score` DESC
=======
-- get records
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
>>>>>>> f87d9a95787dde15a905f7ffe759820dd508082a
