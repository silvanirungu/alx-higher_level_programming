-- create user and grant privileges
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost'
IDENTIFIED BY 'user_0d_1_pwd';
-- grant privileges
GRANT ALL PRIVILEGES
ON *.*
TO 'user_0d_1'@'localhost' WITH GRANT OPTION;