<<<<<<< HEAD
-- Script that creates the MySQL server user user_0d_1
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';


=======
-- create user and grant privileges
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost'
IDENTIFIED BY 'user_0d_1_pwd';
-- grant privileges
GRANT ALL PRIVILEGES
ON *.*
TO 'user_0d_1'@'localhost' WITH GRANT OPTION;
>>>>>>> f87d9a95787dde15a905f7ffe759820dd508082a
