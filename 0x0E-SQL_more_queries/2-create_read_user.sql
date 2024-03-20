<<<<<<< HEAD
-- Script that creates the database hbtn_0d_2 and the user user_0d_2
CREATE DATABASE IF NOT EXISTS `hbtn_0d_2`;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT
ON `hbtn_0d_2`.*
TO 'user_0d_2'@'localhost';
=======
-- create database and user and grant permissions
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost'
IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT
ON hbtn_0d_2.*
TO 'user_0d_2'@'localhost';
>>>>>>> f87d9a95787dde15a905f7ffe759820dd508082a
