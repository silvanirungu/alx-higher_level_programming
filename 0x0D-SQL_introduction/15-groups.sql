-- select score
SELECT score, COUNT(score) as number
-- select table
FROM second_table
-- count the scores
GROUP BY score;