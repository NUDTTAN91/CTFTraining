create database dropbox;

use dropbox;

CREATE TABLE users
(
    id int PRIMARY KEY AUTO_INCREMENT,
    username varchar(100),
    password varchar(100)
);
