USE ctftraining;
SET FOREIGN_KEY_CHECKS=0;

CREATE TABLE flag (flag VARCHAR(255) NOT NULL);

CREATE TABLE passage
(
    id int PRIMARY KEY AUTO_INCREMENT,
    content varchar(1000)
);


INSERT INTO passage values(NULL, 'Hello, glzjin wants a girlfriend.'),(NULL, 'Do you want to be my girlfriend?')
