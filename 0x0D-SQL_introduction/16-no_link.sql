-- insert new values
INSERT INTO second_table (score, name)
   VALUES (18, 'Aria'), (12, 'Aria');
-- delete id 4
DELETE FROM second_table
    WHERE name = 'George';
-- show results
SELECT score, name
    FROM second_table
    ORDER BY score DESC;