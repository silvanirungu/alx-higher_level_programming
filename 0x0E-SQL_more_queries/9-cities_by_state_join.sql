<<<<<<< HEAD
-- Script that lists all the cities that can be found in the database hbtn_0d_usa
SELECT `cities`.`id`, `cities`.`name`, `states`.`name`
FROM `cities`
JOIN `states`
ON `cities`.`state_id` = `states`.`id`
ORDER BY `cities`.`id` ASC;

=======
-- show city id, city name and state name
-- sorted in asc city id
-- join city and states table by id
SELECT cities.id AS id, cities.name AS name, states.name AS name
FROM cities
INNER JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;
>>>>>>> f87d9a95787dde15a905f7ffe759820dd508082a
