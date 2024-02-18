<<<<<<< HEAD
-- Lists all cities of CA in the database hbtn_0d_usa.
-- Results are ordered by ascending cities.id.
SELECT `id`, `name`
  FROM `cities`
 WHERE `state_id` IN
       (SELECT `id`
	  FROM `states`
	 WHERE `name` = "California")
 ORDER BY `id`;
=======
-- list all cities of the state of california
-- results sorted in ascending order by cities id
-- don't use join
-- 1. get state id of california from states
-- 2. get names of cities matching the state id from cities
SELECT id, name
FROM cities
WHERE state_id = 
(
    SELECT id
     FROM states
     WHERE name = 'California'
)
ORDER BY id ASC;
>>>>>>> f87d9a95787dde15a905f7ffe759820dd508082a
