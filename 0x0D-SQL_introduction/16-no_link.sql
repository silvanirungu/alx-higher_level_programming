-- new table
INSERT INTO second_table (score, name)
   VALUES (18, 'Aria'), (12, 'Aria');
DELETE FROM second_table
    WHERE name = 'George';
SELECT score, name
    FROM second_table
    ORDER BY score DESC;