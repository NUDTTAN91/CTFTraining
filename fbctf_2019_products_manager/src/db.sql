CREATE DATABASE IF NOT EXISTS facebook;

USE facebook;

CREATE TABLE IF NOT EXISTS products (name char(64),secret char(64),description varchar(250));

INSERT INTO products VALUES('messenger', sha2('efiuyf93fhewof3yhnokleohfecweefewf', 256), '1'),
('instagram', sha2('efoh3fio3h2fo3hdewyfew890f', 256), '2'),
('whatsapp', sha2('ewlkfhj3io4fhewcbjkleouihfcrfw', 256), '3'),
('oculus-rift', sha2('ewfgjkewhfui3h2f32', 256), '4');
