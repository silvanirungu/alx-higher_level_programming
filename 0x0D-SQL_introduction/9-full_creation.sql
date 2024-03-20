<<<<<<< HEAD
-- Creates and fills a table second_table with attributes id, name and score.
CREATE TABLE IF NOT EXISTS `second_table` (`id` INT, `name` VARCHAR(256), `score` INT);
INSERT INTO `second_table` (`id`, `name`, `score`) VALUES (1, "John", 10);
INSERT INTO `second_table` (`id`, `name`, `score`) VALUES (2, "Alex", 3);
INSERT INTO `second_table` (`id`, `name`, `score`) VALUES (3, "Bob", 14);
INSERT INTO `second_table` (`id`, `name`, `score`) VALUES (4, "George", 8);
=======
-- create and enter records
CREATE TABLE IF NOT EXISTS second_table
(
    id INT,
    name VARCHAR(256),
    score INT
);
INSERT INTO second_table(id, name, score)
VALUES(1, 'John', 10),
(2, 'Alex', 3),
(3, 'Bob', 14),
(4, 'George', 8);
>>>>>>> f87d9a95787dde15a905f7ffe759820dd508082a
