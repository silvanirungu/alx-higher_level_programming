-- show city id, city name and state name
-- sorted in asc city id
-- join city and states table by id
SELECT cities.id AS id, cities.name AS name, states.name AS name
FROM cities
INNER JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;